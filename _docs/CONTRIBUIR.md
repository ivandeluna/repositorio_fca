# Cómo agregar un ejercicio nuevo

## Desde el navegador, con Pages CMS (para profesores)

No necesitas instalar nada ni saber Git.

1. Abre la invitación que te llegó por correo y entra a [app.pagescms.org](https://app.pagescms.org).
2. Elige el repositorio **repositorio_fca** y la sección **Ejercicios**. Verás las carreras y materias como carpetas.
3. Entra a la carpeta de la materia y crea un ejercicio nuevo, o abre uno existente para editarlo.
4. Llena la ficha (título, tema, nivel, duración, autor, etiquetas, uso de IA) y escribe el contenido en el campo **Contenido**. Usa los mismos encabezados de siempre: `## Objetivo de aprendizaje`, `## Teoría`, `## Ejercicio / caso práctico`, `## Solución / guía de solución`, `## Prompt sugerido para hacerlo con Claude o ChatGPT`, `## Recursos adicionales`.
5. Sube tus archivos de apoyo (Excel, CSV, PDF) desde **Materiales**, dentro de la carpeta `materiales/` de tu ejercicio.
6. Guarda. En unos minutos el ejercicio aparece en el sitio. Queda marcado como «Pendiente de revisión docente» hasta que el coordinador lo revise.

La carrera y la materia se toman de la carpeta donde guardas el ejercicio.

### Si tu materia todavía no existe

1. Entra a la carpeta de la **carrera** (no a una materia) y crea ahí tu ejercicio.
2. En el campo **Materia** de la ficha escribe el nombre completo de la materia, con acentos y mayúsculas como quieras que aparezca (por ejemplo, «Matemáticas Básicas»).
3. Guarda. En unos minutos el sistema crea la materia, mueve tu ejercicio dentro de ella y lo publica. Si ya existía una materia con ese nombre (aunque la escribas sin acentos o en minúsculas), lo pone en esa en lugar de duplicarla.

Después de guardar, tu ejercicio aparecerá en Pages CMS dentro de la carpeta de la materia; si quieres seguir editándolo, ábrelo desde ahí. Si la materia necesita una descripción, pídesela al coordinador.

> **Importante:** crea el ejercicio *dentro de la carpeta de su materia*, (Carrera → Materia → tu ejercicio), o en la carpeta de la carrera solo si vas a abrir una materia nueva. No edites los archivos que ya aparecen con el nombre de una carrera o materia: son índices que se regeneran solos. Si guardas un ejercicio directo en la carpeta de una carrera *sin* escribir la materia en su ficha, no se publica y aparece un aviso en GitHub Actions hasta que la escribas.

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
2. Crea la carpeta del ejercicio con `README.md` (con su ficha en el encabezado YAML) e `index.html`, ya con la estructura y el formato estándar (incluida la sección de "Prompt sugerido para hacerlo con Claude o ChatGPT").

**Después de correrlo:**

1. Llena el contenido real en el `README.md` del ejercicio (teoría, caso práctico, solución, prompt sugerido) — y opcionalmente en su `index.html`, o pide ayuda para redactar ambos.
2. Corre `python3 _scripts/generar_indices.py` para regenerar automáticamente todos los índices (raíz, carrera, materia) — nunca los edites a mano, se sobrescriben en cada corrida.
3. `git add`, `git commit` y `git push`.

## A mano (alternativa)

1. Crea la carpeta de la carrera/materia si no existe, con un `_info.yml` (`nombre:`, `descripcion:`, `orden:`).
2. Crea la carpeta del ejercicio y copia la plantilla de [`_plantillas/plantilla-ejercicio.md`](../_plantillas/plantilla-ejercicio.md) a su `README.md`.
3. Llena la ficha en el encabezado YAML del `README.md` (entre las dos líneas `---`), con los campos descritos en [`PLAN.md`](../PLAN.md#3-anatomía-de-un-ejercicio-la-unidad-mínima-del-repositorio).
4. Corre `python3 _scripts/generar_indices.py` para que los índices y el HTML de listados se regeneren solos.
5. Para el `index.html` del ejercicio en sí (el contenido, no los índices) sí hay que crearlo/editarlo a mano — usa cualquier `index.html` de ejercicio existente como referencia de la estructura.

## Ejercicios con materiales de clase (opcional)

Un ejercicio puede traer, además de `README.md` e `index.html`:

```
<ejercicio>/
├── GUIA-DOCENTE.md        ← guía del profesor: preparación, cronograma, frases, qué hacer sin IA
└── materiales/
    ├── 01-caso-alumno.md  ← caso para repartir, sin solución
    ├── 02-hoja-de-trabajo.md
    ├── 03-prompts.md      ← los prompts, listos para copiar
    ├── 04-rubrica.md
    ├── datos.csv
    └── tablero-*.html     ← tablero de referencia autocontenido
```

En ese caso, el `README.md` sigue siendo el documento principal (con la solución en un bloque `<details markdown="1">` y los prompts escritos en la sección «Prompt sugerido para hacerlo con Claude o ChatGPT») y enlaza a esos archivos en una sección «Cómo usar este ejercicio en clase». Ver como ejemplo los ejercicios de Administración Estratégica, Ventas, Compras y Recursos Humanos.

Para generar el `index.html` del ejercicio a partir de su `README.md`:

```
python3 _scripts/readme_a_html.py carreras/<carrera>/<materia>/<ejercicio>/
```

## Sobre el uso de IA

Este repositorio permite y documenta el uso de IA para redactar o ampliar la parte teórica de los ejercicios. La única regla es la transparencia: cada ejercicio debe indicar, en su sección de teoría y en el campo `asistencia_ia` de su ficha, qué tanto se apoyó en IA.
