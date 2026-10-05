# Derivados III: swaps de tasa de interés y de divisas

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Derivados: swaps
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá explicar qué es un swap, calcular los flujos de un swap de tasa de interés que convierte un crédito de tasa variable en tasa fija, y explicar cómo un swap de divisas ayuda a una empresa exportadora a alinear su deuda con la moneda de sus ingresos.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

Un **swap** (intercambio) es un contrato en el que dos partes acuerdan **intercambiar flujos de dinero** en fechas futuras, durante varios años. Se usa para cambiar el tipo de deuda que se tiene sin tener que pedir un crédito nuevo.

**1. Swap de tasa de interés (de variable a fija).** Muchas empresas tienen créditos en pesos a **tasa variable**, por ejemplo TIIE de Fondeo + 2 puntos. Desde 2025, la **TIIE de Fondeo** es la tasa de referencia que el Banco de México pide usar en los nuevos créditos y derivados en pesos, en lugar de la TIIE a 28 días. Si la TIIE sube, los intereses suben. Con un swap la empresa:

- **paga** al banco una tasa **fija**, y
- **recibe** del banco la tasa **variable** (TIIE de Fondeo).

Lo que recibe del swap compensa lo que paga de más en el crédito, así que su costo final queda fijo:

Costo total = (TIIE + margen del crédito) + tasa fija del swap − TIIE = **tasa fija del swap + margen**

En la práctica solo se intercambia la **diferencia neta** entre lo que cada parte debe. El monto del crédito se llama **nocional**: sirve para calcular los intereses, pero no se intercambia.

**2. Swap de divisas (cross-currency swap).** Las partes intercambian **capital e intereses en dos monedas distintas**:

1. **Al inicio:** intercambian los montos de capital (por ejemplo, pesos por dólares al tipo de cambio de hoy).
2. **Cada periodo:** cada uno paga los intereses de la moneda que recibió.
3. **Al final:** devuelven los montos de capital al **mismo tipo de cambio del inicio**.

Sirve, por ejemplo, para que una empresa que gana en dólares pero tiene deuda en pesos (o al revés) pague su deuda en la misma moneda en que recibe sus ingresos y así elimine el riesgo cambiario.

## Ejercicio / caso práctico

**Nogalera del Nazas, S.A. de C.V.** tiene dos problemas financieros.

**Parte A: crédito a tasa variable.** Tiene un crédito de **$10,000,000** a 3 años, con intereses anuales a **TIIE de Fondeo + 2.00 puntos** (simplificado a un pago al año). Teme que suban las tasas. Su banco le ofrece un swap en el que Nogalera **paga 7.80 % fijo** y **recibe TIIE de Fondeo** sobre el mismo nocional.

Supón que la TIIE de Fondeo resulta así (datos ilustrativos):

| Año | TIIE de Fondeo |
|---:|---:|
| 1 | 7.25 % |
| 2 | 8.50 % |
| 3 | 9.75 % |

**Parte B: deuda en pesos, ingresos en dólares.** Nogalera vende casi todo en dólares, pero tiene otro crédito por **$18,500,000** a tasa fija de **9.00 %** anual, que pagará en una sola exhibición al final de 3 años. Un banco le ofrece un swap de divisas a 3 años con tipo de cambio de **18.50 MXN/USD**: Nogalera recibirá los pesos para pagar su crédito y pagará dólares a una tasa fija de **5.50 %** anual.

**Se pide:**

1. **Parte A.** Calcula para cada año: intereses del crédito, lo que Nogalera paga y recibe en el swap, el pago neto del swap y su costo total. ¿Qué tasa paga en realidad?
2. **Parte A.** ¿En qué año el swap "le costó" dinero y en cuáles le ahorró? ¿Valió la pena?
3. **Parte B.** Calcula el nocional en dólares y los flujos anuales del swap en cada moneda, incluido el intercambio final.
4. **Parte B.** Sin swap, ¿cuántos dólares necesitaría Nogalera para pagar cada año los intereses en pesos y, al final, el capital si el dólar está en 17.50, 18.50 o 20.00? ¿Qué cambia con el swap?
5. **Datos reales con IA.** Pide a la IA el nivel actual de la TIIE de Fondeo y explica por qué los créditos nuevos ya no usan la TIIE a 28 días. Verifica en la página del Banco de México.

## Solución / guía de solución

