"""
Lectura y escritura de ejercicios del Repositorio FCA.

Cada ejercicio es un solo archivo: carreras/<carrera>/<materia>/<ejercicio>/README.md
con sus metadatos en un encabezado YAML (front matter) entre dos líneas `---`:

    ---
    titulo: "Ciclo de Conversión de Efectivo"
    nivel: "Intermedio"
    ...
    ---

    ## Objetivo de aprendizaje
    ...

Este es el formato que edita Pages CMS (ver .pages.yml). Si un ejercicio
antiguo todavía trae metadata.yml, se lee como respaldo.
"""
import re
from pathlib import Path

import yaml

# Orden de los campos al escribir el encabezado (los que no estén aquí van al final)
ORDEN_CAMPOS = [
    "titulo", "carrera", "materia", "tema", "nivel", "duracion_estimada", "tipo",
    "modalidad", "entregable_alumno", "autor", "fecha", "tags", "asistencia_ia",
    "revisado_por_docente",
]

_FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)


def separar(texto: str):
    """Devuelve (metadatos, cuerpo) de un Markdown con encabezado YAML."""
    m = _FM.match(texto)
    if not m:
        return {}, texto
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, texto[m.end():]


def leer_ejercicio(dir_ej: Path):
    """Metadatos y cuerpo de un ejercicio. None si la carpeta no es un ejercicio."""
    readme = dir_ej / "README.md"
    if not readme.exists():
        return None
    meta, cuerpo = separar(readme.read_text(encoding="utf-8"))
    viejo = dir_ej / "metadata.yml"
    if not meta and viejo.exists():
        meta = yaml.safe_load(viejo.read_text(encoding="utf-8")) or {}
    if not meta.get("titulo") or meta.get("indice"):
        return None  # sin ficha, o es el índice de una carrera/materia
    if meta.get("fecha") is not None:
        meta["fecha"] = str(meta["fecha"])
    return meta, cuerpo


def es_ejercicio(dir_ej: Path) -> bool:
    return dir_ej.is_dir() and not dir_ej.name.startswith("_") and leer_ejercicio(dir_ej) is not None


def encabezado(meta: dict) -> str:
    ordenado = {k: meta[k] for k in ORDEN_CAMPOS if k in meta}
    ordenado.update({k: v for k, v in meta.items() if k not in ordenado})
    y = yaml.safe_dump(ordenado, allow_unicode=True, sort_keys=False, width=1000,
                       default_flow_style=None)
    return f"---\n{y}---\n\n"


def escribir_ejercicio(dir_ej: Path, meta: dict, cuerpo: str):
    (dir_ej / "README.md").write_text(encabezado(meta) + cuerpo.lstrip("\n"), encoding="utf-8")
