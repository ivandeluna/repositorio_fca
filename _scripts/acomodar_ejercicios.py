#!/usr/bin/env python3
"""
Acomoda los ejercicios que un profesor guardó directo en la carpeta de una
carrera (sin materia), usando el campo «Materia» de su ficha.

Así un profesor puede abrir una materia nueva desde Pages CMS: entra a la
carrera, crea su ejercicio ahí y escribe el nombre de la materia. Este script
(que corre en GitHub Actions antes de regenerar los índices):

  1. Busca la materia entre las existentes de esa carrera, sin importar
     acentos ni mayúsculas ("matematicas basicas" = "Matemáticas Básicas").
  2. Si no existe, crea la carpeta de la materia con su _info.yml.
  3. Mueve el ejercicio (con sus materiales) dentro de la materia.

Si el ejercicio no trae materia, se deja donde está; generar_indices.py lo
reporta como aviso y el sitio no lo publica hasta que se acomode.

Uso:
    python3 _scripts/acomodar_ejercicios.py
"""
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ejercicio_io import ORDEN_CAMPOS, es_ejercicio, separar  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CARRERAS = RAIZ / "carreras"


def slugify(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", texto.lower().strip()).strip("-")


def leer_yaml(p: Path) -> dict:
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}) if p.exists() else {}


def limpiar_nombre(nombre: str) -> str:
    """Quita espacios sobrantes y, si viene todo en minúsculas, lo capitaliza."""
    nombre = " ".join(str(nombre).split())
    if nombre == nombre.lower():
        nombre = nombre[:1].upper() + nombre[1:]
    return nombre


def buscar_materia(dir_carrera: Path, nombre: str):
    """Carpeta de una materia existente que coincida con `nombre`, o None."""
    objetivo = slugify(nombre)
    for d in sorted(dir_carrera.iterdir()):
        if not d.is_dir() or d.name.startswith("_") or es_ejercicio(d):
            continue
        nombre_existente = leer_yaml(d / "_info.yml").get("nombre", d.name)
        if objetivo in (slugify(nombre_existente), slugify(d.name)):
            return d
    return None


def crear_materia(dir_carrera: Path, nombre: str) -> Path:
    slug = slugify(nombre)
    destino = dir_carrera / slug
    if destino.exists():
        # la carpeta existe pero es un ejercicio (p. ej. con el mismo título
        # que la materia); se usa un nombre distinto para la materia
        destino = dir_carrera / f"{slug}-materia"
    destino.mkdir()
    materias = [d for d in dir_carrera.iterdir()
                if d.is_dir() and not d.name.startswith("_") and not es_ejercicio(d)]
    datos = {"nombre": nombre, "descripcion": "", "orden": len(materias)}
    (destino / "_info.yml").write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return destino


def actualizar_ficha(readme: Path, carrera: str, materia: str):
    meta, cuerpo = separar(readme.read_text(encoding="utf-8"))
    meta["carrera"], meta["materia"] = carrera, materia
    ordenado = {k: meta[k] for k in ORDEN_CAMPOS if k in meta}
    ordenado.update({k: v for k, v in meta.items() if k not in ordenado})
    readme.write_text("---\n" + yaml.safe_dump(ordenado, allow_unicode=True, sort_keys=False, width=80)
                      + "---\n" + cuerpo.lstrip("\n"), encoding="utf-8")


def main():
    movidos, sin_materia = [], []
    for dir_carrera in sorted(p for p in CARRERAS.iterdir() if p.is_dir() and not p.name.startswith("_")):
        if es_ejercicio(dir_carrera):
            continue  # un ejercicio guardado fuera de toda carrera: no se adivina
        nombre_carrera = leer_yaml(dir_carrera / "_info.yml").get("nombre", dir_carrera.name)
        for dir_ej in sorted(p for p in dir_carrera.iterdir() if p.is_dir()):
            if dir_ej.name.startswith("_") or not es_ejercicio(dir_ej):
                continue
            meta, _ = separar((dir_ej / "README.md").read_text(encoding="utf-8"))
            materia = limpiar_nombre(meta.get("materia") or "")
            if not materia:
                sin_materia.append(dir_ej.relative_to(RAIZ))
                continue

            # se aparta el ejercicio primero: su carpeta podría llamarse igual que la materia
            temporal = dir_carrera / f"_acomodando-{dir_ej.name}"
            dir_ej.rename(temporal)
            dir_materia = buscar_materia(dir_carrera, materia)
            nueva = dir_materia is None
            if nueva:
                dir_materia = crear_materia(dir_carrera, materia)
            nombre_materia = leer_yaml(dir_materia / "_info.yml").get("nombre", materia)

            destino = dir_materia / dir_ej.name
            n = 2
            while destino.exists():
                destino = dir_materia / f"{dir_ej.name}-{n}"
                n += 1
            shutil.move(str(temporal), str(destino))
            # índices viejos que el generador haya dejado dentro de la carpeta
            viejo = destino / "index.html"
            if viejo.exists() and "Materia de la carrera" in viejo.read_text(encoding="utf-8", errors="ignore"):
                viejo.unlink()
            actualizar_ficha(destino / "README.md", nombre_carrera, nombre_materia)
            movidos.append((destino.relative_to(RAIZ), nombre_materia, nueva))

    for ruta, materia, nueva in movidos:
        estado = "materia nueva" if nueva else "materia existente"
        print(f"Acomodado: {ruta}  ({estado}: {materia})")
        print(f"::notice file={ruta}/README.md::Ejercicio acomodado en {estado} «{materia}».")
    for ruta in sin_materia:
        print(f"Sin materia: {ruta} (se deja donde está; falta escribir la materia en su ficha)")
    if not movidos and not sin_materia:
        print("No hay ejercicios por acomodar.")


if __name__ == "__main__":
    main()
