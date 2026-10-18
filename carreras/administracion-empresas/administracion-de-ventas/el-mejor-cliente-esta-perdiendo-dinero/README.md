# El mejor cliente de la empresa está perdiendo dinero

**Carrera:** Administración de Empresas
**Materia:** Administración de Ventas
**Tema:** Rentabilidad por cliente y costo de servir
**Nivel:** Intermedio
**Duración estimada:** 50 min

> ### 🎯 El gancho
> **El segundo cliente en ventas y tercero en margen bruto resulta ser el último en margen neto: pierde $402,188 al año.** Y el cliente más pequeño de los doce es el de mayor margen neto en porcentaje.
>
> Ninguna de las dos cosas se ve en el reporte de ventas. El asistente de IA va a premiar al cliente equivocado, porque solo mira el margen bruto.

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
| [`materiales/tablero-rentabilidad-clientes.html`](materiales/tablero-rentabilidad-clientes.html) | Tablero de referencia ya funcionando (HTML) | Profesor, para la plenaria |

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular la rentabilidad neta por cliente incorporando el costo de servir y el costo financiero del crédito; verificar críticamente si el asistente de IA se quedó en el margen bruto; y fundamentar una decisión de depuración o renegociación de cartera distinguiendo entre clientes que destruyen valor y clientes que solo son pequeños.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; construcción del caso, cálculo de costos de servir y guía de solución con apoyo de IA. Pendiente de revisión docente.

### Por qué el margen bruto miente

El reporte de ventas de casi cualquier empresa ordena a los clientes por facturación o por margen bruto. Ese margen solo resta el costo de lo vendido, y da por supuesto que **atender a un cliente cuesta lo mismo que atender a otro**. No es cierto.

Un cliente que coloca 186 pedidos al año, pide 44 líneas en cada uno, exige 186 entregas, recibe 22 visitas del vendedor, devuelve 41 veces y paga a 105 días **consume un volumen de recursos radicalmente distinto** de otro que coloca 9 pedidos, recibe 9 entregas y paga a 30 días. Ninguno de esos consumos aparece en el costo de ventas.

### Los tres niveles de margen

$$\text{Margen bruto} = \text{Ventas} - \text{Costo de lo vendido}$$

$$\text{Costo de servir} = \sum (\text{transacciones} \times \text{costo unitario de cada actividad})$$

$$\text{Costo financiero} = \text{Ventas} \times \text{días de crédito} \times \frac{\text{tasa anual}}{365}$$

$$\text{Margen neto por cliente} = \text{Margen bruto} - \text{Costo de servir} - \text{Costo financiero}$$

El costo de servir se construye igual que un costeo por actividades, pero con generadores comerciales: número de pedidos, líneas por pedido, entregas, visitas y devoluciones.

### La curva de ballena

Al ordenar los clientes por margen neto acumulado, suele aparecer una curva que sube, alcanza un máximo y **vuelve a bajar**: la utilidad acumulada llega a superar la utilidad total de la empresa, y los últimos clientes se la comen. Esa forma —conocida como curva de ballena— es la evidencia visual de que hay clientes que destruyen valor mientras figuran como importantes en el reporte de ventas.

La conclusión correcta rara vez es «despidamos a ese cliente». Suele ser renegociar: pedido mínimo, frecuencia de entrega, plazo de pago o precio.

## Ejercicio / caso práctico

**Distribuidora Industrial Laguna, S.A. de C.V.** factura $42,100,000 al año entre doce clientes. Su tasa de financiamiento es del 18 % anual.

