# El margen cae y nadie sabe por qué

**Carrera:** Administración de Empresas
**Materia:** Administración Estratégica
**Tema:** Balanced Scorecard, indicadores de resultado e inductores de actuación
**Nivel:** Intermedio
**Duración estimada:** 50 min

> ### 🎯 El gancho
> **Las ventas crecieron 11.2 % y el margen operativo cayó de 11.4 % a 9.8 %.** La dirección reforzó cobranza, negoció el precio de la lámina y recortó capacitación. Nada funcionó, porque el problema nace tres eslabones antes de donde lo estaban buscando.
>
> Nueve de cada diez equipos van a empezar por la cartera. El asistente de IA también.

## Cómo usar este ejercicio en clase

La guía para el profesor —preparación, cronograma minuto a minuto, frases sugeridas y qué hacer si se acorta el tiempo o no hay IA en el salón— está en [`GUIA-DOCENTE.md`](GUIA-DOCENTE.md). Materiales listos para usar en clase:

| Archivo | Qué es | Uso |
|---|---|---|
| [`GUIA-DOCENTE.md`](GUIA-DOCENTE.md) | Guía completa del profesor, con la solución | **Solo el profesor** |
| [`materiales/01-caso-alumno.md`](materiales/01-caso-alumno.md) | Caso para el alumno, sin solución | Se imprime y se reparte |
| [`materiales/02-hoja-de-trabajo.md`](materiales/02-hoja-de-trabajo.md) | Hoja de trabajo con las tablas por llenar | Se imprime, una por equipo |
| [`materiales/03-prompts.md`](materiales/03-prompts.md) | Prompts listos para copiar y pegar | Se comparte en digital |
| [`materiales/04-rubrica.md`](materiales/04-rubrica.md) | Rúbrica de evaluación | Se comparte con los alumnos al inicio |
| [`materiales/datos.csv`](materiales/datos.csv) | Datos del caso, para pegar en la IA o abrir en Excel | Se comparte en digital |
| [`materiales/tablero-bsc.html`](materiales/tablero-bsc.html) | Tablero de referencia ya funcionando (HTML) | Profesor, para la plenaria |

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá distinguir un indicador de resultado de un inductor de actuación dentro de un Balanced Scorecard; trazar la cadena causa-efecto que conecta las cuatro perspectivas hasta un deterioro financiero; verificar críticamente si el asistente de IA ubicó el origen en la perspectiva donde solo se manifiesta el síntoma; y proponer una acción correctiva sobre la causa, con su costo comparado contra el daño que evita.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; construcción del tablero, cadena causal y guía de solución con apoyo de IA. Pendiente de revisión docente.

### Las cuatro perspectivas y su orden

El Balanced Scorecard organiza los indicadores en cuatro perspectivas que **no están al mismo nivel**: se encadenan.

$$\text{Aprendizaje y crecimiento} \rightarrow \text{Procesos internos} \rightarrow \text{Cliente} \rightarrow \text{Financiera}$$

La perspectiva financiera es la **última** de la cadena. Todo lo que aparece ahí es consecuencia de algo que ocurrió antes, en alguna de las otras tres. Por eso un estado financiero siempre llega tarde: informa de un daño que se produjo meses atrás.

### Indicador de resultado contra inductor de actuación

- Un **indicador de resultado** mide qué pasó. Llega tarde y no se puede accionar directamente: margen, rentabilidad, días de cartera, participación de mercado.
- Un **inductor de actuación** mide algo que, si cambia hoy, modifica el resultado mañana: horas de capacitación, número de preparaciones, costo de no calidad, rotación de personal.

El error clásico de gestión es **actuar sobre el indicador de resultado**. Reforzar cobranza cuando los días de cartera suben es el ejemplo perfecto: si el cliente paga tarde porque le entregaron tarde, meter dos cobradores no cambia nada.

### Cómo se lee un tablero

No se lee indicador por indicador. Se lee buscando **si los que están en rojo forman una cadena**. Cuatro indicadores en rojo repartidos al azar son cuatro problemas; cuatro indicadores en rojo encadenados son **un solo problema** visto en cuatro momentos distintos.

