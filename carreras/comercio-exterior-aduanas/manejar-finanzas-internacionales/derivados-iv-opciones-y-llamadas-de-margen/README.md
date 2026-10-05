# Derivados IV: opciones y llamadas de margen

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Derivados: opciones y llamadas de margen
**Nivel:** Intermedio
**Duración estimada:** 45 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá armar una cobertura de "costo cero" (collar) con opciones sobre el dólar, explicar por qué quien vende una opción debe depositar garantías y quien la compra no, llevar la cuenta de margen de una posición vendida día por día identificando las llamadas de margen, y evaluar el riesgo de liquidez que implica para una empresa exportadora.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

**Comprar vs. vender una opción.** En el ejercicio de opciones, Nogalera *compraba* opciones: pagaba la prima y, como mucho, perdía esa prima. Quien está del otro lado, el que *vende* (o "emite") la opción, cobra la prima, pero se obliga a cumplir si el comprador la ejerce. Su pérdida puede ser muy grande.

| | Comprador de la opción | Vendedor de la opción |
|---|---|---|
| Prima | La paga | La cobra |
| Derecho u obligación | Derecho | **Obligación** |
| Pérdida máxima | La prima | Muy grande (en un call vendido, sin límite) |
| ¿Deposita garantías? | No | **Sí** |

**Collar o cobertura de "costo cero".** Una empresa exportadora que quiere un piso para su tipo de cambio puede comprar un **put**. Para no pagar la prima, vende al mismo tiempo un **call** con un precio de ejercicio más alto y usa la prima que cobra para pagar la del put. El resultado es un **rango**: el tipo de cambio efectivo nunca queda abajo del piso (el put) ni arriba del techo (el call). A cambio de no pagar prima, renuncia a la ganancia si el dólar sube mucho.

**Garantías y llamadas de margen.** En los mercados organizados, como MexDer, una **cámara de compensación** se pone en medio de cada operación y garantiza que todos cumplan. Para protegerse, a quien tiene una posición con riesgo de pérdida (por ejemplo, un call vendido) le exige:

- **Margen inicial** (aportación inicial mínima): un depósito al abrir la posición.
- **Valuación diaria:** cada día la posición se valúa a precio de mercado. Si el precio de la opción vendida sube, la pérdida del día se descuenta de la cuenta de margen; si baja, la ganancia se abona.
- **Margen de mantenimiento:** el saldo mínimo que debe tener la cuenta.
- **Llamada de margen:** si el saldo cae por debajo del mantenimiento, la cámara exige depositar, normalmente al día siguiente, lo necesario para regresar al margen inicial. Si no se deposita, **cierra la posición** y la pérdida se vuelve definitiva.

En los contratos con bancos (fuera de bolsa) pasa algo parecido: el banco puede pedir garantías adicionales cuando la posición pierde valor.

**El riesgo de liquidez.** Para un exportador, la pérdida del call vendido cuando sube el dólar se compensa con más pesos por sus ventas. El problema es el **momento**: las llamadas de margen se pagan *hoy*, en efectivo, y los dólares del cliente llegan *después*. Una cobertura correcta en el papel puede llevar a una empresa a quedarse sin efectivo. En octubre de 2008, cuando el peso se depreció bruscamente, varias empresas mexicanas sufrieron pérdidas muy grandes con derivados cambiarios. El caso más conocido es el de Controladora Comercial Mexicana, que terminó en concurso mercantil.

## Ejercicio / caso práctico

**Nogalera del Nazas, S.A. de C.V.** cobrará **USD 200,000 dentro de 90 días** por una exportación de nuez. Quiere protegerse de que el dólar baje, pero no quiere pagar prima, así que arma un collar con opciones listadas en bolsa (contratos de 10,000 USD):

**Datos (ilustrativos, no son cotizaciones reales):**

| Dato | Valor |
|---|---:|
| Tipo de cambio spot hoy | 18.50 MXN/USD |
| **Compra** put a 90 días: precio de ejercicio / prima | 18.30 / 0.25 MXN por dólar |
| **Vende** call a 90 días: precio de ejercicio / prima | 19.20 / 0.25 MXN por dólar |
| Número de contratos de cada opción | 20 (20 × 10,000 = USD 200,000) |
| Margen inicial por el call vendido | $6,000 por contrato |
| Margen de mantenimiento | $4,800 por contrato |
| Regla de llamada de margen | Si el saldo baja del mantenimiento, se deposita lo necesario para volver al margen inicial |