| Cliente | Ventas | Margen bruto | Pedidos | Líneas por pedido | Entregas | Visitas | Devoluciones | Días de crédito |
|---------|--------|--------------|---------|-------------------|----------|---------|--------------|------------------|
| Autoservicios del Norte | $8,400,000 | 18.5 % | 96 | 42 | 96 | 24 | 14 | 75 |
| Cadena Hogar Express | $6,900,000 | 15.2 % | 186 | 44 | 186 | 22 | 41 | 105 |
| Grupo Constructor Nazas | $5,600,000 | 21.2 % | 18 | 6 | 18 | 9 | 1 | 60 |
| Industrial Torreón | $4,300,000 | 24.1 % | 24 | 8 | 24 | 11 | 2 | 45 |
| Súper Abastos Lerdo | $3,700,000 | 19.8 % | 92 | 29 | 92 | 16 | 17 | 75 |
| Ferretera La Laguna | $3,200,000 | 26.8 % | 28 | 11 | 28 | 12 | 2 | 45 |
| Mayoreo del Bravo | $2,400,000 | 25.5 % | 31 | 12 | 31 | 13 | 4 | 45 |
| Materiales Gómez | $2,100,000 | 29.5 % | 22 | 9 | 22 | 10 | 3 | 30 |
| Distribuidora Cerro | $1,800,000 | 31.2 % | 14 | 7 | 14 | 6 | 1 | 30 |
| Constructora Peñoles | $1,500,000 | 28.8 % | 12 | 5 | 12 | 7 | 1 | 60 |
| Comercial Matamoros | $1,250,000 | 33.5 % | 11 | 5 | 11 | 5 | 0 | 30 |
| Talleres Unidos | $950,000 | 34.8 % | 9 | 4 | 9 | 4 | 1 | 30 |

**Costos unitarios de las actividades comerciales:**

| Actividad | Generador | Costo unitario |
|-----------|-----------|----------------|
| Procesamiento de pedido | pedido | $840 |
| Captura y surtido de línea | línea de pedido | $65 |
| Entrega | entrega | $1,250 |
| Visita del vendedor | visita | $1,900 |
| Gestión de devolución | devolución | $3,200 |

**Mandato de la dirección.** Uno distinto por equipo:

| Equipo | Instrucción que recibió |
|--------|--------------------------|
| 1 | «Suban las ventas 10 % sin aumentar la fuerza de ventas.» |
| 2 | «Depuren la cartera: queremos menos clientes y más utilidad.» |
| 3 | «Prioricen a los clientes grandes, ahí está el negocio.» |
| 4 | «Reduzcan el capital de trabajo invertido en clientes.» |
| 5 | «Suban la utilidad neta sin perder ningún cliente.» |

**Se pide (cinco pasos):**

---

### Paso 1 · Rankear con la IA · 10 min
**Entregable:** la respuesta de la IA, copiada.

Usa el **prompt 1**. Pégale **solo** las columnas de cliente, ventas y margen bruto. **No le des todavía** las columnas de pedidos, líneas, entregas, visitas, devoluciones ni días de crédito.

Pídele el ranking de clientes y un plan para cumplir el mandato de tu equipo.

---

### Paso 2 · Anotar la predicción · 5 min
**Entregable:** tres nombres, escritos antes de calcular.

Antes de seguir, escriban en una hoja:

1. ¿Cuál creen que es el cliente **más** rentable de los doce?
2. ¿Cuál el **menos** rentable?
3. ¿Cuántos creen que están **perdiendo** dinero?

Guarden la hoja. Se compara al final.

---

### Paso 3 · Recibir el dato que faltaba · 10 min
**Entregable:** la tabla de margen neto, completa.

El profesor entrega ahora las columnas de actividad y de crédito, y la tabla de costos unitarios. Usa el **prompt 2**.

| Cliente | Margen bruto | Costo de servir | Costo financiero | Margen neto | Margen neto % | Lugar en bruto | Lugar en neto |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

**Responde por escrito:** ¿cuántos lugares se movió el cliente que más cambió de posición? ¿Por qué la IA no pidió estos datos?

---

### Paso 4 · Construir el tablero · 15 min
**Entregable:** un archivo HTML que funcione.

Usa el **prompt 3** para generar un tablero con la curva de ballena, el ranking doble y los controles editables. Ábrelo y prueba:

