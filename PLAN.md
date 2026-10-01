# Plan: Repositorio de Métodos y Ejercicios FCA

**Inspiración:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/) — pero en lugar de catalogar *datasets*, este repositorio cataloga **métodos y ejercicios de clase** que los profesores de la Facultad de Contaduría y Administración (FCA) usan para enseñar, organizados por carrera y materia.

**Objetivo:** crear un catálogo navegable, versionado y fácil de ampliar, donde cualquier profesor pueda encontrar (o subir) un ejercicio listo para usar en su curso — con la teoría necesaria, el planteamiento del ejercicio y, cuando aplique, apoyo de IA para resolverlo o explicarlo.

## 1. Alcance y decisiones ya tomadas

- **Formato del contenido:** Markdown plano. Cada ejercicio es un `README.md` con la teoría (redactada "a mano" y, donde se indique, con ayuda de IA) más el planteamiento del ejercicio.
- **Catálogo/navegación:** un `README.md` en cada nivel (raíz → carrera → materia → ejercicio) hace de índice, igual que las páginas de categoría de UC Irvine. Nada de generador de sitios por ahora — se puede añadir después (Quarto, Docusaurus, GitHub Pages) sin reestructurar el contenido, porque Markdown es la base común.
- **Ubicación:** el repositorio vive local en tu carpeta `FCA/Repositorio` por ahora. Cuando quieras compartirlo o versionarlo con colegas, se sube tal cual a GitHub (la estructura ya es compatible: README.md se renderiza automáticamente en cada carpeta).

## 2. Estructura de carpetas

```
Repositorio/
├── README.md                          ← catálogo raíz (las 3 carreras)
├── PLAN.md                            ← este documento
├── _plantillas/
│   └── plantilla-ejercicio.md         ← formato estándar para nuevos ejercicios
├── _docs/
│   └── CONTRIBUIR.md                  ← guía para que otros profesores agreguen ejercicios
└── carreras/
    ├── contador-publico/
    │   ├── README.md                  ← índice de materias de la carrera
    │   └── aplicar-administracion-finanzas/
    │       ├── README.md              ← índice de ejercicios de la materia
    │       ├── ciclo-conversion-efectivo/
    │       │   ├── README.md          ← teoría + ejercicio (el contenido real)
    │       │   └── metadata.yml       ← metadatos estructurados (para catalogar/filtrar después)
    │       ├── administracion-de-cuentas-por-cobrar/
    │       │   ├── README.md
    │       │   └── metadata.yml
    │       └── administracion-de-inventario/
    │           ├── README.md
    │           └── metadata.yml
    ├── comercio-exterior-aduanas/
    │   ├── README.md
    │   ├── manejar-finanzas-internacionales/
    │   │   ├── README.md
    │   │   ├── arbitraje-tipo-cambio-tasas-interes/
    │   │   │   ├── README.md
    │   │   │   └── metadata.yml
    │   │   └── amortizacion-de-prestamos/
    │   │       ├── README.md
    │   │       └── metadata.yml
    │   └── econometria/
    │       ├── README.md
    │       └── regresion-lineal-simple/
    │           ├── README.md
    │           └── metadata.yml
    ├── administracion-empresas/
    │   └── README.md
    └── materias-comunes/
        ├── README.md
        ├── _info.yml
        └── estadistica-basica/
            ├── README.md
            ├── _info.yml
            └── medidas-de-tendencia-central/
                ├── README.md
                └── metadata.yml
```

> **Nota sobre materias compartidas:** cuando una materia (como Estadística Básica) la cursan las tres carreras por igual, no se duplica dentro de cada una — vive una sola vez bajo la "carrera" especial `materias-comunes`, que aparece como una cuarta tarjeta más en el catálogo raíz. El generador de índices la trata igual que cualquier otra carrera, así que no requirió cambios al script.

Jerarquía: **Carrera → Materia → Ejercicio/Método**. Cada nivel es una carpeta con su propio `README.md` que actúa como índice de lo que contiene — el mismo patrón de "categoría → subcategoría → dataset" de UCI.

## 3. Anatomía de un ejercicio (la unidad mínima del repositorio)

Cada ejercicio vive en su propia carpeta y contiene:

1. **`README.md`** — el documento de contenido, con esta forma:
   - Encabezado con metadatos rápidos (materia, carrera, nivel, duración estimada)
   - **Objetivo de aprendizaje**
   - **Teoría** (la parte "a mano + IA": redactada por el profesor, pulida o ampliada con ayuda de IA cuando aplique — se marca explícitamente qué partes tuvieron asistencia de IA, por transparencia académica)
   - **Ejercicio / caso práctico**
   - **Solución o guía de solución** (opcional, se puede separar en `solucion.md` si se quiere ocultar a los alumnos)
   - **Prompt sugerido para hacerlo con Claude o ChatGPT** (un prompt listo para copiar/pegar que resuelva o explique el ejercicio, más una nota de qué documentos conviene adjuntar — p. ej. "se sugiere agregar el Estado de Resultados" — o "ninguno" si los datos caben en el prompt)
   - **Recursos adicionales** (lecturas, plantillas de Excel, datasets de apoyo)

2. **`metadata.yml`** — ficha estructurada, pensada para que en el futuro se pueda generar un índice automático o un buscador:
   ```yaml
   titulo: "Ciclo de Conversión de Efectivo"
   carrera: "Contador Público"
   materia: "Aplicar Administración de las Finanzas"
   tema: "Administración del capital de trabajo"
   nivel: "Intermedio"
   duracion_estimada: "50 min"
   tipo: "Ejercicio práctico"
   asistencia_ia: "Redacción de teoría revisada/ampliada con IA; ejercicio original del profesor"
   autor: "Iván de Luna-Aldape"
   fecha: "2026-09-10"
   tags: ["capital de trabajo", "liquidez", "finanzas corporativas"]
   ```

