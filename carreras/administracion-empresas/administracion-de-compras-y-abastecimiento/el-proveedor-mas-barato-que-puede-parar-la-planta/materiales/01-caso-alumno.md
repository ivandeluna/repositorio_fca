> **Hoja del alumno.** No contiene la solución.

# El proveedor más barato que puede parar la planta

**Carrera:** Administración de Empresas
**Materia:** Administración de Compras y Abastecimiento
**Tema:** Clasificación de proveedores, concentración del gasto y riesgo de suministro
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá construir una clasificación ABC del gasto por proveedor y contrastarla contra una clasificación de riesgo de suministro; verificar críticamente si el asistente de IA confundió volumen de compra con importancia estratégica; y fundamentar una decisión de abastecimiento comparando el gasto anual de un proveedor contra la exposición económica que representa.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; desarrollo de la matriz de posicionamiento, construcción del caso y guía de solución con apoyo de IA. Pendiente de revisión docente.

### El análisis ABC del gasto

El **análisis ABC**, derivado del principio de Pareto, ordena a los proveedores de mayor a menor gasto anual y los agrupa en tres categorías según el porcentaje acumulado:

- **Categoría A:** proveedores que concentran aproximadamente el primer 80 % del gasto.
- **Categoría B:** los que llevan del 80 % al 95 %.
- **Categoría C:** el resto.

Su utilidad es clara: indica dónde concentrar el esfuerzo de negociación, porque un punto porcentual arrancado a un proveedor de categoría A vale más que una renegociación completa con uno de categoría C.

**Su limitación también es clara, y es el objeto de este ejercicio: el ABC mide una sola dimensión.** Un proveedor puede representar el 0.5 % del gasto y ser, al mismo tiempo, el único del mercado capaz de surtir una pieza sin la cual la línea se detiene. En la clasificación por gasto aparecerá en el último lugar.

### El riesgo de suministro como segundo eje

Peter Kraljic propuso en 1983 cruzar el gasto con una segunda dimensión —el **riesgo de suministro**— y obtener cuatro cuadrantes con estrategias distintas:

|                      | **Riesgo de suministro bajo**                                                       | **Riesgo de suministro alto**                                                                      |
| -------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Gasto alto**       | **Apalancados.** Hay competencia: negociar precio, licitar, consolidar volumen.     | **Estratégicos.** Relación de largo plazo, contratos, desarrollo conjunto, planes de contingencia. |
| **Gasto bajo**       | **Rutinarios.** Simplificar: catálogos, compra automática, reducir costo de gestión. | **Cuello de botella.** Asegurar el suministro: inventario de resguardo, segunda fuente, contrato.  |

El riesgo de suministro se estima con tres variables observables:

1. **Número de fuentes alternativas** calificadas que podrían surtir lo mismo.
2. **Semanas de resustitución:** cuánto tardaría la empresa en homologar y poner a producir a un proveedor alterno.
3. **Efecto de la interrupción:** ninguno, menor, paro parcial o paro total de la línea.

El error que este ejercicio busca provocar es el siguiente: **el cuadrante de cuello de botella es invisible para el ABC**, porque está formado precisamente por los proveedores de gasto bajo. Quien clasifica solo por monto nunca lo ve, y la recomendación natural —"depuremos la cola de proveedores pequeños"— ataca justo ahí.

## Ejercicio / caso práctico

**Industrias del Nazas, S.A. de C.V.** es una empresa metalmecánica de Torreón con 340 empleados. Compra a 18 proveedores por un total de **$22,500,000** al año. Si la línea se detiene, la empresa deja de generar **$410,000 semanales** de margen de contribución.

| # | Proveedor | Gasto anual | Fuentes alternativas | Semanas de resustitución | Efecto si se interrumpe |
|---|-----------|-------------|----------------------|--------------------------|--------------------------|
| 1 | Aceros del Norte | $4,820,000 | 4 | 2 | Menor |
| 2 | Resinas Monclova | $3,650,000 | 2 | 6 | Paro parcial |
| 3 | Empaques Laguna | $2,940,000 | 5 | 1 | Menor |
| 4 | Tornillería Industrial | $2,180,000 | 6 | 1 | Menor |
| 5 | Pinturas y Recubrimientos | $1,760,000 | 4 | 2 | Menor |
| 6 | Lubricantes del Bajío | $1,390,000 | 5 | 1 | Menor |
| 7 | Fletes Torreón | $1,120,000 | 4 | 1 | Menor |
| 8 | Cartón Corrugado | $940,000 | 6 | 1 | Menor |
| 9 | Herramental Gómez | $780,000 | 2 | 8 | Paro parcial |
| 10 | Papelería Comercial | $640,000 | 9 | 1 | Ninguno |
| 11 | Sellos Técnicos MX | $510,000 | 1 | 16 | Paro total |
| 12 | Uniformes La Comarca | $430,000 | 7 | 1 | Ninguno |
| 13 | Calibración y Metrología | $360,000 | 2 | 10 | Paro parcial |
| 14 | Gases Industriales | $295,000 | 3 | 2 | Paro parcial |
| 15 | Software de Nómina | $240,000 | 4 | 4 | Menor |
| 16 | Catalizador Especial | $185,000 | 1 | 24 | Paro total |
| 17 | Limpieza Industrial | $150,000 | 8 | 1 | Ninguno |
| 18 | Refacciones Eléctricas | $110,000 | 6 | 1 | Menor |