1. ¿En qué cliente alcanza su máximo la utilidad acumulada?
2. Sube el costo de una entrega de $1,250 a $1,900. ¿Cuántos clientes quedan en negativo?
3. Baja el plazo de Cadena Hogar Express de 105 a 45 días. ¿Alcanza para volverlo rentable?

> Puedes comparar con [`materiales/tablero-rentabilidad-clientes.html`](materiales/tablero-rentabilidad-clientes.html). No es «la respuesta correcta»: es una referencia.

---

### Paso 5 · Decidir y presentar · 10 min
**Entregable:** 6–8 líneas.

Reformula el mandato de tu equipo en una propuesta que incluya: qué clientes se renegocian y con qué condición concreta (pedido mínimo, frecuencia de entrega, plazo, precio), cuáles no se tocan, y qué pasaría con la utilidad total si la propuesta funciona.

**Plenaria.** Se comparan las predicciones del paso 2 contra el resultado. Pregunta de cierre: **¿por qué la respuesta no es «dejar de venderle al cliente que pierde»?**

---

## Solución / guía de solución

<details markdown="1">
<summary><strong>Mostrar guía para el profesor</strong></summary>

> ⚠️ **Nota de transparencia:** esta guía de solución se redactó con apoyo de IA al integrar el ejercicio al repositorio; las cifras se verificaron con código contra `materiales/datos.csv`. Costo financiero calculado con 365 días. Pendiente de revisión docente.

### Resultados correctos (paso 3)

| Cliente | Margen bruto | Costo de servir | Costo financiero | **Margen neto** | Margen neto % | Lugar en bruto | Lugar en neto |
|---|---:|---:|---:|---:|---:|:---:|:---:|
| Grupo Constructor Nazas | $1,187,200 | $64,940 | $165,699 | **$956,561** | 17.1 % | 2 | **1** |
| Industrial Torreón | $1,036,300 | $89,940 | $95,425 | **$850,935** | 19.8 % | 4 | **2** |
| Autoservicios del Norte | $1,554,000 | $553,120 | $310,685 | **$690,195** | 8.2 % | 1 | **3** |
| Ferretera La Laguna | $857,600 | $107,740 | $71,014 | **$678,846** | 21.2 % | 5 | **4** |
| Materiales Gómez | $619,500 | $87,450 | $31,068 | **$500,982** | 23.9 % | 7 | **5** |
| Distribuidora Cerro | $561,600 | $50,230 | $26,630 | **$484,740** | 26.9 % | 9 | **6** |
| Mayoreo del Bravo | $612,000 | $126,470 | $53,260 | **$432,270** | 18.0 % | 8 | **7** |
| Comercial Matamoros | $418,750 | $36,065 | $18,493 | **$364,192** | 29.1 % | 11 | **8** |
| Constructora Peñoles | $432,000 | $45,480 | $44,384 | **$342,136** | 22.8 % | 10 | **9** |
| Talleres Unidos | $330,600 | $31,950 | $14,055 | **$284,595** | 30.0 % | 12 | **10** |
| Súper Abastos Lerdo | $732,600 | $450,500 | $136,849 | **$145,251** | 3.9 % | 6 | **11** |
| Cadena Hogar Express | $1,048,800 | $1,093,700 | $357,288 | **−$402,188** | −5.8 % | 3 | **12** |
| **Total** | **$9,390,950** | **$2,737,585** | **$1,324,849** | **$5,328,516** | **12.7 %** | | |

**Lo que hay que ver en la tabla:**

- **Un solo cliente destruye valor:** Cadena Hogar Express. Su costo de servir ($1,093,700) ya es mayor que todo su margen bruto, antes del costo financiero.
- **El que más se mueve:** Cadena Hogar Express, del lugar 3 al 12 (**nueve lugares**). Le sigue Súper Abastos Lerdo, del 6 al 11.
- **El más rentable en pesos** es Grupo Constructor Nazas ($956,561). **El de mayor margen neto en porcentaje** es Talleres Unidos (30.0 %), el más pequeño de los doce.
- El componente que más pesa en el costo de servir de Cadena Hogar Express es el de **líneas**: 186 pedidos × 44 líneas = 8,184 líneas × $65 = $531,960.