**Evolución de los primeros 5 días hábiles:**

| Día | Tipo de cambio spot | Precio (prima) del call 19.20 |
|---:|---:|---:|
| 0 (apertura) | 18.50 | 0.25 |
| 1 | 18.55 | 0.32 |
| 2 | 18.75 | 0.45 |
| 3 | 19.00 | 0.70 |
| 4 | 18.85 | 0.55 |
| 5 | 19.30 | 0.95 |

**Se pide:**

1. **El collar.** ¿Cuánto paga Nogalera de prima neta? Calcula el tipo de cambio efectivo y los pesos que recibe al vencimiento si el dólar termina en 17.50, 18.30, 18.80, 19.20, 19.80 o 20.50. Compara con no cubrirse.
2. **¿Quién deposita?** Explica por qué Nogalera debe depositar margen por el call vendido pero no por el put comprado.
3. **Cuenta de margen.** Calcula el margen inicial y el de mantenimiento de la posición. Después, día por día, calcula la pérdida o ganancia del call vendido, el saldo de la cuenta y si hay llamada de margen y de cuánto.
4. **Liquidez.** ¿Cuánto efectivo en total tuvo que depositar Nogalera en estos 5 días? ¿De dónde lo saca si los dólares del cliente llegan hasta el día 90? ¿Qué pasaría si no deposita?
5. **¿Fue mala la cobertura?** Si al día 90 el dólar está en 19.80, ¿cuánto recibe Nogalera en total contando el collar? ¿La pérdida en el call significa que la cobertura falló?
6. **Caso real con IA.** Pide a la IA que te explique qué le pasó a Controladora Comercial Mexicana con sus derivados en 2008 y verifica los datos principales en al menos una fuente periodística o en los reportes de la empresa a la BMV.

## Solución / guía de solución

**1. El collar**

- Prima neta = prima del put pagada − prima del call cobrada = (0.25 − 0.25) × 200,000 = **$0**: costo cero.
- Tipo de cambio efectivo = el spot, pero nunca menor a 18.30 ni mayor a 19.20.

| Dólar al día 90 | Put (comprado) | Call (vendido) | TC efectivo | Pesos con collar | Pesos sin cobertura |
|---:|---|---|---:|---:|---:|
| 17.50 | Nogalera lo ejerce | No se ejerce | 18.30 | 3,660,000 | 3,500,000 |
| 18.30 | Indiferente | No se ejerce | 18.30 | 3,660,000 | 3,660,000 |
| 18.80 | No se ejerce | No se ejerce | 18.80 | 3,760,000 | 3,760,000 |
| 19.20 | No se ejerce | Indiferente | 19.20 | 3,840,000 | 3,840,000 |
| 19.80 | No se ejerce | Se lo ejercen | 19.20 | 3,840,000 | 3,960,000 |
| 20.50 | No se ejerce | Se lo ejercen | 19.20 | 3,840,000 | 4,100,000 |

Nogalera queda asegurada entre **$3,660,000 y $3,840,000**.

**2. ¿Quién deposita?**

Con el put comprado, Nogalera ya pagó todo lo que podía perder (la prima) y solo tiene derechos. Con el call vendido tiene una **obligación**: si el dólar sube, debe vender dólares a 19.20 aunque valgan más. La cámara de compensación le pide garantías para asegurarse de que cumpla.

**3. Cuenta de margen**

- Margen inicial = 6,000 × 20 = **$120,000**. Mantenimiento = 4,800 × 20 = **$96,000**.
- Pérdida o ganancia diaria del call vendido = −(prima de hoy − prima de ayer) × 200,000. Si la prima sube, el vendedor pierde.

