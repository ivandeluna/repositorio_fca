# Instrumentos de deuda: Cetes, bonos y tasas de interés

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Instrumentos de deuda
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el precio y el rendimiento de un Cete, comparar una inversión en pesos con una en dólares considerando el tipo de cambio, y explicar por qué el precio de un bono baja cuando suben las tasas de interés.

## Teoría

> *Nota de transparencia: redactado con apoyo de IA a partir del lineamiento temático del profesor; los cálculos se verificaron con código. Revisar antes de usar en clase.*

Un **instrumento de deuda** es un préstamo que el inversionista le hace a un gobierno o a una empresa. A cambio, el emisor promete devolver el dinero en una fecha (el **vencimiento**) y pagar un interés. Los más conocidos en México los emite el Gobierno Federal:

| Instrumento | Moneda | Cómo paga | Plazo típico |
|---|---|---|---|
| **Cetes** (Certificados de la Tesorería) | Pesos | Se compran "a descuento" (por debajo de $10) y al vencimiento pagan $10 | 28, 91, 182 y 364 días, y 2 años |
| **Bonos M** | Pesos | Tasa fija; pagan un cupón cada 6 meses | 3 a 30 años |
| **Udibonos** | UDIS (se ajustan por inflación) | Tasa real fija; protegen contra la inflación | 3 a 30 años |
| **T-Bills / Treasuries** (EE. UU.) | Dólares | Equivalentes a los Cetes y a los bonos en EE. UU. | Semanas a 30 años |

**Precio de un Cete.** Valor nominal de $10, tasa de rendimiento anual *r* y *t* días por vencer (año de 360 días):

Precio = 10 / (1 + r × t / 360)

**Invertir en otra moneda.** Si un inversionista mexicano convierte sus pesos a dólares para invertir en EE. UU., su rendimiento en pesos depende de dos cosas: la tasa en dólares y lo que pase con el tipo de cambio. El **tipo de cambio de equilibrio** es el que hace que ambas inversiones rindan lo mismo:

TC de equilibrio = TC hoy × (1 + i_MXN × t / 360) / (1 + i_USD × t / 360)

Si al vencimiento el dólar cuesta más que ese valor, convino invertir en dólares; si cuesta menos, convino quedarse en pesos.

**Precio de un bono y tasas de interés.** Un bono a tasa fija paga cupones fijos. Su precio es el valor presente de esos pagos:

Precio = Σ cupón / (1 + r)^t + valor nominal / (1 + r)^n

Si las tasas de mercado **suben**, los cupones fijos del bono valen menos en comparación y su precio **baja**. Si las tasas **bajan**, el precio **sube**. Esta es la regla más importante del mercado de deuda.

## Ejercicio / caso práctico

**Nogalera del Nazas, S.A. de C.V.** exporta nuez pecanera desde Torreón a Estados Unidos. Después de la cosecha tiene **$1,000,000 de pesos** que no necesitará durante 91 días y quiere invertirlos sin arriesgarse mucho.

**Datos de mercado (ilustrativos, no son cotizaciones reales):**

| Dato | Valor |
|---|---:|
| Tipo de cambio hoy | 18.50 MXN/USD |
| Tasa de Cetes a 91 días | 7.50 % anual |
| Tasa de T-Bills a 91 días (EE. UU.) | 4.00 % anual |
| Bono a tasa fija: valor nominal $100, cupón anual 8 %, plazo 3 años | — |

**Se pide:**

1. **Cetes.** Calcula el precio de un Cete a 91 días, cuántos títulos puede comprar la empresa con $1,000,000 y cuánto gana al vencimiento.
2. **Pesos o dólares.** Si en lugar de eso convierte el dinero a dólares e invierte en T-Bills, ¿cuántos dólares tendrá al vencimiento? Calcula el tipo de cambio de equilibrio y el resultado en pesos si al vencimiento el dólar está en 18.00, 18.50 o 19.00.
3. **Bonos y tasas.** Calcula el precio del bono si la tasa de mercado es de 7 %, 8 % y 9 %. ¿Qué le pasa al precio cuando la tasa sube?
4. **Datos reales con IA.** Usa el prompt sugerido para repetir los incisos 1 y 2 con la tasa de Cetes y el tipo de cambio FIX actuales. Verifica en la página del Banco de México que la IA haya usado los valores correctos.