### Paso 4 · Respuestas del tablero

1. **Curva de ballena.** La utilidad acumulada alcanza su máximo en el cliente 11 (Súper Abastos Lerdo): **$5,730,703**, el 107.5 % de la utilidad neta total. El último cliente se come $402,188.
2. **Entrega a $1,900.** Sigue habiendo **un solo** cliente en negativo: Cadena Hogar Express baja a −$523,088. Súper Abastos Lerdo queda en $85,451, muy cerca de cero.
3. **Plazo de 105 a 45 días.** **No alcanza**: Cadena Hogar Express mejora a −$198,023, pero sigue perdiendo. Tampoco alcanza solo con consolidar entregas: con un pedido semanal (52 al año, mismas líneas totales) y 105 días sigue en −$122,128. **Las dos medidas juntas** (pedido semanal y 45 días) lo llevan a cerca de **+$82,000**.

### Paso 5 · Respuesta a la pregunta de cierre

Dejar de venderle a Cadena Hogar Express elimina $1,048,800 de margen bruto, y no todo el costo de servir desaparece con él: parte es costo fijo de la fuerza de ventas, del almacén y de la flotilla. La salida correcta es **renegociar las condiciones que generan el costo**: pedido mínimo o entregas consolidadas, plazo de pago, un cargo o una política para devoluciones (41 al año, $131,200) y, si nada de eso es posible, el precio. El resto de la cartera no se toca; los clientes pequeños con margen alto se protegen.

**Por mandato:**

| Equipo | Trampa del mandato | Reformulación razonable |
|---|---|---|
| 1 · Subir ventas 10 % | Crecer con clientes como Cadena Hogar Express aumenta la pérdida | Crecer en clientes de margen neto alto y renegociar al que pierde |
| 2 · Depurar la cartera | Es probable que la IA proponga eliminar a los pequeños, que son los de mejor margen neto % | Depurar condiciones, no clientes |
| 3 · Priorizar a los grandes | Dos de los tres clientes más grandes están entre los tres últimos en margen neto % | Priorizar por margen neto, no por ventas |
| 4 · Reducir capital de trabajo | Es el único mandato alineado con la causa: los plazos de 75 y 105 días | Bajar plazos a Cadena Hogar Express, Autoservicios del Norte y Súper Abastos Lerdo |
| 5 · Más utilidad sin perder clientes | Exige renegociar en lugar de despedir | Es el mandato que lleva directo a la respuesta correcta |

### Errores frecuentes del asistente de IA

| Lo que suele hacer la IA | Por qué está mal | Qué debe responder el alumno |
|---|---|---|
| Ordena por margen bruto y recomienda priorizar a Autoservicios del Norte y Cadena Hogar Express | Supone que atender a todos cuesta lo mismo | Señalar que no pidió los datos de actividad |
| Multiplica las líneas por pedido por $65 sin multiplicar por el número de pedidos | Subestima el costo de líneas de Cadena Hogar Express en más de $500,000 | Calcular líneas totales = pedidos × líneas por pedido |
| Calcula el costo financiero como 18 % de las ventas | Olvida el plazo: el interés corre solo durante los días de crédito | Ventas × días × 18 % / 365 |
| Recomienda «dejar de venderle» al cliente que pierde | Ignora la parte fija del costo de servir y el margen bruto que se pierde | Proponer condiciones concretas de renegociación |
| Califica a Talleres Unidos como «cliente marginal» por su tamaño | Confunde tamaño con rentabilidad | Es el de mayor margen neto en porcentaje |

### Rúbrica

Ver [`materiales/04-rubrica.md`](materiales/04-rubrica.md).

</details>

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copiar y pegar en Claude o ChatGPT, **en orden**. No adelantes el prompt 2.