## Ejercicio / caso práctico

**Industrias del Nazas, S.A. de C.V.**, metalmecánica de Torreón, 340 empleados, ventas de $218,000,000. Implantó un Balanced Scorecard hace un año.

Las ventas crecieron 11.2 %, por encima de la meta de 8 %. El margen operativo cayó de 11.4 % a 9.8 % en seis meses. El director general no entiende por qué.

**Lo que la dirección ya intentó:**

- Reforzar cobranza con dos personas. Los días de cartera siguieron subiendo.
- Negociar precio con los proveedores de lámina. Se logró 3 %, sin efecto visible.
- Congelar contrataciones y **recortar a la mitad el presupuesto de capacitación**.

### Tablero al cierre del semestre

| Perspectiva | Indicador | Meta | Real | Estado |
|-------------|-----------|------|------|--------|
| **Financiera** | Margen operativo | 12.0 % | 9.8 % | 🔴 |
| | Rendimiento sobre capital | 18.0 % | 16.4 % | 🟡 |
| | Días de cartera | 45 d | 62 d | 🔴 |
| | Crecimiento en ventas | 8.0 % | 11.2 % | 🟢 |
| **Cliente** | Índice de satisfacción | 90 pts | 87 pts | 🟡 |
| | Retención de clientes | 92.0 % | 94.1 % | 🟢 |
| | Entregas completas y a tiempo | 95.0 % | 88.6 % | 🔴 |
| | Participación de mercado | 14.0 % | 13.2 % | 🟡 |
| **Procesos internos** | Ciclo de pedido | 5.0 d | 7.4 d | 🔴 |
| | Merma de producción | 2.0 % | 2.6 % | 🟡 |
| | Rotación de inventario | 8.0 x | 6.9 x | 🟡 |
| | Costo de no calidad | 1.5 % | 2.9 % | 🔴 |
| **Aprendizaje** | Horas de capacitación por empleado | 24 h | 17 h | 🔴 |
| | Rotación de personal | 12.0 % | 15.8 % | 🟡 |
| | Puestos clave cubiertos | 90.0 % | 92.0 % | 🟢 |
| | Índice de clima laboral | 80 pts | 78 pts | 🟡 |

### Datos complementarios del periodo

| Concepto | Hace 6 meses | Actual |
|----------|--------------|--------|
| Ventas anualizadas | $196,000,000 | $218,000,000 |
| Utilidad de operación | $22,344,000 | $21,364,000 |
| Reprocesos y garantías | $3,920,000 | $6,322,000 |
| Fletes urgentes por retraso | $840,000 | $2,180,000 |
| Presupuesto de capacitación | $1,600,000 | $800,000 |
| Personal con menos de 1 año de antigüedad | 18 % | 31 % |

**Se pide (cinco pasos):**

---

### Paso 1 · Diagnosticar con la IA · 10 min
**Entregable:** la respuesta de la IA, copiada.

Usa el **prompt 1**. Pégale el tablero completo pero **no los datos complementarios**. Pídele que explique por qué cae el margen y que proponga dos acciones correctivas.

---

### Paso 2 · Clasificar los indicadores · 5 min
**Entregable:** una tabla de cinco renglones.

Toma estos **cinco indicadores en rojo** y clasifícalos:

| Indicador en rojo | ¿Resultado o inductor? | ¿Por qué? |
|---|---|---|
| Margen operativo | | |
| Días de cartera | | |
| Entregas completas y a tiempo | | |
| Costo de no calidad | | |
| Horas de capacitación | | |

**Pregunta:** si solo uno de estos se puede accionar hoy, ¿cuál es?

---

### Paso 3 · Trazar la cadena y confrontar · 10 min
**Entregable:** la cadena de cuatro eslabones, dibujada.

El profesor entrega ahora los **datos complementarios**. Usa el **prompt 2** para devolvérselos a la IA.

Dibuja la cadena causa-efecto con flechas, empezando **en la perspectiva donde se origina**:

```
[            ] → [            ] → [            ] → [            ]
```

