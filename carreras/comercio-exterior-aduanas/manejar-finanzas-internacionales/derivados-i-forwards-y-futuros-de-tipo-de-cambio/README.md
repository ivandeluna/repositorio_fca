# Derivados I: forwards y futuros de tipo de cambio

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Derivados: futuros y forwards
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular un tipo de cambio forward a partir de las tasas de interés de México y de EE. UU., comparar el resultado de un exportador con y sin cobertura, y explicar las diferencias entre un forward bancario y un futuro del dólar en MexDer, incluida la liquidación diaria de pérdidas y ganancias.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

Un **derivado** es un contrato cuyo valor depende de otra cosa, llamada **subyacente**: el tipo de cambio, una tasa de interés, una acción o una materia prima. En comercio exterior se usan sobre todo para **cubrirse** (protegerse) del riesgo de que el tipo de cambio se mueva en contra.

**Forward.** Es un acuerdo privado, normalmente con un banco, para comprar o vender una cantidad de dólares en una fecha futura a un precio que se fija **hoy**. Se hace a la medida (monto y fecha exactos), no cuesta nada al firmarlo y se liquida al vencimiento.

**Futuro.** Es lo mismo en esencia, pero se negocia en una bolsa de derivados, que en México es **MexDer**. Sus diferencias:

| Característica | Forward | Futuro (MexDer) |
|---|---|---|
| Dónde se negocia | Directo con un banco | En bolsa (MexDer) |
| Monto | A la medida | Estandarizado: 10,000 USD por contrato (también hay un "mini" de 1,000 USD) |
| Fecha | Cualquiera | Fechas fijas de vencimiento |
| Garantía | Línea de crédito con el banco | **Aportación inicial mínima** (margen) en una cámara de compensación |
| Pérdidas y ganancias | Solo al vencimiento | **Todos los días** (liquidación diaria) |
| Riesgo de que la otra parte no pague | Sí | Casi nulo: la cámara de compensación garantiza |

**¿Cómo se calcula el tipo de cambio forward?** Por la **paridad de tasas de interés**: el forward compensa la diferencia de tasas entre México y EE. UU. Como en México la tasa es más alta, el dólar a futuro cuesta más que hoy.

F = S × (1 + i_MXN × t / 360) / (1 + i_USD × t / 360)

**¿Quién compra y quién vende?**

- El **exportador** va a **recibir** dólares y teme que el dólar baje: **vende** dólares a futuro.
- El **importador** va a **pagar** dólares y teme que el dólar suba: **compra** dólares a futuro.

Cubrirse elimina el riesgo pero también la posible ganancia: si el dólar sube, el exportador cubierto no aprovecha el alza. El objetivo de la cobertura es **tener certeza**, no ganar.

**Derivados de tasa de interés.** Con la misma lógica existen forwards y futuros sobre tasas de interés (MexDer también lista futuros de tasas), que permiten fijar hoy la tasa de un crédito o una inversión futura.

## Ejercicio / caso práctico

**Nogalera del Nazas, S.A. de C.V.** vendió nuez a un cliente de Texas y cobrará **USD 200,000 dentro de 90 días**. Sus costos están en pesos, y el director de finanzas quiere saber hoy cuántos pesos recibirá.

**Datos de mercado (ilustrativos, no son cotizaciones reales):**

| Dato | Valor |
|---|---:|
| Tipo de cambio spot hoy | 18.50 MXN/USD |
| Tasa en pesos a 90 días | 7.50 % anual |
| Tasa en dólares a 90 días | 4.00 % anual |
| Contrato de futuro del dólar en MexDer | 10,000 USD |
| Precio del futuro en los siguientes 3 días | 18.70, 18.55, 18.80 |

**Se pide:**

1. **Forward.** Calcula el tipo de cambio forward a 90 días. ¿Nogalera debe comprar o vender dólares a futuro?
2. **Escenarios.** Calcula cuántos pesos recibe con y sin forward si en 90 días el dólar está en 17.50, 18.50 o 19.50. ¿En qué escenario se "arrepiente" de haberse cubierto? ¿Fue mala decisión?
3. **Futuros.** Si en lugar del forward usa futuros de MexDer, ¿cuántos contratos necesita? Suponiendo que los vende al precio del forward, calcula la pérdida o ganancia diaria de los primeros 3 días y la acumulada.
4. **Comparación.** Menciona dos ventajas y dos desventajas del futuro frente al forward para una empresa como Nogalera.
5. **Datos reales con IA.** Pide a la IA que calcule el forward a 90 días con el tipo de cambio FIX y las tasas actuales, y compáralo con la cotización de un banco o de MexDer.