| Día | Prima del call | Pérdida o ganancia | Saldo antes de la llamada | ¿Llamada de margen? | Depósito | Saldo final |
|---:|---:|---:|---:|---|---:|---:|
| 0 | 0.25 | — | — | — | 120,000 (inicial) | 120,000 |
| 1 | 0.32 | −14,000 | 106,000 | No (arriba de 96,000) | — | 106,000 |
| 2 | 0.45 | −26,000 | 80,000 | **Sí** | 40,000 | 120,000 |
| 3 | 0.70 | −50,000 | 70,000 | **Sí** | 50,000 | 120,000 |
| 4 | 0.55 | +30,000 | 150,000 | No | — | 150,000 |
| 5 | 0.95 | −80,000 | 70,000 | **Sí** | 50,000 | 120,000 |

**4. Liquidez**

- En 5 días Nogalera aportó **$260,000** en efectivo: $120,000 de margen inicial y $140,000 en tres llamadas de margen. Eso es cerca del 7 % de lo que espera recibir por la exportación, y los dólares todavía no llegan.
- Tiene que salir de su caja o de una línea de crédito. Si no deposita, la cámara cierra el call a 0.95 y la pérdida de $140,000 se vuelve definitiva, pero Nogalera **se queda con el put y sin el call**: ya no tiene un collar.
- Lección: antes de vender opciones o contratar derivados con garantías, la empresa debe calcular cuánta liquidez necesitaría en un escenario adverso y tener esos recursos disponibles.

**5. ¿Fue mala la cobertura?**

Con el dólar en 19.80, el call se ejerce: Nogalera pierde (19.80 − 19.20) × 200,000 = $120,000 en el call, pero vende sus dólares a 19.80 y recibe $3,960,000. Neto: 3,960,000 − 120,000 = **$3,840,000**, exactamente el techo del collar. La cobertura funcionó como se diseñó. Lo que "pierde" es la ganancia a la que renunció a cambio de no pagar prima. Las llamadas de margen fueron adelantos de esa misma pérdida, no un costo adicional (sin contar el costo financiero de adelantar el efectivo).

**6. Caso real (respuesta abierta)**

Puntos que el alumno debería encontrar y verificar: en 2008 la empresa tenía contratos de derivados cambiarios de un monto mucho mayor que su exposición real en dólares; la fuerte depreciación del peso en octubre de 2008 generó pérdidas y exigencias de garantías que no pudo cubrir; terminó en concurso mercantil y en una reestructura de su deuda. La diferencia con Nogalera: **cubrir una exposición real** frente a **especular con montos mayores** que esa exposición.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT.

```
Actúa como especialista en derivados y gestión de riesgos para empresas de
comercio exterior. Explica de forma sencilla, para un estudiante de
licenciatura.

Una empresa exportadora mexicana cobrará USD 200,000 en 90 días. Arma un
collar de costo cero con opciones listadas (contratos de 10,000 USD):
compra 20 puts con precio de ejercicio 18.30 (prima 0.25 MXN por USD) y
vende 20 calls con precio de ejercicio 19.20 (prima 0.25 MXN por USD).
Spot actual: 18.50 MXN/USD.

Por el call vendido, la cámara de compensación exige un margen inicial de
$6,000 por contrato y un margen de mantenimiento de $4,800 por contrato.
Si el saldo baja del mantenimiento, se deposita lo necesario para volver al
margen inicial.

La prima del call vendido evoluciona así: día 1 = 0.32, día 2 = 0.45,
día 3 = 0.70, día 4 = 0.55, día 5 = 0.95.

1. Calcula la prima neta del collar y una tabla con el tipo de cambio
   efectivo y los pesos recibidos si el dólar termina en 17.50, 18.30,
   18.80, 19.20, 19.80 y 20.50.
2. Explica por qué el vendedor de una opción deposita garantías y el
   comprador no.
3. Haz una tabla día por día de la cuenta de margen: pérdida o ganancia,
   saldo, si hay llamada de margen y el monto a depositar.
4. Calcula el efectivo total aportado y explica el riesgo de liquidez para
   la empresa.
5. Explica brevemente qué le pasó a Controladora Comercial Mexicana con sus
   derivados cambiarios en 2008 y cita tus fuentes.

Muestra cada cálculo con los números sustituidos.
```

**Documentos a adjuntar:** ninguno.

## Recursos adicionales

- MexDer (mexder.com.mx): reglas de aportaciones iniciales mínimas y de la cámara de compensación (Asigna).
- Ejercicios relacionados: *Derivados I: forwards y futuros* (liquidación diaria) y *Derivados II: opciones*.
