# Derivados II: opciones de tipo de cambio

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Derivados: opciones
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá explicar qué es una opción de compra (call) y una opción de venta (put) sobre el dólar, calcular el resultado de un importador que se cubre con un call y de un exportador que se cubre con un put, y comparar la cobertura con opciones contra la cobertura con forward.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

Una **opción** da a quien la compra el **derecho, pero no la obligación**, de comprar o vender algo a un precio fijado hoy, llamado **precio de ejercicio** (*strike*), en una fecha futura. Por ese derecho se paga hoy un precio llamado **prima**.

| Tipo | Derecho que da | ¿Quién la usa en comercio exterior? |
|---|---|---|
| **Call** (opción de compra) | Comprar dólares al precio de ejercicio | El **importador**, que teme que el dólar suba |
| **Put** (opción de venta) | Vender dólares al precio de ejercicio | El **exportador**, que teme que el dólar baje |

**La lógica del seguro.** Una opción funciona como un seguro de auto: se paga la prima por adelantado. Si pasa lo malo (el dólar se mueve en contra), la opción se ejerce y protege. Si no pasa (el dólar se mueve a favor), no se ejerce, se pierde la prima y se aprovecha el mejor tipo de cambio.

**Fórmulas para un call de importador:**

- Si al vencimiento el dólar está **arriba** del precio de ejercicio: se ejerce y se compra al precio de ejercicio.
- Si está **abajo**: no se ejerce y se compra en el mercado.
- Tipo de cambio efectivo = mínimo(spot al vencimiento, precio de ejercicio) + prima
- **Punto de equilibrio** = precio de ejercicio + prima

**Fórmula para un put de exportador:** tipo de cambio efectivo = máximo(spot al vencimiento, precio de ejercicio) − prima

**Opción vs. forward:**

| | Forward | Opción |
|---|---|---|
| ¿Cuesta al contratarlo? | No | Sí, la prima |
| ¿Protege si el dólar se mueve en contra? | Sí | Sí |
| ¿Aprovecha si el dólar se mueve a favor? | No | **Sí** |
| ¿Obliga a operar? | Sí | No |

**Opciones sobre tasas de interés.** La misma idea se usa en créditos: un **cap** es una opción que pone un techo a la tasa variable de un crédito. Si la TIIE de Fondeo sube por encima del techo, la opción paga la diferencia.

## Ejercicio / caso práctico

**Nogalera del Nazas, S.A. de C.V.** necesita comprar en Estados Unidos una máquina descascaradora de nuez por **USD 150,000, que pagará en 90 días**. Al mismo tiempo, cobrará **USD 200,000** por una exportación en la misma fecha.

**Datos de mercado (ilustrativos, no son cotizaciones reales):**

| Dato | Valor |
|---|---:|
| Tipo de cambio spot hoy | 18.50 MXN/USD |
| Forward a 90 días (ver el ejercicio de forwards) | 18.6603 MXN/USD |
| **Call** USD/MXN a 90 días: precio de ejercicio / prima | 18.80 / 0.30 MXN por dólar |
| **Put** USD/MXN a 90 días: precio de ejercicio / prima | 18.30 / 0.25 MXN por dólar |

**Se pide:**

1. **Call para la importación.** ¿Cuánto paga Nogalera de prima por cubrir los USD 150,000? ¿Cuál es su punto de equilibrio?
2. **Escenarios.** Calcula cuántos pesos le cuesta la máquina sin cobertura, con el call y con el forward si en 90 días el dólar está en 17.50, 18.50, 19.10, 19.50 o 20.50. ¿En qué casos ejerce la opción?
3. **Put para la exportación.** Calcula el tipo de cambio efectivo y los pesos que recibe por los USD 200,000 si en 90 días el dólar está en 17.50, 18.30, 19.00 o 19.50.
4. **Decisión.** Si el director de finanzas cree que el dólar bajará pero no está seguro, ¿qué le conviene más para la importación, el forward o el call? Justifica.
5. **Pregunta para pensar.** Nogalera paga y cobra dólares en la misma fecha. ¿Necesita cubrir las dos operaciones completas? (Pista: cobertura natural.)

## Solución / guía de solución