## Solución / guía de solución

**1. Forward a 90 días**

F = 18.50 × (1 + 0.075 × 90 / 360) / (1 + 0.04 × 90 / 360) = 18.50 × 1.01875 / 1.01 = **18.6603 MXN/USD**

Nogalera va a recibir dólares, así que **vende dólares a futuro** a 18.6603.

**2. Escenarios a 90 días (USD 200,000)**

| Dólar en 90 días | Sin cobertura | Con forward | Diferencia a favor del forward |
|---:|---:|---:|---:|
| 17.50 | 3,500,000 | 3,732,060 | +232,060 |
| 18.50 | 3,700,000 | 3,732,060 | +32,060 |
| 19.50 | 3,900,000 | 3,732,060 | −167,940 |

Con el forward, Nogalera sabe desde hoy que recibirá **$3,732,060** pase lo que pase. Si el dólar sube a 19.50 "deja de ganar" $167,940, pero no fue una mala decisión: cuando firmó el contrato no sabía qué iba a pasar y eligió certeza, que es justo para lo que sirve la cobertura.

**3. Futuros en MexDer**

- Contratos: 200,000 / 10,000 = **20 contratos**, en posición **corta** (vendedora).
- Una posición corta gana cuando el precio baja y pierde cuando sube. Por día: (precio anterior − precio nuevo) × 10,000 × 20.

| Día | Precio del futuro | Pérdida o ganancia del día | Acumulado |
|---:|---:|---:|---:|
| 0 (venta) | 18.6603 | — | — |
| 1 | 18.70 | −7,940 | −7,940 |
| 2 | 18.55 | +30,000 | +22,060 |
| 3 | 18.80 | −50,000 | −27,940 |

Las pérdidas se cargan cada día a la cuenta de margen. Si el saldo baja del mínimo, la empresa debe depositar más dinero (**llamada de margen**). Al vencimiento, la suma de todas las liquidaciones más la venta de los dólares al spot da el mismo resultado que el forward. La diferencia está en el **flujo de efectivo** durante el camino.

**4. Comparación (respuesta abierta)**

- Ventajas del futuro: casi no hay riesgo de que la contraparte incumpla; precios públicos y transparentes; se puede cerrar la posición antes del vencimiento.
- Desventajas: montos y fechas fijos (USD 200,000 cuadra exacto, pero USD 205,000 no); exige depositar margen y aguantar pérdidas diarias en efectivo; requiere abrir cuenta con un operador de MexDer.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT. Cambia los datos por los actuales si quieres trabajar con el mercado real.

```
Actúa como especialista en coberturas cambiarias para empresas de comercio
exterior. Explica de forma sencilla, para un estudiante de licenciatura.

Una empresa exportadora mexicana cobrará USD 200,000 dentro de 90 días.
Datos (si puedes, consulta los valores actuales y cita la fuente; si no,
usa estos):
- Tipo de cambio spot: [18.50] MXN/USD
- Tasa en pesos a 90 días: [7.50 %] anual
- Tasa en dólares a 90 días: [4.00 %] anual

1. Calcula el tipo de cambio forward a 90 días con la paridad de tasas de
   interés (año de 360 días) e indica si la empresa debe comprar o vender
   dólares a futuro.
2. Haz una tabla con los pesos recibidos con y sin forward si en 90 días el
   dólar está en 17.50, 18.50 y 19.50.
3. Explica cuántos contratos de futuro del dólar de MexDer (10,000 USD cada
   uno) necesitaría y simula la liquidación diaria de una posición corta si
   el precio del futuro va a 18.70, 18.55 y 18.80 en tres días.
4. Compara forward y futuro en una tabla de ventajas y desventajas.

Muestra cada fórmula con los números sustituidos.
```

**Documentos a adjuntar:** ninguno.

## Recursos adicionales

- MexDer, Mercado Mexicano de Derivados (mexder.com.mx): especificaciones del contrato de futuro del dólar y del mini futuro del dólar.
- Banco de México: tipo de cambio FIX y tasas de interés de referencia.