Y cuantifícala: suma el aumento de reprocesos y el de fletes urgentes. Compáralo contra la caída de la utilidad de operación.

**Responde por escrito:** ¿en qué perspectiva empezó el diagnóstico de la IA? ¿Por qué ahí?

---

### Paso 4 · Construir el tablero · 15 min
**Entregable:** un archivo HTML que funcione.

Usa el **prompt 3** para generar un tablero interactivo con las cuatro perspectivas, sus semáforos y la cadena causal resaltada. Debe permitir **simular**:

1. Restituir el presupuesto de capacitación a $1,600,000. ¿Qué indicadores se mueven y en qué orden temporal?
2. Contratar dos cobradores más. ¿Qué se mueve?
3. ¿Cuál de las dos acciones cambia el margen en doce meses?

> Referencia en [`materiales/tablero-bsc.html`](materiales/tablero-bsc.html).

---

### Paso 5 · Decidir y presentar · 10 min
**Entregable:** 6–8 líneas.

Propón una acción sobre la **causa** y otra sobre el **síntoma**. Para cada una: costo, tiempo hasta ver efecto, y qué indicador del tablero avisaría si está funcionando.

**Plenaria.** Pregunta de cierre: **la dirección recortó capacitación para proteger el margen. ¿Qué efecto tuvo esa decisión sobre el margen?**

---

## Solución / guía de solución

<details markdown="1">
<summary><strong>Mostrar guía para el profesor</strong></summary>

> ⚠️ **Nota de transparencia:** esta guía de solución se redactó con apoyo de IA al integrar el ejercicio al repositorio; las cifras se verificaron con código contra los datos del caso. Pendiente de revisión docente.

### Paso 2 · Resultado o inductor

| Indicador en rojo | Perspectiva | Clasificación | Por qué |
|---|---|---|---|
| Margen operativo | Financiera | **Resultado** | Es el último eslabón: registra un daño que ya ocurrió y no se puede mover directamente. |
| Días de cartera | Financiera | **Resultado** | El cliente paga tarde porque recibió tarde o incompleto. Por eso los dos cobradores no cambiaron nada. |
| Entregas completas y a tiempo | Cliente | **Resultado** de procesos (e inductor de la cartera) | Depende del ciclo de pedido y de los reprocesos; no se corrige por decreto. |
| Costo de no calidad | Procesos internos | **Inductor** | Mide reprocesos y garantías; se reduce actuando sobre cómo se trabaja. |
| Horas de capacitación por empleado | Aprendizaje | **Inductor** | Es una decisión presupuestal de la dirección. |

**El único que se puede accionar hoy:** horas de capacitación. Las demás cifras se mueven como consecuencia.

> Nota: el tablero tiene un sexto indicador en rojo, **ciclo de pedido** (7.4 d contra 5.0 d), que pertenece al mismo eslabón de procesos internos. Si algún equipo lo agrega a la tabla, es un acierto.

### Paso 3 · La cadena causa-efecto

| Aprendizaje → | Procesos internos → | Cliente → | Financiera |
|---|---|---|---|
| Capacitación: 24 → 17 h por empleado | Costo de no calidad: 2.9 % (meta 1.5 %) | Entregas completas y a tiempo: 88.6 % | Días de cartera: 62 d |
| Personal con menos de 1 año: 18 % → 31 % | Ciclo de pedido: 7.4 d (meta 5.0 d) | Satisfacción: 87 pts | Margen operativo: 9.8 % |
| Rotación de personal: 15.8 % | Merma: 2.6 % | | |

Personal con menos experiencia y menos capacitación produce más reprocesos y garantías; los reprocesos alargan el ciclo de pedido y obligan a fletes urgentes; las entregas llegan tarde o incompletas; el cliente paga tarde y el sobrecosto se come el margen.

**Cuantificación:**

| Concepto | Hace 6 meses | Actual | Aumento |
|---|---:|---:|---:|
| Reprocesos y garantías | $3,920,000 | $6,322,000 | $2,402,000 |
| Fletes urgentes por retraso | $840,000 | $2,180,000 | $1,340,000 |
| **Sobrecosto total** | | | **$3,742,000** |
| Utilidad de operación | $22,344,000 | $21,364,000 | −$980,000 |

