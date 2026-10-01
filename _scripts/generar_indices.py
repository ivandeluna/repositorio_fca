#!/usr/bin/env python3
"""
Regenera los índices del repositorio (README.md + index.html) en los niveles
de raíz, carrera y materia, a partir de:
  - carreras/<carrera>/_info.yml
  - carreras/<carrera>/<materia>/_info.yml
  - carreras/<carrera>/<materia>/<ejercicio>/metadata.yml

NO toca el contenido de los ejercicios (README.md / index.html dentro de cada
carpeta de ejercicio) — esos se siguen redactando a mano / con ayuda de IA.

Uso:
    python3 _scripts/generar_indices.py
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML. Instálalo con:  pip3 install pyyaml --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
CARRERAS_DIR = ROOT / "carreras"


def read_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def slug_title(slug):
    return slug.replace("-", " ").title()


def collect():
    """Recorre carreras/*/*/*/metadata.yml y arma la estructura anidada."""
    carreras = []
    if not CARRERAS_DIR.is_dir():
        sys.exit(f"No existe {CARRERAS_DIR}")

    for carrera_dir in sorted(CARRERAS_DIR.iterdir()):
        if not carrera_dir.is_dir():
            continue
        info_path = carrera_dir / "_info.yml"
        info = read_yaml(info_path) if info_path.exists() else {}
        carrera = {
            "slug": carrera_dir.name,
            "nombre": info.get("nombre", slug_title(carrera_dir.name)),
            "descripcion": info.get("descripcion", ""),
            "orden": info.get("orden", 999),
            "materias": [],
        }

        for materia_dir in sorted(carrera_dir.iterdir()):
            if not materia_dir.is_dir() or materia_dir.name.startswith("_"):
                continue
            minfo_path = materia_dir / "_info.yml"
            minfo = read_yaml(minfo_path) if minfo_path.exists() else {}
            materia = {
                "slug": materia_dir.name,
                "nombre": minfo.get("nombre", slug_title(materia_dir.name)),
                "descripcion": minfo.get("descripcion", ""),
                "orden": minfo.get("orden", 999),
                "ejercicios": [],
            }

            for ej_dir in sorted(materia_dir.iterdir()):
                if not ej_dir.is_dir() or ej_dir.name.startswith("_"):
                    continue
                meta_path = ej_dir / "metadata.yml"
                if not meta_path.exists():
                    continue
                meta = read_yaml(meta_path)
                materia["ejercicios"].append({
                    "slug": ej_dir.name,
                    "titulo": meta.get("titulo", slug_title(ej_dir.name)),
                    "tema": meta.get("tema", ""),
                    "nivel": meta.get("nivel", ""),
                    "duracion_estimada": meta.get("duracion_estimada", ""),
                    "tipo": meta.get("tipo", ""),
                })

            materia["ejercicios"].sort(key=lambda e: e["titulo"])
            carrera["materias"].append(materia)

        carrera["materias"].sort(key=lambda m: (m["orden"], m["nombre"]))
        carreras.append(carrera)

    carreras.sort(key=lambda c: (c["orden"], c["nombre"]))
    return carreras


# ---------------------------------------------------------------------------
# Plantillas HTML compartidas
# ---------------------------------------------------------------------------

HTML_HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css_path}">
</head>
<body>

<header class="site-header">
  <div class="top">
    <div class="brand">
      <img src="{logo_path}" alt="Universidad Autónoma de Coahuila" class="brand-logo">
      <div class="brand-text">
        <span class="kicker">Universidad Autónoma de Coahuila · Facultad de Contaduría y Administración, Unidad Torreón</span>
        <h1><a href="{home_path}">Repositorio de Métodos y Ejercicios</a></h1>
      </div>
    </div>
    <nav class="top-nav">
      <a href="{home_path}">Inicio</a>
      <a href="{contrib_path}">Cómo contribuir</a>
    </nav>
  </div>
</header>

<main>
"""

HTML_FOOT = """</main>

<footer class="site-footer">
  Universidad Autónoma de Coahuila · Facultad de Contaduría y Administración, Unidad Torreón
</footer>

</body>
</html>
"""


def up(n):
    return "../" * n


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Nivel raíz
# ---------------------------------------------------------------------------

