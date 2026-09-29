# Cómo agregar un ejercicio nuevo

## Con el script (recomendado)

Desde la raíz del repositorio:

```
python3 _scripts/nuevo_ejercicio.py \
  --carrera "Administración de Empresas" \
  --materia "Gestión de Operaciones" \
  --titulo "Punto de Equilibrio" \
  --tema "Análisis costo-volumen-utilidad" \
  --nivel "Introductorio" \
  --duracion "40 min" \
  --autor "Tu nombre"
```

O simplemente corre `python3 _scripts/nuevo_ejercicio.py` sin argumentos y contesta las preguntas.

El script:
1. Crea la carrera y/o la materia si todavía no existen (reconoce las que ya existen por su nombre, aunque escribas mayúsculas/acentos distintos — no las duplica).
2. Crea la carpeta del ejercicio con `README.md`, `metadata.yml` e `index.html`, ya con la estructura y el formato estándar (incluida la sección de "Prompt sugerido para hacerlo con Claude o ChatGPT").

**Después de correrlo:**

1. Llena el contenido real en el `README.md` del ejercicio (teoría, caso práctico, solución, prompt sugerido) — y opcionalmente en su `index.html`, o pide ayuda para redactar ambos.
2. Corre `python3 _scripts/generar_indices.py` para regenerar automáticamente todos los índices (raíz, carrera, materia) — nunca los edites a mano, se sobrescriben en cada corrida.
3. `git add`, `git commit` y `git push`.

## A mano (alternativa)

1. Crea la carpeta de la carrera/materia si no existe, con un `_info.yml` (`nombre:`, `descripcion:`, `orden:`).
2. Crea la carpeta del ejercicio y copia la plantilla de [`_plantillas/plantilla-ejercicio.md`](../_plantillas/plantilla-ejercicio.md) a su `README.md`.
3. Agrega `metadata.yml` con los campos descritos en [`PLAN.md`](../PLAN.md#3-anatomía-de-un-ejercicio-la-unidad-mínima-del-repositorio).
4. Corre `python3 _scripts/generar_indices.py` para que los índices y el HTML de listados se regeneren solos.
5. Para el `index.html` del ejercicio en sí (el contenido, no los índices) sí hay que crearlo/editarlo a mano — usa cualquier `index.html` de ejercicio existente como referencia de la estructura.

## Sobre el uso de IA

Este repositorio permite y documenta el uso de IA para redactar o ampliar la parte teórica de los ejercicios. La única regla es la transparencia: cada ejercicio debe indicar, en su sección de teoría y en `metadata.yml` (campo `asistencia_ia`), qué tanto se apoyó en IA.
