# Mercado bursátil: acciones, tipo de cambio y tasas de interés

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Acciones y mercado bursátil
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el rendimiento de una acción (dividendos más ganancia de capital), calcular el rendimiento en pesos de una acción extranjera considerando el tipo de cambio, y explicar por qué el precio de las acciones tiende a bajar cuando suben las tasas de interés.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

Una **acción** es una parte de la propiedad de una empresa. Quien compra acciones se vuelve socio y gana de dos formas: con los **dividendos** (la parte de las utilidades que reparte la empresa) y con la **ganancia de capital** (vender la acción más cara de lo que se compró). A diferencia de la deuda, la acción no promete un pago fijo: puede ganar mucho o perder.

**¿Dónde se compran?** En México hay dos bolsas de valores: la **Bolsa Mexicana de Valores (BMV)** y la **Bolsa Institucional de Valores (BIVA)**. Su indicador principal es el **S&P/BMV IPC**, que sigue a las empresas más negociadas. Las acciones de empresas extranjeras, como las de Estados Unidos, se pueden comprar desde México en pesos a través del **Sistema Internacional de Cotizaciones (SIC)**, con una casa de bolsa.

**Rendimiento de una acción:**

Rendimiento = (precio final − precio inicial + dividendos) / precio inicial

**Acciones extranjeras y tipo de cambio.** Si un mexicano compra una acción de EE. UU., su rendimiento en pesos combina dos efectos: lo que gana la acción en dólares y lo que cambia el precio del dólar.

(1 + rendimiento en pesos) = (1 + rendimiento en dólares) × (1 + variación del tipo de cambio)

Si el peso se deprecia (el dólar sube), el inversionista gana más en pesos. Si el peso se aprecia, gana menos y hasta puede perder.

**Acciones y tasas de interés.** Una forma sencilla de valuar una acción es el **modelo de Gordon**, que supone que el dividendo crece siempre a una tasa constante *g*:

Precio = dividendo del próximo año / (k − g)

donde *k* es el rendimiento que exige el inversionista. Cuando el Banco de México o la Reserva Federal **suben las tasas**, los Cetes y los bonos pagan más, y el inversionista le exige más a las acciones (*k* sube). Con *k* más alto, el precio **baja**. Por eso las bolsas suelen caer cuando suben las tasas.

## Ejercicio / caso práctico

La familia dueña de **Nogalera del Nazas, S.A. de C.V.** (exportadora de nuez de Torreón) quiere invertir parte de sus ahorros personales en la bolsa y compara tres situaciones.

**Datos (ilustrativos, no son cotizaciones reales):**

| Situación | Datos |
|---|---|
| A. Acción mexicana en la BMV | Compra 1,000 acciones a $50.00. En un año la empresa paga un dividendo de $1.50 por acción y el precio sube a $54.00. |
| B. Acción de EE. UU. por el SIC | Compra 100 acciones a USD 120.00 con el dólar a 18.50. En un año la acción vale USD 126.00. El dólar puede terminar en 17.60, 18.50 o 19.40. |
| C. Efecto de las tasas | Una empresa pagará un dividendo de $2.00 el próximo año, que crecerá 4 % anual. Los inversionistas exigen 10 %, pero el banco central sube las tasas y ahora exigen 11 %. |
| Referencia | Cetes a un año: 7.50 % anual |

**Se pide:**

1. **Acción mexicana.** Calcula el rendimiento total y sepáralo en rendimiento por dividendo y ganancia de capital. ¿Rindió más o menos que los Cetes?
2. **Acción extranjera.** Calcula cuántos pesos invirtió, cuántos pesos tiene al final y el rendimiento en pesos en cada escenario del tipo de cambio.
3. **Tasas de interés.** Con el modelo de Gordon, calcula el precio de la acción con *k* = 10 % y con *k* = 11 %. ¿Cuánto cambió el precio?
4. **Reflexión.** Nogalera vende en dólares. ¿Qué le pasa a sus ingresos en pesos cuando el peso se deprecia? ¿Por qué eso puede hacer que suban las acciones de las empresas exportadoras?
5. **Datos reales con IA.** Pide a la IA el rendimiento del último año del S&P/BMV IPC y del S&P 500 medido en pesos, y verifica las cifras en una fuente confiable.