## Solución / guía de solución

**1. Cetes**

- Precio = 10 / (1 + 0.075 × 91 / 360) = 10 / 1.018958 = **$9.813944**
- Títulos = 1,000,000 / 9.813944 = **101,895 Cetes** (inversión de $999,991.82)
- Al vencimiento recibe 101,895 × $10 = **$1,018,950.00**, es decir, una ganancia de **$18,958.18** (1.90 % en 91 días, equivalente a 7.50 % anual).

**2. Pesos o dólares**

- Dólares iniciales: 1,000,000 / 18.50 = USD 54,054.05
- Al vencimiento: 54,054.05 × (1 + 0.04 × 91 / 360) = **USD 54,600.60**
- TC de equilibrio = 18.50 × 1.018958 / 1.010111 = **18.6620 MXN/USD**

| Dólar al vencimiento | Pesos recibidos | Ganancia | Rendimiento anualizado | ¿Convino? |
|---:|---:|---:|---:|---|
| 18.00 | 982,810.81 | −17,189.19 | −6.80 % | No, perdió |
| 18.50 | 1,010,111.11 | 10,111.11 | 4.00 % | Menos que Cetes |
| 18.6620 (equilibrio) | 1,018,958.33 | 18,958.33 | 7.50 % | Igual que Cetes |
| 19.00 | 1,037,411.41 | 37,411.41 | 14.80 % | Sí, más que Cetes |

La tasa en pesos es más alta, así que para que la inversión en dólares convenga, el peso se tiene que depreciar más de 18.6620. Invertir en dólares sin cobertura es **apostar al tipo de cambio**.

**3. Bonos y tasas**

| Tasa de mercado | Precio del bono | Lectura |
|---:|---:|---|
| 7 % | $102.62 | La tasa bajó: el cupón de 8 % es atractivo y el bono vale más |
| 8 % | $100.00 | Tasa igual al cupón: se vende "a la par" |
| 9 % | $97.47 | La tasa subió: el bono vale menos |

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT. Si la IA puede buscar en internet, pídele los datos actuales; si no, búscalos tú en Banxico y pégalos en los corchetes.

```
Actúa como asesor de inversiones de tesorería para una empresa exportadora
mexicana. Explica todo de forma sencilla, como para un estudiante de
licenciatura que ve el tema por primera vez.

La empresa tiene $1,000,000 de pesos disponibles durante 91 días.

Datos (búscalos en fuentes oficiales y cita la fuente y la fecha; si no
puedes consultarlos, usa los que te doy):
- Tipo de cambio FIX de hoy: [18.50] MXN/USD (Banco de México)
- Tasa de Cetes a 91 días de la última subasta: [7.50 %] (Banco de México)
- Tasa de T-Bills a 13 semanas: [4.00 %] (Tesoro de EE. UU.)

1. Calcula el precio de un Cete a 91 días (valor nominal $10, año de 360
   días), cuántos títulos se pueden comprar y la ganancia al vencimiento.
2. Calcula cuántos dólares tendría si invierte en T-Bills y el tipo de
   cambio de equilibrio que iguala ambas inversiones.
3. Muestra en una tabla el resultado en pesos si al vencimiento el dólar
   está 3 % abajo, igual y 3 % arriba del tipo de cambio de hoy.
4. Explica en dos líneas por qué el precio de un bono a tasa fija baja
   cuando suben las tasas de interés.

Muestra cada fórmula con los números sustituidos.
```

**Documentos a adjuntar:** ninguno. Si la IA no puede navegar, copia los valores del día de la página de Banxico y pégalos en el prompt.

## Recursos adicionales

- Banco de México, Sistema de Información Económica (SIE): tipo de cambio FIX y resultados de la subasta de valores gubernamentales.
- cetesdirecto.com: plataforma del gobierno para invertir en Cetes, Bonos y Udibonos desde $100.