**1 y 2. Swap de tasa de interés (nocional $10,000,000)**

| Año | TIIE | Intereses del crédito (TIIE + 2 %) | Nogalera paga fijo 7.80 % | Nogalera recibe TIIE | Pago neto del swap | Costo total |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 7.25 % | 925,000 | 780,000 | 725,000 | paga 55,000 | **980,000** |
| 2 | 8.50 % | 1,050,000 | 780,000 | 850,000 | recibe 70,000 | **980,000** |
| 3 | 9.75 % | 1,175,000 | 780,000 | 975,000 | recibe 195,000 | **980,000** |

Nogalera paga en realidad **9.80 % fijo** (7.80 % + 2.00 %) los tres años. En el año 1 el swap le costó $55,000 porque la TIIE estuvo por debajo de 7.80 %. En los años 2 y 3 le ahorró $265,000 en total. Pero igual que en cualquier cobertura, la decisión no se evalúa por el resultado: al contratarlo, Nogalera ganó **certeza** para presupuestar sus intereses.

**3. Swap de divisas**

- Nocional en dólares: 18,500,000 / 18.50 = **USD 1,000,000**
- Intereses anuales en pesos que recibe del banco: 18,500,000 × 9 % = **$1,665,000**, justo lo que debe pagar de su crédito.
- Intereses anuales en dólares que paga al banco: 1,000,000 × 5.5 % = **USD 55,000**

| Momento | Nogalera recibe | Nogalera paga |
|---|---:|---:|
| Años 1, 2 y 3 (intereses) | $1,665,000 | USD 55,000 |
| Fin del año 3 (capital) | $18,500,000 | USD 1,000,000 |

Con los pesos que recibe del swap paga su crédito. En la práctica, Nogalera queda con una **deuda en dólares** que cubre con lo que cobra de sus exportaciones.

**4. Sin swap vs. con swap**

| Dólar | USD necesarios para pagar intereses en pesos (cada año) | USD necesarios para pagar el capital |
|---:|---:|---:|
| 17.50 | 95,142.86 | 1,057,142.86 |
| 18.50 | 90,000.00 | 1,000,000.00 |
| 20.00 | 83,250.00 | 925,000.00 |

Sin swap, si el peso se aprecia (dólar a 17.50) Nogalera necesita más dólares de sus ventas para pagar la misma deuda en pesos. Con el swap, sus pagos quedan fijos en **USD 55,000 al año y USD 1,000,000 al final**, sin importar el tipo de cambio. Pagar en la moneda en que se cobra elimina el riesgo cambiario.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT.

```
Actúa como especialista en derivados y tesorería corporativa. Explica de
forma sencilla, para un estudiante de licenciatura en Comercio Exterior.

Parte A. Una empresa tiene un crédito de $10,000,000 a 3 años a TIIE de
Fondeo + 2.00 puntos, con un pago de intereses al año. Contrata un swap en
el que paga 7.80 % fijo y recibe TIIE de Fondeo sobre el mismo nocional.
La TIIE de Fondeo resulta: año 1 = 7.25 %, año 2 = 8.50 %, año 3 = 9.75 %.
1. Haz una tabla por año con los intereses del crédito, lo que paga y
   recibe en el swap, el pago neto y el costo total.
2. Explica qué tasa paga realmente la empresa y por qué.

Parte B. La misma empresa cobra en dólares y tiene un crédito de
$18,500,000 a 9.00 % fijo, que pagará en una sola exhibición al final de 3
años. Contrata un swap de divisas a 18.50 MXN/USD en el que recibe pesos al
9.00 % y paga dólares al 5.50 %.
3. Calcula el nocional en dólares y los flujos anuales y finales en cada
   moneda.
4. Compara cuántos dólares necesitaría para pagar su deuda sin swap si el
   dólar está en 17.50, 18.50 y 20.00.

Además, explica brevemente qué es la TIIE de Fondeo y por qué sustituyó a la
TIIE a 28 días en los contratos nuevos. Muestra cada cálculo.
```

**Documentos a adjuntar:** ninguno.

## Recursos adicionales

- Banco de México: TIIE de Fondeo (publicación diaria) y documentos sobre la transición de la TIIE a plazos a la TIIE de Fondeo.
- Lectura sugerida: capítulo de swaps en el libro de texto de finanzas internacionales del curso.