- El sobrecosto ($3,742,000) es **3.8 veces** la caída visible de la utilidad ($980,000). El crecimiento de las ventas escondió la mayor parte del daño.
- Si el margen se hubiera sostenido en 11.4 %, con ventas de $218,000,000 la utilidad sería de $24,852,000: **$3,488,000 más** que la real, una cifra del mismo orden que el sobrecosto.
- Los reprocesos y garantías actuales ($6,322,000) equivalen al 2.9 % de las ventas: es exactamente el costo de no calidad del tablero. Hace seis meses eran 2.0 %.
- El recorte de capacitación ahorró **$800,000**; el sobrecosto que coincide con él es **4.7 veces** mayor.

**¿Por qué la IA empieza en la perspectiva financiera?** Porque es donde está el síntoma que se le pide explicar («por qué cae el margen») y porque, sin los datos complementarios, los indicadores aparecen como una lista y no como una cadena. Lo esperable es que proponga cobranza, crédito o precios.

### Paso 4 · Simulación (proyección, no dato)

| Acción | Qué se mueve y cuándo | ¿Cambia el margen en 12 meses? |
|---|---|---|
| Restituir capacitación a $1,600,000 | 3 meses: horas de capacitación. 6 meses: costo de no calidad, merma y ciclo de pedido. 12 meses: entregas a tiempo, días de cartera y margen. | **Sí**, si se confirma la cadena. |
| Contratar dos cobradores más | Días de cartera, marginalmente; agrega costo fijo. | **No**: ataca el síntoma y además cuesta. |

### Paso 5 · Respuesta a la pregunta de cierre

La dirección recortó capacitación para proteger el margen y obtuvo el efecto contrario: ahorró $800,000 y el margen siguió cayendo, porque el recorte alimentó el eslabón donde se origina el problema. Una acción razonable sobre la causa es restituir el presupuesto con prioridad en el 31 % de personal con menos de un año (inducción, certificación por puesto, acompañamiento de un operario experimentado), con el costo de no calidad como indicador de alerta temprana. Sobre el síntoma, se acepta una medida temporal para contener fletes urgentes o cartera, siempre que se declare como tal.

**Matiz que conviene premiar:** el caso está construido para que la cadena sea coherente, pero coincidencia en el tiempo no es demostración. Un equipo que diga qué dato adicional confirmaría la causalidad (por ejemplo, reprocesos por antigüedad del operario) merece la mejor nota en el criterio de justificación.

### Errores frecuentes del asistente de IA

| Lo que suele hacer la IA | Por qué está mal | Qué debe responder el alumno |
|---|---|---|
| Empieza por días de cartera y recomienda endurecer cobranza, factoraje o políticas de crédito | Actúa sobre un indicador de resultado; la dirección ya lo intentó y no funcionó | Señalar que la cartera es el último síntoma de la cadena |
| Atribuye la caída a materia prima, mezcla de productos o precios | No hay datos de eso en el tablero; es un supuesto | Marcar la cifra o la causa como no sustentada |
| Lee los 16 indicadores como una lista | No busca si los rojos se encadenan | Trazar la cadena de aprendizaje a financiera |
| Avala el recorte de capacitación como «medida de austeridad» | Trata un inductor como gasto prescindible | Mostrar que el ahorro es menor que el sobrecosto que coincide con él |
| Con los datos complementarios, suma los reprocesos totales ($6.3 M) en lugar del aumento | Confunde nivel con variación | Usar solo el aumento: $2,402,000 + $1,340,000 |
| Afirma la causalidad sin matices | Dos series que se mueven juntas no prueban causa | Declarar el supuesto y qué dato lo confirmaría |

### Rúbrica

Ver [`materiales/04-rubrica.md`](materiales/04-rubrica.md).

</details>

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copiar y pegar en Claude o ChatGPT, **en orden**. No adelantes el prompt 2.

### Prompt 1 — primera respuesta (paso 1)