### Prompt 1 — primera respuesta (paso 1)

```
Actúa como analista comercial.

Distribuidora Industrial Laguna factura $42,100,000 al año entre doce
clientes. Tasa de financiamiento: 18 % anual.

[pega aquí SOLO las columnas: cliente, ventas, margen_bruto_pct]

Mandato de la dirección: [el mandato de tu equipo]

1. Calcula el margen bruto en pesos de cada cliente y ordénalos.
2. Identifica a los clientes más y menos rentables.
3. Propón un plan para cumplir el mandato: a qué clientes te enfocarías
   y a cuáles no.

Usa únicamente los datos que te entregué. Si para responder bien
necesitas información que no te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

```
Te entrego las columnas que antes no tenías: pedidos, líneas por pedido,
entregas, visitas, devoluciones y días de crédito.

[pega el archivo datos.csv completo]

Costos unitarios:
- Procesamiento de pedido: $840 por pedido
- Captura y surtido: $65 por línea de pedido
- Entrega: $1,250 por entrega
- Visita del vendedor: $1,900 por visita
- Gestión de devolución: $3,200 por devolución
Tasa de financiamiento: 18 % anual

1. Calcula para cada cliente: costo de servir, costo financiero
   (ventas × días de crédito × 18 % / 365) y margen neto.
2. Ordena a los clientes por margen bruto y por margen neto, lado a lado.
3. Señala cuántos lugares se movió cada uno.
4. Identifica a los clientes con margen neto negativo.

Después responde: ¿tu plan anterior se enfocaba en algún cliente que
destruye valor? ¿Por qué no lo detectaste?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos:
[pega aquí el contenido de datos.csv]
Costos unitarios: pedido $840, línea $65, entrega $1,250, visita $1,900, devolución $3,200. Tasa 18 % anual.

El tablero debe tener:
1. CONTROLES EDITABLES para los cinco costos unitarios y la tasa.
2. Cuatro indicadores: ventas totales, margen bruto total, margen neto
   total y número de clientes que destruyen valor.
3. CURVA DE BALLENA: clientes ordenados de mayor a menor margen neto,
   con la utilidad acumulada; marca dónde alcanza su máximo.
4. Ranking doble lado a lado: por margen bruto y por margen neto, con
   líneas que conecten al mismo cliente para ver cuánto se movió.
5. Barras de descomposición por cliente: margen bruto, costo de servir,
   costo financiero y margen neto.
6. Tabla de los doce con todas las columnas, resaltando los negativos.

Reglas:
- No inventes ningún dato: todos los números salen de los datos que te di.
- Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
- Los controles deben recalcular TODO al instante, sin recargar la página.
```

---

**Nota para el alumno:** si la IA te pide datos que no tienes, dilo en la hoja de trabajo. Que los pida es buena señal; que los invente, no.

📎 **Documentos a adjuntar:** Ninguno: los datos se pegan directamente. Si el equipo trabaja con una empresa real, se sugiere adjuntar el reporte de ventas por cliente del último ejercicio y, si existe, el registro de pedidos, entregas y devoluciones.

## Recursos adicionales

- Kaplan, R. S. y Narayanan, V. G. (2001). Measuring and Managing Customer Profitability. *Journal of Cost Management*, 15(5), 5–15.
- Kaplan, R. S. y Anderson, S. R. (2007). *Time-Driven Activity-Based Costing*. Harvard Business School Press.
- Cooper, R. y Kaplan, R. S. (1991). Profit Priorities from Activity-Based Costing. *Harvard Business Review*, 69(3), 130–135.
- Materiales del ejercicio (caso, hoja de trabajo, prompts, rúbrica, datos y tablero de referencia): ver la tabla en *Cómo usar este ejercicio en clase*.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** construcción del caso de doce clientes, cálculo de costos de servir, prompts, tabla de errores típicos y rúbrica; guía de solución redactada con apoyo de IA al integrar el ejercicio al repositorio; pendiente de revisión docente.