**Mandato de la dirección.** A cada equipo se le asigna uno distinto:

| Equipo | Instrucción que recibió de la dirección |
|--------|------------------------------------------|
| 1 | «Reduzcan el gasto de compras un 8 % este año.» |
| 2 | «Bajen de 18 a 12 proveedores para simplificar la administración.» |
| 3 | «Concentren las compras para ganar poder de negociación.» |
| 4 | «Prioricen proveedores locales de La Laguna.» |
| 5 | «Reduzcan a la mitad el riesgo de paro de línea sin aumentar el gasto más de 3 %.» |

**Se pide (cinco pasos):**

---

### Paso 1 · Clasificar con la IA · 10 min
**Entregable:** la respuesta de la IA, copiada.

Abre Claude o ChatGPT y usa el **prompt 1**. Pégale **solo tres columnas**: proveedor, gasto anual y fuentes alternativas. No le des todavía las de semanas ni la de efecto.

Pídele la clasificación ABC y un plan para cumplir el mandato de tu equipo. Guarda la respuesta completa: la vas a necesitar en el paso 3.

---

### Paso 2 · Comprobar el supuesto de Pareto · 5 min
**Entregable:** una cifra.

La IA casi siempre afirma que «el 20 % de los proveedores concentra el 80 % del gasto». Calcúlalo tú con estos datos:

1. Ordena los 18 de mayor a menor gasto.
2. Toma los primeros cuatro (el 20 % de 18, redondeado).
3. Suma su gasto y divídelo entre $22,500,000.

**Escribe el porcentaje real y compáralo con lo que afirmó la IA.**

---

### Paso 3 · Recibir el dato que faltaba · 10 min
**Entregable:** la tabla de abajo, llena.

El profesor te entrega ahora las dos columnas que no tenías: **semanas de resustitución** y **efecto si se interrumpe**. Usa el **prompt 2** para devolvérselas a la IA y confrontar su propio plan.

| Proveedor que la IA propuso tocar | Categoría ABC | Fuentes | Semanas | Efecto | ¿Sigue en pie la recomendación? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Responde por escrito:** la IA nunca pidió esta información. ¿Por qué no la echó de menos?

---

### Paso 4 · Construir el tablero · 15 min
**Entregable:** un archivo HTML que funcione.

Aquí no se llena una hoja: **se construye una herramienta**. Usa el **prompt 3** para que la IA genere un tablero en un solo archivo HTML y ábrelo en el navegador.

El tablero debe permitir **cambiar los umbrales** —cuántas fuentes y cuántas semanas marcan riesgo alto— y recalcular todo al instante. Pruébalo:

1. Con el umbral de 8 semanas, ¿cuántos proveedores quedan en cuello de botella?
2. Bájalo a 5 semanas. ¿Cuántos quedan ahora? ¿Quién entró?
3. Súbelo a 20. ¿Quién se queda solo en el cuadrante rojo?

**El umbral no te lo da el enunciado: lo decides tú.** Anota qué umbral propones para esta empresa y con qué argumento.

> Puedes comparar tu resultado con [`materiales/tablero-proveedores.html`](materiales/tablero-proveedores.html). No es «la respuesta correcta»: es una versión de referencia. Si la tuya hace algo distinto y lo justificas, está bien.

---

### Paso 5 · Decidir y presentar · 10 min
**Entregable:** 6–8 líneas y el tablero proyectado.

Reformula el mandato de tu equipo en una propuesta ejecutable, que incluya:

- Qué proveedores sí se tocan.
- Cuáles quedan intocables y por qué.
- Qué medida concreta propones para el cuello de botella más grave, con su costo aproximado.
- Qué umbral de riesgo fijaste y con qué argumento.

**Plenaria.** Cada equipo presenta su tablero y responde: ¿cuál de los cinco mandatos era el único que no llevaba a tocar un proveedor crítico?

---

## Prompts sugeridos para hacerlo con Claude o ChatGPT

### Prompt 1 — clasificación (paso 1)

Pega **solo** nombre, gasto y fuentes alternativas.