```
Actúa como consultor de gestión.

Industrias del Nazas, metalmecánica de Torreón, 340 empleados,
ventas de $218,000,000. Las ventas crecieron 11.2 % y el margen
operativo cayó de 11.4 % a 9.8 % en seis meses.

La dirección ya intentó: reforzar cobranza con dos personas,
negociar el precio de la lámina (logró 3 %) y recortar a la mitad
el presupuesto de capacitación.

[pega aquí el contenido de datos.csv: el tablero de 16 indicadores]

1. Identifica los indicadores fuera de meta.
2. Explica por qué cae el margen operativo aunque las ventas crezcan.
3. Propón dos acciones correctivas.

Usa únicamente los datos del tablero. Si necesitas información que no
te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

```
Te entrego datos complementarios que antes no tenías:

Concepto | Hace 6 meses | Actual
Ventas anualizadas | $196,000,000 | $218,000,000
Utilidad de operación | $22,344,000 | $21,364,000
Reprocesos y garantías | $3,920,000 | $6,322,000
Fletes urgentes por retraso | $840,000 | $2,180,000
Presupuesto de capacitación | $1,600,000 | $800,000
Personal con menos de 1 año | 18 % | 31 %

1. ¿En qué perspectiva del Balanced Scorecard empezó tu diagnóstico
   anterior? ¿Por qué ahí?
2. Traza la cadena causa-efecto completa, de cuatro eslabones,
   empezando por la perspectiva donde se ORIGINA el problema.
3. Clasifica cada indicador en rojo como indicador de resultado o
   inductor de actuación, y justifica.
4. Cuantifica: suma el aumento de reprocesos y el de fletes urgentes,
   y compáralo contra la caída de la utilidad de operación.

Después responde: la dirección recortó capacitación para proteger el
margen. ¿Qué efecto tuvo esa decisión sobre el margen?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos:
[pega aquí el contenido de datos.csv]
Caída de la utilidad de operación: de $22,344,000 a $21,364,000.

El tablero debe tener:
1. Las cuatro perspectivas con sus 16 indicadores, meta contra real,
   y semáforo verde/ámbar/rojo.
2. La CADENA CAUSA-EFECTO dibujada arriba, con los cuatro eslabones
   conectados por flechas, resaltando los indicadores que la forman.
3. Cuatro indicadores: número de rojos, número de ámbares, caída del
   margen en puntos, y el sobrecosto de reprocesos más fletes.
4. Un SIMULADOR: al restituir el presupuesto de capacitación, mostrar
   qué indicadores se moverían y en qué orden temporal (3, 6, 12 meses),
   marcando claramente que es una proyección y no un dato.
5. Tabla de datos complementarios comparando los dos periodos.

Reglas:
- No inventes ningún dato: todos los números salen de los datos que te di.
- Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
- Los controles deben recalcular TODO al instante, sin recargar la página.
```

---

**Nota para el alumno:** si la IA te pide datos que no tienes, dilo en la hoja de trabajo. Que los pida es buena señal; que los invente, no.

📎 **Documentos a adjuntar:** Ninguno. Si el equipo trabaja con una empresa real, se sugiere adjuntar su tablero de indicadores del último semestre y el estado de resultados comparativo.

## Recursos adicionales

- Kaplan, R. S. y Norton, D. P. (1996). *The Balanced Scorecard: Translating Strategy into Action*. Harvard Business School Press.
- Kaplan, R. S. y Norton, D. P. (2004). *Strategy Maps: Converting Intangible Assets into Tangible Outcomes*. Harvard Business School Press.
- Kaplan, R. S. y Norton, D. P. (1992). The Balanced Scorecard: Measures That Drive Performance. *Harvard Business Review*, 70(1), 71–79.
- Materiales del ejercicio (caso, hoja de trabajo, prompts, rúbrica, datos y tablero de referencia): ver la tabla en *Cómo usar este ejercicio en clase*.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** construcción del tablero de 16 indicadores, cadena causal, datos complementarios, prompts y rúbrica; guía de solución redactada con apoyo de IA al integrar el ejercicio al repositorio; pendiente de revisión docente.