Esto es opcional de llenar al 100% desde el día uno, pero tenerlo desde el ejemplo piloto evita tener que "retro-etiquetar" decenas de ejercicios después.

## 4. Roadmap sugerido

1. **Fase 0 — Piloto (hoy):** estructura de carpetas + 1 ejercicio completo (Ciclo de Conversión de Efectivo) para validar el formato. ✅
2. **Fase 1 — Poblar Contador Público:** agregar 3–5 ejercicios más de "Aplicar Administración de las Finanzas" y abrir 1–2 materias adicionales de la misma carrera.
3. **Fase 2 — Cubrir las otras dos carreras:** Comercio Exterior y Aduanas ya tiene dos materias con ejercicio piloto ✅ (Manejar Finanzas Internacionales → Arbitraje con Tipo de Cambio y Diferencial de Tasas de Interés; Econometría → Regresión Lineal Simple). Administración de Empresas sigue pendiente.
4. **Fase 3 — Publicar en GitHub:** ✅ repositorio git inicializado localmente con el primer commit. Falta el paso final (crear el repo remoto en GitHub y hacer el primer `push`) — ver la sección 7 más abajo.
5. **Fase 4 — Automatizar los índices:** ✅ `_scripts/generar_indices.py` regenera automáticamente el `README.md` y `index.html` de raíz, carrera y materia a partir de los `_info.yml` y `metadata.yml` — ya no se editan a mano.

## 5. Convenciones de nombres

- Carpetas en minúsculas, sin acentos, con guiones: `ciclo-conversion-efectivo`, `aplicar-administracion-finanzas`.
- Un ejercicio = una carpeta. Si un ejercicio tiene archivos de apoyo (Excel, datos, imágenes), van dentro de esa misma carpeta.
- El texto visible (títulos, contenido) sí lleva acentos y formato normal en español.

## 6. Qué se construyó ya como prototipo

- Estructura completa de carpetas, con `README.md` de teoría + ejercicio y `metadata.yml` para:
  - Contador Público → Aplicar Administración de las Finanzas → **Ciclo de Conversión de Efectivo**
  - Contador Público → Aplicar Administración de las Finanzas → **Administración de Cuentas por Cobrar** (evaluación de una propuesta de descuento por pronto pago vs. costo de oportunidad de CxC)
  - Contador Público → Aplicar Administración de las Finanzas → **Administración de Inventario** (EOQ, punto de reorden con/sin inventario de seguridad, y su relación con JIT)
  - Comercio Exterior y Aduanas → Manejar Finanzas Internacionales → **Arbitraje con Tipo de Cambio y Diferencial de Tasas de Interés**
  - Comercio Exterior y Aduanas → Manejar Finanzas Internacionales → **Amortización de Préstamos** (sistema francés, cálculo de un mes específico y efecto de un pago anticipado a capital)
  - Comercio Exterior y Aduanas → Econometría → **Regresión Lineal Simple**
  - Materias Comunes → Estadística Básica → **Medidas de Tendencia Central** (el caso práctico y su solución los agregó la IA; el borrador original solo traía teoría y prompts)
- Un **prototipo navegable en HTML** (paleta azul/blanco de la FCA) que refleja la misma estructura de carpetas, con página de inicio, páginas de carrera, de materia y de ejercicio — incluyendo una sección de **"Prompt sugerido para hacerlo con Claude o ChatGPT"** en cada ejercicio, con el prompt listo para copiar y una nota de qué documentos conviene adjuntar (o si no se requiere ninguno).
- Índices de cada nivel y la plantilla para nuevos ejercicios, ya actualizada con la sección de prompt sugerido.

Revísalo directamente en tu carpeta `FCA/Repositorio` (abre `index.html` para la versión navegable).

## 7. Publicar en GitHub y flujo de trabajo hacia adelante

**Estado actual:** el repositorio ya es un repositorio git local (`git init` hecho, primer commit hecho, rama `main`). Falta únicamente conectarlo a GitHub:

1. Crea un repositorio vacío en GitHub (privado), **sin** inicializarlo con README/licencia (ya tenemos uno).
2. Desde una Terminal en tu Mac, dentro de la carpeta `FCA/Repositorio`:
   ```
   git remote add origin https://github.com/<tu-usuario>/<nombre-del-repo>.git
   git push -u origin main
   ```
3. La Terminal pedirá autenticarte con GitHub (usuario + un *personal access token*, o a través de `gh auth login` / GitHub Desktop si prefieres una interfaz gráfica).

**Flujo para agregar un ejercicio nuevo (carrera, materia o ejercicio) de aquí en adelante:**

1. `python3 _scripts/nuevo_ejercicio.py` (con argumentos o interactivo) — crea las carpetas y archivos con la estructura estándar, incluyendo carrera/materia nuevas si hace falta.
2. Editar el `README.md` (y opcionalmente el `index.html`) del ejercicio con el contenido real.
3. `python3 _scripts/generar_indices.py` — regenera automáticamente todos los índices (raíz, carrera, materia).
4. `git add -A && git commit -m "Agrega ejercicio: <nombre>" && git push`

Los únicos archivos que se editan a mano son los de contenido de cada ejercicio (`README.md` / `index.html` dentro de su carpeta) y los `_info.yml` de carrera/materia si se quiere ajustar su descripción u orden. Todo lo demás (índices) se regenera solo.