```
Actúa como analista de compras.

Empresa: Industrias del Nazas, metalmecánica, 340 empleados.
Gasto anual de compras: $22,500,000 entre 18 proveedores.

[pega aquí: proveedor | gasto anual | fuentes alternativas]

Mandato de la dirección: [el mandato de tu equipo]

1. Clasifica a los proveedores en categorías A, B y C por porcentaje
   acumulado de gasto (80 % / 95 % / resto). Muestra la tabla ordenada
   con el porcentaje individual y el acumulado.
2. Indica qué porcentaje del gasto concentra el 20 % de los proveedores,
   calculado con estos datos y no con el principio general.
3. Propón un plan para cumplir el mandato: qué proveedores tocarías
   y en qué orden.

Usa únicamente los datos que te entregué. Si necesitas información que
no te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

Ahora sí, pega la tabla completa.

```
Te entrego dos columnas que antes no tenías: semanas de resustitución
y efecto si el suministro se interrumpe.

[pega la tabla completa de los 18]

1. ¿Tu plan anterior proponía tocar a algún proveedor cuyo suministro
   provoque paro parcial o total? Nómbralos uno por uno.
2. Clasifica a los 18 en la matriz de Kraljic (apalancado, estratégico,
   rutinario, cuello de botella). Declara el criterio exacto con el que
   separas riesgo alto de riesgo bajo y aplícalo igual a todos.
3. Para cada proveedor de riesgo alto calcula la exposición:
   semanas de resustitución × $410,000 × factor de efecto
   (paro total = 100 %, paro parcial = 45 %).
4. Ordénalos por exposición y compárala contra su gasto anual.

Después responde: ¿en qué lugar de la clasificación ABC quedó el
proveedor con mayor exposición? ¿Por qué no lo detectaste antes?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos (18 proveedores):
[pega la tabla completa]
Margen de contribución que se pierde por semana de paro: $410,000

El tablero debe contener:

1. Encabezado con el nombre de la empresa y un veredicto general
   (rojo si hay proveedores en cuello de botella).
2. Cuatro indicadores: gasto anual total, número de proveedores en
   cuello de botella, exposición total, y la razón entre la exposición
   mayor y el gasto de ese proveedor.
3. CONTROLES EDITABLES para margen semanal de paro, umbral de fuentes
   y umbral de semanas. Al cambiar cualquiera, TODO se recalcula.
4. Matriz de Kraljic con los 18 ubicados: eje X riesgo de suministro,
   eje Y gasto anual en escala logarítmica, tamaño del punto
   proporcional al gasto, rojo si el riesgo es alto.
5. Barras de exposición por proveedor, de mayor a menor, con la razón
   exposición/gasto de cada uno.
6. Curva de Pareto del gasto acumulado, marcando dónde cae el 20 % de
   los proveedores y qué porcentaje del gasto concentra realmente.
7. Panel de alertas generado automáticamente para cada cuello de botella.
8. Tabla de los 18 con ABC, cuadrante y exposición, resaltando los
   cuellos de botella.

Reglas de cálculo:
- ABC por porcentaje acumulado: A hasta 80 %, B hasta 95 %, C el resto.
- Riesgo alto si: fuentes <= umbral, O semanas >= umbral, O efecto de paro.
- Exposición = semanas × margen semanal × factor de efecto
  (paro total 1.00, paro parcial 0.45, los demás 0).
- No inventes ningún dato: todos los números salen de la tabla.

Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
```

📎 **Documentos a adjuntar:** Ninguno: los datos del caso se pueden pegar directamente en el prompt. Si el equipo trabaja con una empresa real, se sugiere adjuntar el reporte de compras por proveedor del último ejercicio y, si existe, el padrón de proveedores homologados con sus alternativas calificadas.

## Recursos adicionales

- Kraljic, P. (1983). Purchasing Must Become Supply Management. *Harvard Business Review*, 61(5), 109–117.
- Monczka, R. M., Handfield, R. B., Giunipero, L. C. y Patterson, J. L. (2021). *Purchasing and Supply Chain Management* (7.ª ed.). Cengage Learning.
- Chopra, S. y Meindl, P. (2019). *Supply Chain Management: Strategy, Planning, and Operation* (7.ª ed.). Pearson.
- `tablero-proveedores.html` — **tablero de referencia ya funcionando.** Ábrelo y cambia los umbrales.
- `matriz-vacia.svg` — hoja de trabajo para los equipos, lista para imprimir.
- `matriz-resuelta.svg` — la misma matriz con los 18 proveedores ubicados, para proyectar en la plenaria.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** construcción del caso de 18 proveedores, cálculo de exposiciones, prompts, tabla de errores típicos y rúbrica; pendiente de revisión docente.