def gen_root(carreras):
    # README.md
    rows = []
    for c in carreras:
        materias_txt = ", ".join(m["nombre"] for m in c["materias"]) or "*(por agregar)*"
        rows.append(f"| [{c['nombre']}](./carreras/{c['slug']}/README.md) | {materias_txt} |")

    readme = f"""# Repositorio de Métodos y Ejercicios — FCA

Catálogo de métodos, dinámicas y ejercicios de clase usados por profesores de la Facultad de Contaduría y Administración (FCA), organizados por carrera y materia — inspirado en el formato de catálogo del [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/), pero en lugar de *datasets*, aquí se catalogan **formas de dar clase con y sin apoyo de IA**.

Ver el plan completo del proyecto en [`PLAN.md`](./PLAN.md).

## Carreras

| Carrera | Materias registradas |
|---|---|
{chr(10).join(rows)}

## ¿Cómo agregar un ejercicio nuevo?

Ver la guía en [`_docs/CONTRIBUIR.md`](./_docs/CONTRIBUIR.md) y usar la plantilla en [`_plantillas/plantilla-ejercicio.md`](./_plantillas/plantilla-ejercicio.md).

> Este README y sus páginas HTML se generan automáticamente con `_scripts/generar_indices.py` — no los edites a mano, edita los `_info.yml` / `metadata.yml` correspondientes y vuelve a correr el script.
"""
    write(ROOT / "README.md", readme)

    # index.html
    cards = []
    for c in carreras:
        n_mat = len(c["materias"])
        n_ej = sum(len(m["ejercicios"]) for m in c["materias"])
        if n_mat == 0:
            meta_html = '        <span class="badge soon">próximamente</span>\n'
        else:
            meta_html = (
                f'        <span class="badge count">{n_mat} materia{"s" if n_mat != 1 else ""}</span>\n'
                f'        <span class="badge count">{n_ej} ejercicio{"s" if n_ej != 1 else ""}</span>\n'
            )
        cards.append(
            f'    <a class="card" href="carreras/{c["slug"]}/index.html">\n'
            f'      <h3>{c["nombre"]}</h3>\n'
            f'      <p>{c["descripcion"]}</p>\n'
            f'      <div class="meta">\n{meta_html}      </div>\n'
            f'    </a>'
        )

    body = HTML_HEAD.format(
        title="Repositorio de Métodos y Ejercicios — FCA",
        css_path="assets/style.css",
        logo_path="assets/img/uadec-logo.png",
        home_path="index.html",
        plan_path="PLAN.md",
        contrib_path="_docs/CONTRIBUIR.md",
    )
    body += """  <div class="hero">
    <h2>Catálogo de métodos y ejercicios de clase</h2>
    <p class="lead">Inspirado en el <a href="https://archive.ics.uci.edu/" target="_blank" rel="noopener">UC Irvine Machine Learning Repository</a> — pero en lugar de catalogar datasets, aquí se catalogan formas de dar clase, con y sin apoyo de IA, organizadas por carrera y materia.</p>
  </div>

  <div class="search-box">
    <span class="icon">🔎</span>
    <input type="text" id="filter" placeholder="Buscar carrera..." onkeyup="filterCards()">
  </div>

  <div class="section-title">Carreras</div>
  <div class="card-grid" id="card-grid">
"""
    body += "\n".join(cards) + "\n  </div>\n"
    body += HTML_FOOT.format(plan_path="PLAN.md")
    body += """
<script>
function filterCards(){
  var q = document.getElementById('filter').value.toLowerCase();
  document.querySelectorAll('#card-grid .card').forEach(function(c){
    var text = c.innerText.toLowerCase();
    c.style.display = text.indexOf(q) !== -1 ? '' : 'none';
  });
}
</script>
"""
    write(ROOT / "index.html", body)


# ---------------------------------------------------------------------------
# Nivel carrera
# ---------------------------------------------------------------------------

