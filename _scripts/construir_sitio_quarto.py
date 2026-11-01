#!/usr/bin/env python3
"""
Construye el sitio Quarto del Repositorio FCA a partir de carreras/.

Lee los _info.yml (carrera y materia) y el README.md (con encabezado YAML) de cada
ejercicio, y genera un proyecto Quarto en sitio/ con:
  - catálogo con buscador, filtros por categoría y ordenamiento
  - una página por carrera y por materia
  - una página por ejercicio, con la solución y la guía docente plegadas
  - los materiales de cada ejercicio (casos, hojas, tableros, datos)

Uso:
    python3 _scripts/construir_sitio_quarto.py
    cd sitio && quarto render        # o: quarto preview
"""
import re
import shutil
from pathlib import Path

import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ejercicio_io import es_ejercicio, leer_ejercicio  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CARRERAS = RAIZ / "carreras"
PLANTILLA = RAIZ / "_scripts" / "quarto"          # _quarto.yml, estilos, plantillas EJS
SALIDA = RAIZ / "sitio"

COLOR_CARRERA = {
    "contador-publico": "cp",
    "comercio-exterior-aduanas": "cea",
    "administracion-empresas": "ae",
    "materias-comunes": "mc",
}

# Ejercicios con un bloque interactivo extra (Observable JS, corre en el navegador)
INTERACTIVOS = {
    "ciclo-conversion-efectivo": "interactivo-cce.qmd",
}


def leer_yaml(p: Path) -> dict:
    if not p.exists():
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def fm(d: dict) -> str:
    """Front matter YAML. Omite los campos vacíos: Quarto rechaza, por ejemplo,
    un `subtitle` nulo cuando un ejercicio no trae tema, y eso tiraba el sitio."""
    d = {k: v for k, v in d.items() if v is not None and v != "" and v != "None"}
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n"


def secciones(md: str):
    """Divide un Markdown en (titulo_h2, texto) respetando bloques de código."""
    partes, actual, titulo, en_codigo = [], [], None, False
    for linea in md.splitlines():
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
        if not en_codigo and linea.startswith("## "):
            partes.append((titulo, "\n".join(actual)))
            titulo, actual = linea[3:].strip(), []
        else:
            actual.append(linea)
    partes.append((titulo, "\n".join(actual)))
    return partes


def quitar_encabezado(md: str) -> str:
    """Quita el H1 y las líneas **Carrera:** ... (ya van en la ficha)."""
    lineas = md.splitlines()
    out, en_cab = [], True
    for l in lineas:
        if en_cab and (l.startswith("# ") or re.match(r"^\*\*[^*]+:\*\*", l) or not l.strip()):
            continue
        en_cab = False
        out.append(l)
    return "\n".join(out)


def bajar_titulos(md: str, niveles=1) -> str:
    out, en_codigo = [], False
    for l in md.splitlines():
        if l.strip().startswith("```"):
            en_codigo = not en_codigo
        if not en_codigo and re.match(r"^#{1,5} ", l):
            l = "#" * niveles + l
        out.append(l)
    return "\n".join(out)


def primer_parrafo(md: str, limite=190) -> str:
    for titulo, texto in secciones(md):
        if titulo and titulo.lower().startswith("objetivo"):
            p = " ".join(texto.strip().split("\n\n")[0].split())
            p = re.sub(r"[*_`]", "", p)
            return p if len(p) <= limite else p[: limite].rsplit(" ", 1)[0] + "…"
    return ""


def callout(tipo: str, titulo: str, cuerpo: str, plegado=True, ident="") -> str:
    col = ' collapse="true"' if plegado else ""
    idt = f"#{ident} " if ident else ""
    return f'::: {{{idt}.callout-{tipo}{col} title="{titulo}"}}\n\n{bajar_titulos(cuerpo, 2)}\n:::\n'


