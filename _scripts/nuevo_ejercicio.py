#!/usr/bin/env python3
"""
Crea el esqueleto de un ejercicio nuevo (carpeta + README.md + metadata.yml +
index.html) dentro de una carrera y materia — creando la carrera y/o la
materia si todavía no existen.

Uso interactivo:
    python3 _scripts/nuevo_ejercicio.py

Uso con argumentos:
    python3 _scripts/nuevo_ejercicio.py \\
        --carrera "Administración de Empresas" \\
        --materia "Gestión de Operaciones" \\
        --titulo "Punto de Equilibrio" \\
        --tema "Análisis costo-volumen-utilidad" \\
        --nivel "Introductorio" \\
        --duracion "40 min" \\
        --autor "Iván de Luna-Aldape"

Después de correr este script:
  1. Llena la teoría, el ejercicio, la solución y el prompt sugerido en el
     README.md que se creó (y opcionalmente en su index.html).
  2. Corre `python3 _scripts/generar_indices.py` para actualizar todos los
     índices (raíz, carrera, materia) automáticamente.
"""
import argparse
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARRERAS_DIR = ROOT / "carreras"


def slugify(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")


def ask(prompt, default=None):
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val or default or ""


def _norm(texto):
    """Normaliza para comparar nombres sin importar acentos/mayúsculas."""
    return slugify(texto)


def _find_existing(parent_dir, nombre):
    """Busca, entre las subcarpetas de parent_dir, una cuyo _info.yml tenga
    un 'nombre' que normalice igual al que se está buscando (evita crear
    'administracion-de-empresas' cuando ya existe 'administracion-empresas')."""
    if not parent_dir.exists():
        return None
    objetivo = _norm(nombre)
    for d in sorted(parent_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        info_path = d / "_info.yml"
        if info_path.exists():
            try:
                info = read_yaml_simple(info_path)
            except Exception:
                info = {}
            nombre_existente = info.get("nombre", d.name)
        else:
            nombre_existente = d.name
        if _norm(nombre_existente) == objetivo:
            return d.name
        # también compara contra el slug de la carpeta, por si no tiene _info.yml
        if _norm(d.name) == objetivo:
            return d.name
    return None


def read_yaml_simple(path):
    try:
        import yaml
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        # fallback mínimo sin PyYAML: parsea líneas "clave: valor"
        data = {}
        with open(path, encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    k, _, v = line.partition(":")
                    data[k.strip()] = v.strip().strip('"')
        return data


def ensure_carrera(nombre, descripcion=""):
    existente = _find_existing(CARRERAS_DIR, nombre)
    if existente:
        return existente

    slug = slugify(nombre)
    base = CARRERAS_DIR / slug
    base.mkdir(parents=True, exist_ok=True)
    n_existentes = len([d for d in CARRERAS_DIR.iterdir() if d.is_dir()]) if CARRERAS_DIR.exists() else 0
    (base / "_info.yml").write_text(
        f'nombre: "{nombre}"\n'
        f'descripcion: "{descripcion or "(agrega una descripción breve en este archivo)"}"\n'
        f'orden: {n_existentes + 1}\n',
        encoding="utf-8",
    )
    print(f"  ✔ Carrera nueva creada: {nombre} ({slug})")
    return slug


def ensure_materia(carrera_slug, nombre, descripcion=""):
    carrera_dir = CARRERAS_DIR / carrera_slug
    existente = _find_existing(carrera_dir, nombre)
    if existente:
        return existente

    slug = slugify(nombre)
    base = carrera_dir / slug
    base.mkdir(parents=True, exist_ok=True)
    materia_dirs = [d for d in carrera_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
    (base / "_info.yml").write_text(
        f'nombre: "{nombre}"\n'
        f'descripcion: "{descripcion or "(agrega una descripción breve en este archivo)"}"\n'
        f'orden: {len(materia_dirs)}\n',
        encoding="utf-8",
    )
    print(f"  ✔ Materia nueva creada: {nombre} ({slug})")
    return slug


README_TEMPLATE = """# {titulo}

**Carrera:** {carrera}
**Materia:** {materia}
**Tema:** {tema}
**Nivel:** {nivel}
**Duración estimada:** {duracion}

## Objetivo de aprendizaje

[¿Qué debe poder hacer el alumno al terminar este ejercicio?]

## Teoría

> Nota de transparencia: indicar aquí qué partes de esta sección fueron redactadas por el profesor y cuáles se apoyaron en IA.

[Desarrollo teórico necesario para resolver el ejercicio: definiciones, fórmulas, contexto.]

## Ejercicio / caso práctico

[Planteamiento del ejercicio o caso que resolverán los alumnos.]

## Solución / guía de solución

[Puede omitirse del README.md público si no se quiere exponer a los alumnos.]

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

```
[Prompt sugerido — reemplazar con el prompt real del ejercicio]
```

**Documentos a adjuntar:** [indicar si se requiere adjuntar algún documento, o escribir "Ninguno" si los datos del caso caben en el prompt]

## Recursos adicionales

- [Plantillas, lecturas, datasets de apoyo]
"""

METADATA_TEMPLATE = """titulo: "{titulo}"
carrera: "{carrera}"
materia: "{materia}"
tema: "{tema}"
nivel: "{nivel}"
duracion_estimada: "{duracion}"
tipo: "Ejercicio práctico"
asistencia_ia: "[describir qué tanto se usó IA para redactar este ejercicio]"
autor: "{autor}"
fecha: "{fecha}"
tags: []
"""

INDEX_HTML_TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} — Repositorio FCA</title>
<link rel="stylesheet" href="../../../../assets/style.css">
</head>
<body>

<header class="site-header">
  <div class="top">
    <div class="brand">
      <span class="kicker">Facultad de Contaduría y Administración</span>
      <h1><a href="../../../../index.html">Repositorio de Métodos y Ejercicios</a></h1>
    </div>
    <nav class="top-nav">
      <a href="../../../../index.html">Inicio</a>
      <a href="../../../../PLAN.md">Plan del proyecto</a>
      <a href="../../../../_docs/CONTRIBUIR.md">Cómo contribuir</a>
    </nav>
  </div>
</header>

<main>
  <div class="breadcrumb">
    <a href="../../../../index.html">Inicio</a><span class="sep">/</span>
    <a href="../../index.html">{carrera}</a><span class="sep">/</span>
    <a href="../index.html">{materia}</a><span class="sep">/</span>
    {titulo}
  </div>

  <article class="doc">
    <div class="doc-header">
      <h2>{titulo}</h2>
      <div class="badges">
        <span class="badge">{carrera}</span>
        <span class="badge">{materia}</span>
        <span class="badge">{nivel}</span>
        <span class="badge">{duracion}</span>
        <span class="badge">Ejercicio práctico</span>
      </div>
    </div>

    <h3 class="section">Objetivo de aprendizaje</h3>
    <p>[¿Qué debe poder hacer el alumno al terminar este ejercicio?]</p>

    <h3 class="section">Teoría</h3>
    <div class="ai-note">⚠️ Nota de transparencia: indicar aquí qué partes de esta sección se redactaron con apoyo de IA.</div>
    <p>[Desarrollo teórico.]</p>

    <h3 class="section">Ejercicio / caso práctico</h3>
    <p>[Planteamiento del ejercicio o caso.]</p>

    <h3 class="section">Solución / guía de solución</h3>
    <details class="solution">
      <summary>Mostrar solución</summary>
      <div class="inner">
        <p>[Desarrollo de la solución.]</p>
      </div>
    </details>

    <h3 class="section">Prompt sugerido para hacerlo con Claude o ChatGPT</h3>
    <div class="prompt-box">
      <span class="label">🤖 Prompt sugerido</span>[Prompt sugerido — reemplazar con el prompt real del ejercicio]</div>
    <div class="doc-suggestion">📎 <strong>Documentos a adjuntar:</strong> [indicar documento sugerido o "Ninguno"]</div>

    <h3 class="section">Recursos adicionales</h3>
    <ul>
      <li>[Plantillas, lecturas, datasets de apoyo]</li>
    </ul>

    <div class="doc-footer">
      Autor: {autor} · Actualizado: {fecha} · Asistencia de IA: [describir].
    </div>
  </article>
</main>

<footer class="site-footer">
  Prototipo local · <a href="../../../../PLAN.md">ver plan del proyecto</a>
</footer>

</body>
</html>
"""


def main():
    p = argparse.ArgumentParser(description="Crea el esqueleto de un ejercicio nuevo.")
    p.add_argument("--carrera")
    p.add_argument("--materia")
    p.add_argument("--titulo")
    p.add_argument("--tema", default="")
    p.add_argument("--nivel", default="Introductorio")
    p.add_argument("--duracion", default="40 min")
    p.add_argument("--autor", default="")
    p.add_argument("--fecha", default="")
    args = p.parse_args()

    import datetime
    fecha = args.fecha or datetime.date.today().isoformat()

    carrera_nombre = args.carrera or ask("Carrera (nombre completo)")
    materia_nombre = args.materia or ask("Materia (nombre completo)")
    titulo = args.titulo or ask("Título del ejercicio")
    tema = args.tema or ask("Tema específico", "")
    nivel = args.nivel or ask("Nivel", "Introductorio")
    duracion = args.duracion or ask("Duración estimada", "40 min")
    autor = args.autor or ask("Autor", "Iván de Luna-Aldape")

    carrera_slug = ensure_carrera(carrera_nombre)
    materia_slug = ensure_materia(carrera_slug, materia_nombre)
    ej_slug = slugify(titulo)

    ej_dir = CARRERAS_DIR / carrera_slug / materia_slug / ej_slug
    if ej_dir.exists():
        print(f"\n⚠ La carpeta ya existe: {ej_dir.relative_to(ROOT)} — no se sobrescribió nada.")
        return

    ej_dir.mkdir(parents=True)

    ctx = dict(titulo=titulo, carrera=carrera_nombre, materia=materia_nombre,
               tema=tema, nivel=nivel, duracion=duracion, autor=autor, fecha=fecha)

    (ej_dir / "README.md").write_text(README_TEMPLATE.format(**ctx), encoding="utf-8")
    (ej_dir / "metadata.yml").write_text(METADATA_TEMPLATE.format(**ctx), encoding="utf-8")
    (ej_dir / "index.html").write_text(INDEX_HTML_TEMPLATE.format(**ctx), encoding="utf-8")

    rel = ej_dir.relative_to(ROOT)
    print(f"\n✔ Ejercicio creado en: {rel}")
    print("\nSiguientes pasos:")
    print(f"  1. Edita {rel}/README.md (y opcionalmente index.html) con el contenido real.")
    print("  2. Corre:  python3 _scripts/generar_indices.py")
    print("  3. git add, commit y push.")


if __name__ == "__main__":
    main()