def gen_carrera(c):
    base = CARRERAS_DIR / c["slug"]

    rows = [f"| [{m['nombre']}](./{m['slug']}/README.md) | {len(m['ejercicios'])} |" for m in c["materias"]]
    if not rows:
        readme = f"""# {c['nombre']}

Aún no hay materias registradas para esta carrera.

Para agregar la primera, usa la plantilla en [`_plantillas/plantilla-ejercicio.md`](../../_plantillas/plantilla-ejercicio.md) y sigue la estructura descrita en [`PLAN.md`](../../PLAN.md).

⬅ [Volver al catálogo general](../../README.md)
"""
    else:
        readme = f"""# {c['nombre']}

Materias con ejercicios/métodos registrados en este repositorio.

| Materia | Ejercicios |
|---|---|
{chr(10).join(rows)}

⬅ [Volver al catálogo general](../../README.md)
"""
    write(base / "README.md", readme)

    body = HTML_HEAD.format(
        title=f"{c['nombre']} — Repositorio FCA",
        css_path=up(2) + "assets/style.css",
        logo_path=up(2) + "assets/img/uadec-logo.png",
        home_path=up(2) + "index.html",
        plan_path=up(2) + "PLAN.md",
        contrib_path=up(2) + "_docs/CONTRIBUIR.md",
    )
    body += f"""  <div class="breadcrumb">
    <a href="{up(2)}index.html">Inicio</a><span class="sep">/</span>{c['nombre']}
  </div>

  <div class="hero">
    <h2>{c['nombre']}</h2>
    <p class="lead">Materias con métodos y ejercicios registrados para esta carrera.</p>
  </div>

"""
    if not c["materias"]:
        body += """  <div class="card-grid">
    <div class="card empty">
      <h3>Sin materias todavía</h3>
      <p>Usa la plantilla en <code>_plantillas/plantilla-ejercicio.md</code> para agregar la primera.</p>
    </div>
  </div>
"""
    else:
        body += '  <div class="section-title">Materias</div>\n  <div class="card-grid">\n'
        for m in c["materias"]:
            n_ej = len(m["ejercicios"])
            body += (
                f'    <a class="card" href="{m["slug"]}/index.html">\n'
                f'      <h3>{m["nombre"]}</h3>\n'
                f'      <p>{m["descripcion"]}</p>\n'
                f'      <div class="meta">\n'
                f'        <span class="badge count">{n_ej} ejercicio{"s" if n_ej != 1 else ""}</span>\n'
                f'      </div>\n'
                f'    </a>\n'
            )
        body += "  </div>\n"

    body += HTML_FOOT.format(plan_path=up(2) + "PLAN.md")
    write(base / "index.html", body)


# ---------------------------------------------------------------------------
# Nivel materia
# ---------------------------------------------------------------------------

def gen_materia(c, m):
    base = CARRERAS_DIR / c["slug"] / m["slug"]

    rows = [
        f"| [{e['titulo']}](./{e['slug']}/README.md) | {e['tema']} | {e['nivel']} |"
        for e in m["ejercicios"]
    ]
    readme = f"""# {m['nombre']}

Materia de la carrera de {c['nombre']}.

## Ejercicios / métodos registrados

| Ejercicio | Tema | Nivel |
|---|---|---|
{chr(10).join(rows) if rows else "| *(sin ejercicios todavía)* | | |"}

⬅ [Volver a {c['nombre']}](../README.md)
"""
    write(base / "README.md", readme)

    body = HTML_HEAD.format(
        title=f"{m['nombre']} — Repositorio FCA",
        css_path=up(3) + "assets/style.css",
        logo_path=up(3) + "assets/img/uadec-logo.png",
        home_path=up(3) + "index.html",
        plan_path=up(3) + "PLAN.md",
        contrib_path=up(3) + "_docs/CONTRIBUIR.md",
    )
    body += f"""  <div class="breadcrumb">
    <a href="{up(3)}index.html">Inicio</a><span class="sep">/</span>
    <a href="../index.html">{c['nombre']}</a><span class="sep">/</span>
    {m['nombre']}
  </div>

  <div class="hero">
    <h2>{m['nombre']}</h2>
    <p class="lead">Ejercicios y métodos registrados para esta materia.</p>
  </div>

  <div class="section-title">Ejercicios</div>
  <div class="card-grid">
"""
    for e in m["ejercicios"]:
        badges = "".join(f'<span class="badge">{b}</span>\n        ' for b in [e["nivel"], e["duracion_estimada"], e["tipo"]] if b)
        body += (
            f'    <a class="card" href="{e["slug"]}/index.html">\n'
            f'      <h3>{e["titulo"]}</h3>\n'
            f'      <p>{e["tema"]}</p>\n'
            f'      <div class="meta">\n        {badges}</div>\n'
            f'    </a>\n'
        )
    body += "  </div>\n"
    body += HTML_FOOT.format(plan_path=up(3) + "PLAN.md")
    write(base / "index.html", body)


def main():
    carreras = collect()
    gen_root(carreras)
    for c in carreras:
        gen_carrera(c)
        for m in c["materias"]:
            gen_materia(c, m)

    n_mat = sum(len(c["materias"]) for c in carreras)
    n_ej = sum(len(m["ejercicios"]) for c in carreras for m in c["materias"])
    print(f"Índices regenerados: {len(carreras)} carreras, {n_mat} materias, {n_ej} ejercicios.")


if __name__ == "__main__":
    main()
