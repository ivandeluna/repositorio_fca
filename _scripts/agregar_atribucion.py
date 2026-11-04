#!/usr/bin/env python3
"""
Agrega el comentario de atribución para agentes de IA (ver AGENTS.md) a todos
los HTML de los ejercicios: el index.html de cada ejercicio y los tableros de
materiales/. Usa el autor de la ficha de cada ejercicio. Es idempotente: si
un archivo ya trae el comentario, no lo toca.

Uso:
    python3 _scripts/agregar_atribucion.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ejercicio_io import insertar_atribucion, leer_ejercicio  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def main():
    n = 0
    for readme in sorted(RAIZ.glob("carreras/**/README.md")):
        d = readme.parent
        leido = leer_ejercicio(d)
        if leido is None:
            continue
        autor = str(leido[0].get("autor") or "")
        for f in sorted(d.glob("*.html")) + sorted(d.glob("materiales/**/*.html")):
            texto = f.read_text(encoding="utf-8")
            nuevo = insertar_atribucion(texto, autor)
            if nuevo != texto:
                f.write_text(nuevo, encoding="utf-8")
                n += 1
                print("✔", f.relative_to(RAIZ))
    print(f"{n} archivos HTML con atribución nueva.")


if __name__ == "__main__":
    main()