def materiales_md(dir_ej: Path) -> str:
    mat = dir_ej / "materiales"
    if not mat.is_dir():
        return ""
    filas = []
    for f in sorted(mat.iterdir()):
        if f.name.startswith("."):
            continue
        nombre = f.stem.split("-", 1)[-1].replace("-", " ").capitalize() if f.stem[:2].isdigit() else f.stem.replace("-", " ").capitalize()
        ext = f.suffix.lower()
        if ext == ".md":
            tipo, href = "Documento", f"materiales/{f.stem}.html"
        elif ext == ".html":
            tipo, href = "Tablero interactivo", f"materiales/{f.name}"
        elif ext == ".csv":
            tipo, href = "Datos (CSV)", f"materiales/{f.name}"
        elif ext == ".svg":
            tipo, href = "Imagen", f"materiales/{f.name}"
        else:
            tipo, href = ext[1:].upper(), f"materiales/{f.name}"
        filas.append(f'<a class="mat" href="{href}"><span class="mat-tipo">{tipo}</span><span class="mat-nombre">{nombre}</span></a>')
    return '\n## Materiales del ejercicio\n\n```{=html}\n<div class="mat-grid">\n' + "\n".join(filas) + "\n</div>\n```\n"


def construir_ejercicio(dir_ej: Path, destino: Path, slug_carrera: str, carrera: str, materia: str):
    meta, readme = leer_ejercicio(dir_ej)
    # la carpeta manda: así un ejercicio creado desde el CMS queda en su carrera y materia
    meta["carrera"], meta["materia"] = carrera, materia
    cuerpo = quitar_encabezado(readme)
    cuerpo = cuerpo.replace("](GUIA-DOCENTE.md)", "](#guia-docente)").replace("](solucion.md)", "](#solucion)").replace("](./solucion.md)", "](#solucion)")
    # el callout plegable reemplaza a los <details> que algunos README ya traen
    cuerpo = re.sub(r"^\s*</?details[^>]*>\s*$|^\s*<summary>.*?</summary>\s*$", "", cuerpo, flags=re.M)
    sol_extra = dir_ej / "solucion.md"
    sol_extra = quitar_encabezado(sol_extra.read_text(encoding="utf-8")) if sol_extra.exists() else ""

    bloques = []
    for titulo, texto in secciones(cuerpo):
        if titulo is None:
            if texto.strip():
                bloques.append(texto.strip() + "\n")
            continue
        t = titulo.lower()
        if t.startswith("solución") or t.startswith("solucion"):
            bloques.append(callout("tip", "Solución / guía de solución (clic para mostrar)",
                                   texto + "\n\n" + sol_extra, ident="solucion"))
        else:
            bloques.append(f"## {titulo}\n{texto}\n")
            if t.startswith("ejercicio") and dir_ej.name in INTERACTIVOS:
                extra = (PLANTILLA / INTERACTIVOS[dir_ej.name]).read_text(encoding="utf-8")
                bloques.append(extra)

    guia = dir_ej / "GUIA-DOCENTE.md"
    if guia.exists():
        g = quitar_encabezado(guia.read_text(encoding="utf-8"))
        bloques.append(callout("note", "Guía docente (solo profesores)", g, ident="guia-docente"))

    bloques.append(materiales_md(dir_ej))

    ficha = {
        "Nivel": meta.get("nivel"),
        "Duración": meta.get("duracion_estimada"),
        "Tipo": meta.get("tipo"),
        "Modalidad": meta.get("modalidad"),
        "Entregable": meta.get("entregable_alumno"),
    }
    ficha_html = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in ficha.items() if v)
    ia = meta.get("asistencia_ia")
    revisado = meta.get("revisado_por_docente")
    estado = ""
    if revisado is False:
        estado = '<p class="estado pendiente">Pendiente de revisión docente</p>'
    elif revisado is True:
        estado = '<p class="estado ok">Revisado por docente</p>'
    margen = (
        '::: {.column-margin}\n```{=html}\n<div class="ficha">'
        f'<p class="ficha-titulo">Ficha del ejercicio</p><dl>{ficha_html}</dl>{estado}'
        + (f'<details class="ia"><summary>Uso de IA en este material</summary><p>{ia}</p></details>' if ia else "")
        + "</div>\n```\n:::\n\n"
    )

    front = {
        "title": meta.get("titulo", dir_ej.name),
        "subtitle": meta.get("tema"),
        "author": meta.get("autor"),
        "date": str(meta.get("fecha") or ""),
        "description": primer_parrafo(readme),
        "categories": [c for c in [meta.get("materia"), meta.get("nivel")] if c],
        "carrera": meta.get("carrera"),
        "carrera_slug": COLOR_CARRERA.get(slug_carrera, "mc"),
        "materia": meta.get("materia"),
        "nivel": meta.get("nivel"),
        "duracion": meta.get("duracion_estimada"),
        "tags": meta.get("tags", []),
        "title-block-banner": True,
        "body-classes": f"ejercicio car-{COLOR_CARRERA.get(slug_carrera, 'mc')}",
    }
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "index.qmd").write_text(fm(front) + margen + "\n".join(bloques), encoding="utf-8")

    # Materiales y archivos de apoyo
    for f in dir_ej.iterdir():
        if f.is_dir() and f.name == "materiales":
            shutil.copytree(f, destino / "materiales", dirs_exist_ok=True)
        elif f.is_file() and f.suffix.lower() in {".csv", ".svg", ".png", ".jpg", ".xlsx"}:
            shutil.copy2(f, destino / f.name)
    return meta