**1. Prima y punto de equilibrio**

- Prima total = 150,000 × 0.30 = **$45,000** (se paga hoy y no se recupera).
- Punto de equilibrio = 18.80 + 0.30 = **19.10**. Por encima de ese nivel, el call ya salió mejor que no cubrirse.

**2. Escenarios de la importación (USD 150,000)**

| Dólar en 90 días | ¿Ejerce el call? | Sin cobertura | Con call (incluye prima) | Con forward | TC efectivo con call |
|---:|---|---:|---:|---:|---:|
| 17.50 | No | 2,625,000 | 2,670,000 | 2,799,045 | 17.80 |
| 18.50 | No | 2,775,000 | 2,820,000 | 2,799,045 | 18.80 |
| 19.10 | Sí | 2,865,000 | 2,865,000 | 2,799,045 | 19.10 |
| 19.50 | Sí | 2,925,000 | 2,865,000 | 2,799,045 | 19.10 |
| 20.50 | Sí | 3,075,000 | 2,865,000 | 2,799,045 | 19.10 |

Con el call, la máquina **nunca cuesta más de $2,865,000**, y si el dólar baja Nogalera aprovecha el precio más bajo (solo pierde la prima). El forward fija $2,799,045 en todos los casos: es más barato si el dólar sube, pero no deja aprovechar una baja.

**3. Put para la exportación (USD 200,000)**

| Dólar en 90 días | ¿Ejerce el put? | TC efectivo (neto de prima) | Pesos recibidos | Sin cobertura |
|---:|---|---:|---:|---:|
| 17.50 | Sí | 18.05 | 3,610,000 | 3,500,000 |
| 18.30 | Indiferente | 18.05 | 3,610,000 | 3,660,000 |
| 19.00 | No | 18.75 | 3,750,000 | 3,800,000 |
| 19.50 | No | 19.25 | 3,850,000 | 3,900,000 |

El put garantiza un **piso** de 18.05 pesos por dólar y deja abierta la ganancia si el dólar sube.

**4. Decisión (respuesta abierta)**

Si cree que el dólar bajará, el call le conviene más: lo protege por si se equivoca y le permite aprovechar la baja si acierta. El precio de esa flexibilidad es la prima de $45,000. Si lo único que importa es la certeza al menor costo, el forward es mejor.

**5. Cobertura natural**

Como paga USD 150,000 y cobra USD 200,000 el mismo día, puede usar los dólares que cobra para pagar la máquina. Su exposición real es solo de **USD 50,000** (lo que le sobra). Cubrir ambas operaciones completas sería pagar primas de más. Antes de contratar derivados, una empresa siempre debe calcular su **posición neta** en dólares.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT.

```
Actúa como especialista en coberturas cambiarias y explica de forma sencilla,
para un estudiante de licenciatura en Comercio Exterior.

Una empresa mexicana pagará USD 150,000 por una importación dentro de 90
días y cobrará USD 200,000 por una exportación en la misma fecha.
Datos de mercado (ilustrativos):
- Spot: 18.50 MXN/USD; forward a 90 días: 18.6603
- Call USD/MXN a 90 días: precio de ejercicio 18.80, prima 0.30 MXN por USD
- Put USD/MXN a 90 días: precio de ejercicio 18.30, prima 0.25 MXN por USD

1. Calcula la prima total del call para la importación y su punto de
   equilibrio.
2. Haz una tabla con el costo en pesos de la importación sin cobertura, con
   call y con forward si el dólar termina en 17.50, 18.50, 19.10, 19.50 y
   20.50, e indica cuándo se ejerce el call.
3. Haz la tabla equivalente para la exportación cubierta con el put, con
   el dólar en 17.50, 18.30, 19.00 y 19.50.
4. Explica qué es la cobertura natural y cuál es la posición neta en
   dólares de la empresa.

Muestra cada fórmula con los números sustituidos y usa lenguaje claro.
```

**Documentos a adjuntar:** ninguno.

## Recursos adicionales

- MexDer (mexder.com.mx): especificaciones de los contratos de opciones listadas.
- Lectura sugerida: capítulo de opciones sobre divisas en el libro de texto de finanzas internacionales del curso.
