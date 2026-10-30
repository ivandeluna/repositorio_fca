#!/usr/bin/env python3
"""
Migración única: fusiona metadata.yml en el encabezado YAML del README.md de
cada ejercicio y quita del cuerpo el título y las líneas **Carrera:** ... que
ya quedan en el encabezado. Después de correrlo, metadata.yml sobra.

    python3 _scripts/migrar_a_un_archivo.py          # convierte
    python3 _scripts/migrar_a_un_archivo.py --borrar # además borra metadata.yml
"""
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ejercicio_io import escribir_ejercicio, separar  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def limpiar_cuerpo(cuerpo: str) -> str:
    lineas = cuerpo.splitlines()
    i = 0
    while i < len(lineas) and (not lineas[i].strip() or lineas[i].startswith("# ")
                               or re.match(r"^\*\*(Carrera|Materia|Tema|Nivel|Duración estimada|Modalidad|Tipo|Autor):\*\*", lineas[i])):
        i += 1
    return "\n".join(lineas[i:]) + ("\n" if cuerpo.endswith("\n") else "")


def main():
    borrar = "--borrar" in sys.argv
    n = 0
    for meta_path in sorted(RAIZ.glob("carreras/*/*/*/metadata.yml")):
        d = meta_path.parent
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
        if meta.get("fecha") is not None:
            meta["fecha"] = str(meta["fecha"])
        previo, cuerpo = separar((d / "README.md").read_text(encoding="utf-8"))
        meta = {**meta, **previo}
        escribir_ejercicio(d, meta, limpiar_cuerpo(cuerpo))
        if borrar:
            meta_path.unlink()
        n += 1
        print("✔", d.relative_to(RAIZ))
    print(f"{n} ejercicios migrados.")


if __name__ == "__main__":
    main()