def pagina_listado(titulo, subtitulo, contenidos, destino: Path, extra_fm=None, cuerpo=""):
    d = {
        "title": titulo,
        "subtitle": subtitulo,
        "listing": {
            "id": "ejercicios",
            "contents": contenidos,
            "template": "../" * (len(destino.relative_to(SALIDA).parts) - 1) + "_plantillas/tarjeta.ejs",
            "sort": "title",
            "sort-ui": ["title", "date", "nivel", "duracion"],
            "filter-ui": True,
            "categories": True,
            "page-size": 24,
            "fields": ["title", "date", "author", "description", "categories", "carrera", "materia", "nivel", "duracion"],
            "field-display-names": {"title": "Título", "date": "Fecha", "nivel": "Nivel", "duracion": "Duración"},
        },
        "page-layout": "full",
        "title-block-banner": True,
    }
    if extra_fm:
        d.update(extra_fm)
    d = {k: v for k, v in d.items() if v is not None}
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(fm(d) + cuerpo + "\n::: {#ejercicios}\n:::\n", encoding="utf-8")


def main():
    if SALIDA.exists():
        for p in SALIDA.iterdir():
            if p.name in {"_site", ".quarto", "_freeze"}:
                continue
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    SALIDA.mkdir(exist_ok=True)
    shutil.copytree(PLANTILLA, SALIDA, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("interactivo-*.qmd"))
    shutil.copytree(RAIZ / "assets" / "img", SALIDA / "assets" / "img", dirs_exist_ok=True)

    carreras, n_ej, materias_total, autores = [], 0, 0, set()
    for dc in sorted(p for p in CARRERAS.iterdir() if p.is_dir()):
        info_c = leer_yaml(dc / "_info.yml")
        mats = []
        for dm in sorted(p for p in dc.iterdir() if p.is_dir() and not p.name.startswith("_")):
            if es_ejercicio(dm):
                print(f"AVISO: {dm.relative_to(RAIZ)} es un ejercicio fuera de una materia; no se publica.")
                continue
            info_m = leer_yaml(dm / "_info.yml")
            ejs = [p for p in sorted(dm.iterdir()) if es_ejercicio(p)]
            if not ejs:
                continue
            for de in ejs:
                meta = construir_ejercicio(de, SALIDA / "carreras" / dc.name / dm.name / de.name, dc.name,
                                           info_c.get("nombre", dc.name), info_m.get("nombre", dm.name))
                if meta.get("autor"):
                    autores.add(meta["autor"])
            n_ej += len(ejs)
            mats.append((dm.name, info_m.get("nombre", dm.name), info_m.get("descripcion", ""), len(ejs), info_m.get("orden", 99)))
            pagina_listado(info_m.get("nombre", dm.name), info_m.get("descripcion", ""), "*/index.qmd",
                           SALIDA / "carreras" / dc.name / dm.name / "index.qmd",
                           {"categories-title": "Temas"} if False else None)
        if not mats:
            continue
        materias_total += len(mats)
        mats.sort(key=lambda m: (m[4], m[1]))
        chips = "".join(
            f'<a class="chip-materia" href="{m[0]}/index.html">{m[1]} <span>{m[3]}</span></a>' for m in mats)
        pagina_listado(info_c.get("nombre", dc.name), info_c.get("descripcion", ""), "*/*/index.qmd",
                       SALIDA / "carreras" / dc.name / "index.qmd",
                       cuerpo=f'```{{=html}}\n<div class="chips-materias">{chips}</div>\n```\n')
        carreras.append((dc.name, info_c.get("nombre", dc.name), info_c.get("descripcion", ""),
                         sum(m[3] for m in mats), len(mats), info_c.get("orden", 99)))

    carreras.sort(key=lambda c: c[5])
    tarjetas = "".join(
        f'<a class="carrera car-{COLOR_CARRERA.get(c[0], "mc")}" href="carreras/{c[0]}/index.html">'
        f'<span class="carrera-n">{c[3]}</span><span class="carrera-nombre">{c[1]}</span>'
        f'<span class="carrera-desc">{c[2]}</span><span class="carrera-mat">{c[4]} materia{"s" if c[4] != 1 else ""}</span></a>'
        for c in carreras)
    hero = (
        "```{=html}\n"
        '<section class="hero"><div class="hero-txt">'
        '<p class="kicker">Facultad de Contaduría y Administración · Unidad Torreón</p>'
        '<h1>Ejercicios para enseñar con IA, listos para el aula</h1>'
        '<p class="lead">Un catálogo abierto, al estilo del repositorio de datos de UC Irvine, pero de métodos de clase: '
        'cada ejercicio trae teoría, caso práctico, solución, prompts probados y materiales.</p></div>'
        f'<dl class="stats"><div><dt>{n_ej}</dt><dd>ejercicios</dd></div><div><dt>{materias_total}</dt><dd>materias</dd></div>'
        f'<div><dt>{len(carreras)}</dt><dd>áreas</dd></div><div><dt>{len(autores)}</dt><dd>docentes autores</dd></div></dl></section>\n'
        f'<h2 class="sec">Explorar por carrera</h2><div class="carreras">{tarjetas}</div>\n'
        '<h2 class="sec">Todos los ejercicios</h2>\n'
        "```\n"
    )
    pagina_listado("Repositorio FCA", None, "carreras/*/*/*/index.qmd", SALIDA / "index.qmd",
                   {"title-block-banner": False, "pagetitle": "Repositorio FCA",
                    "title": None}, cuerpo=hero)

    # Página para contribuir
    contrib = (RAIZ / "_docs" / "CONTRIBUIR.md").read_text(encoding="utf-8")
    contrib = re.sub(r"^# .*\n", "", contrib, count=1)
    (SALIDA / "contribuir.qmd").write_text(fm({"title": "Cómo contribuir", "subtitle": "Agrega un ejercicio al repositorio"}) + contrib, encoding="utf-8")

    # Navegación de carreras en _quarto.yml
    q = (SALIDA / "_quarto.yml").read_text(encoding="utf-8")
    menu = "\n".join(f'          - text: "{c[1]}"\n            href: carreras/{c[0]}/index.qmd' for c in carreras)
    (SALIDA / "_quarto.yml").write_text(q.replace("          #CARRERAS#", menu), encoding="utf-8")
    print(f"Sitio generado en {SALIDA}: {n_ej} ejercicios, {materias_total} materias, {len(carreras)} carreras.")


if __name__ == "__main__":
    main()