## Solución / guía de solución

**1. Acción mexicana**

- Inversión: 1,000 × $50 = $50,000. Al final: 1,000 × ($54 + $1.50) = $55,500.
- Rendimiento total = (54 − 50 + 1.50) / 50 = **11.00 %**, del cual 3.00 % es dividendo (1.50 / 50) y 8.00 % es ganancia de capital (4 / 50).
- Rindió 3.5 puntos más que los Cetes (7.50 %). Esa diferencia es el premio por el riesgo de invertir en acciones: el precio también pudo haber bajado.

**2. Acción extranjera**

- Inversión: 100 × USD 120 × 18.50 = **$222,000**. En dólares la acción rinde (126 − 120) / 120 = 5 %.

| Dólar al final | Variación del TC | Valor final en pesos | Rendimiento en pesos |
|---:|---:|---:|---:|
| 17.60 | −4.86 % | 221,760 | **−0.11 %** |
| 18.50 | 0.00 % | 233,100 | **5.00 %** |
| 19.40 | +4.86 % | 244,440 | **10.11 %** |

Con el mismo 5 % de la acción, el resultado en pesos va de una pequeña pérdida a una ganancia de 10 %. Al comprar acciones extranjeras también se compra **riesgo cambiario**. Comprobación: 1.05 × 1.0486 − 1 = 10.11 %.

**3. Tasas de interés**

- Con k = 10 %: Precio = 2.00 / (0.10 − 0.04) = **$33.33**
- Con k = 11 %: Precio = 2.00 / (0.11 − 0.04) = **$28.57**
- El precio cae **14.3 %** solo porque subió en un punto el rendimiento exigido, sin que la empresa cambiara nada.

**4. Reflexión (respuesta abierta)**

Si el peso se deprecia, cada dólar que vende Nogalera se convierte en más pesos, así que sus ingresos y utilidades en pesos suben. Por eso, cuando el peso se debilita, el mercado suele premiar a las empresas exportadoras y castigar a las que tienen deudas o costos en dólares.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT. Puedes cambiar los datos por los de una acción real.

```
Actúa como asesor financiero y explica de forma sencilla, para un estudiante
de licenciatura en Comercio Exterior.

Un inversionista mexicano compara:
A) 1,000 acciones mexicanas compradas a $50.00; en un año pagan un
   dividendo de $1.50 por acción y el precio sube a $54.00.
B) 100 acciones de EE. UU. compradas por el SIC a USD 120.00 con el dólar a
   18.50; en un año valen USD 126.00. El dólar puede terminar en 17.60,
   18.50 o 19.40.
C) Una acción que pagará un dividendo de $2.00 el próximo año, con
   crecimiento de 4 % anual; el rendimiento exigido sube de 10 % a 11 %.

1. Calcula el rendimiento total de A y sepáralo en dividendo y ganancia de
   capital; compáralo con Cetes a 7.50 %.
2. Calcula para B la inversión en pesos, el valor final en pesos y el
   rendimiento en pesos en cada escenario; explica el efecto del tipo de
   cambio.
3. Usa el modelo de Gordon para valuar C con 10 % y 11 % y explica por qué
   suben o bajan las bolsas cuando cambian las tasas de interés.

Presenta los resultados en tablas y muestra cada fórmula con los números
sustituidos.
```

**Documentos a adjuntar:** ninguno.

## Recursos adicionales

- Bolsa Mexicana de Valores (bmv.com.mx) y Bolsa Institucional de Valores (biva.mx): información de emisoras e índices.
- Banco de México: tipo de cambio FIX histórico, para medir el rendimiento de una acción extranjera en pesos.
