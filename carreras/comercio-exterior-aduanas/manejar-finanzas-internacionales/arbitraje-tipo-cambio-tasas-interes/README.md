# Arbitraje con Tipo de Cambio y Diferencial de Tasas de Interés

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Paridad de tasas de interés cubierta (arbitraje de interés cubierto)
**Nivel:** Introductorio
**Duración estimada:** 40 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el tipo de cambio forward teórico según la paridad de tasas de interés cubierta, comparar el resultado con un tipo de cambio forward de mercado para identificar oportunidades de arbitraje, y calcular la ganancia libre de riesgo de una operación de arbitraje de interés cubierto.

## Teoría

> *Nota de transparencia: esta sección se redactó con apoyo de IA a partir del lineamiento temático del profesor. Revisar y ajustar antes de usar en clase.*

Cuando dos países tienen tasas de interés distintas, existe un incentivo para mover capital hacia la moneda que paga más. Sin embargo, ese movimiento implica un riesgo cambiario: el inversionista debe convertir su dinero a la otra moneda hoy y de regreso en el futuro. El **arbitraje de interés cubierto** ("covered interest arbitrage") elimina ese riesgo usando un **contrato forward** que fija hoy el tipo de cambio al que se hará la conversión futura.

La **Paridad de Tasas de Interés Cubierta** (PTIC) establece que, en un mercado sin fricciones ni oportunidades de arbitraje, el tipo de cambio forward debe reflejar exactamente el diferencial de tasas de interés entre las dos monedas:

$$F = S \times \frac{(1 + i_{nacional})}{(1 + i_{extranjera})}$$

Donde:
- **S** = tipo de cambio spot (al contado), expresado como unidades de moneda nacional por unidad de moneda extranjera.
- **F** = tipo de cambio forward teórico para el mismo par de monedas, al mismo plazo del diferencial de tasas.
- **i_nacional / i_extranjera** = tasas de interés (para el mismo plazo) en cada país.

**¿Qué pasa si el forward de mercado no coincide con el forward teórico?**

Si el tipo de cambio forward que cotiza el mercado (F_mercado) es distinto al que predice la fórmula (F_teórico), existe una oportunidad de **arbitraje libre de riesgo**: un inversionista puede pedir prestado en la moneda "cara" (la que ofrece rendimiento efectivo insuficiente frente al forward), convertir al spot, invertir en la moneda que rinde más en términos cubiertos, y usar el forward para fijar la reconversión futura — obteniendo una ganancia garantizada sin exposición cambiaria.

Los cuatro pasos del arbitraje de interés cubierto son:

1. **Pedir prestado** en la moneda A a su tasa de interés.
2. **Convertir** el préstamo a la moneda B al tipo de cambio spot.
3. **Invertir** ese monto en la moneda B a su tasa de interés.
4. **Cubrir** con un contrato forward la conversión de regreso a la moneda A, y comparar el monto obtenido contra lo que se debe pagar del préstamo original.

Si lo obtenido en el paso 4 es mayor a la deuda del paso 1, existe una ganancia de arbitraje libre de riesgo. En la práctica, estas oportunidades tienden a cerrarse muy rápido: en cuanto varios inversionistas las aprovechan, la presión de compra/venta ajusta el spot, el forward y hasta las tasas de interés hasta que la paridad se restablece.

## Ejercicio / caso práctico

Un tesorero de una empresa exportadora en Comercio Exterior observa las siguientes condiciones de mercado para el par **MXN/USD** a un plazo de **1 año**:

| Dato | Valor |
|---|---:|
| Tipo de cambio spot (S) | 20.00 MXN/USD |
| Tipo de cambio forward a 1 año cotizado por el banco (F mercado) | 20.80 MXN/USD |
| Tasa de interés anual en México (i MXN) | 10.0% |
| Tasa de interés anual en Estados Unidos (i USD) | 4.0% |
| Capital disponible para la operación | USD $1,000,000 |

**Se pide:**

1. Calcular el tipo de cambio forward teórico según la Paridad de Tasas de Interés Cubierta.
2. Comparar el forward teórico contra el forward de mercado. ¿Existe oportunidad de arbitraje? ¿En qué moneda conviene pedir prestado y en cuál invertir?
3. Con el capital disponible (USD $1,000,000 o su equivalente en MXN), calcular la ganancia libre de riesgo de la operación de arbitraje.
4. Explicar, en una o dos líneas, por qué esta oportunidad tiende a desaparecer conforme más participantes la detectan.

## Solución / guía de solución

**1. Forward teórico (PTIC):**

F_teórico = 20.00 × (1.10 / 1.04) = 20.00 × 1.057692 ≈ **21.1538 MXN/USD**

**2. Comparación y dirección del arbitraje:**

El forward de mercado (20.80) es **menor** al forward teórico (21.1538). Esto significa que el dólar a futuro está "barato" respecto a lo que justifica el diferencial de tasas: conviene **pedir prestado en USD** (la moneda que, cubierta, rinde menos de lo necesario) e **invertir en MXN** (la moneda de mayor tasa), cubriendo el regreso a dólares con el forward de mercado.

**3. Cálculo de la ganancia (capital: USD $1,000,000):**

| Paso | Operación | Resultado |
|---|---|---:|
| 1. Pedir prestado | USD 1,000,000 a 4.0% anual → se debe en 1 año | USD 1,040,000 |
| 2. Convertir a spot | USD 1,000,000 × 20.00 MXN/USD | MXN 20,000,000 |
| 3. Invertir en MXN | MXN 20,000,000 a 10.0% anual → en 1 año | MXN 22,000,000 |
| 4. Cubrir con forward | Comprar USD 1,040,000 (para pagar el préstamo) al forward de 20.80 | Costo: MXN 21,632,000 |
| **Ganancia neta** | MXN 22,000,000 − MXN 21,632,000 | **MXN 368,000** |

Esa ganancia de **MXN $368,000** (equivalente a unos **USD $17,692** al tipo de cambio forward) es libre de riesgo: el monto a pagar del préstamo en dólares ya quedó cubierto con el forward desde el día de la operación, sin importar qué pase después con el tipo de cambio.

**4. Por qué desaparece la oportunidad:**

En cuanto varios participantes del mercado replican esta operación (piden prestado en USD, compran MXN al spot, y compran USD a futuro), aumenta la demanda de MXN al contado y la demanda de USD forward — presionando el spot a la baja, el forward al alza, y/o las tasas de interés a ajustarse — hasta que el forward de mercado vuelve a igualar al forward teórico y la oportunidad de arbitraje se cierra.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por las condiciones de mercado que quieras analizar.

```
Actúa como un especialista en finanzas internacionales y mercados de divisas.
Con los siguientes datos de mercado para el par MXN/USD a 1 año:

- Tipo de cambio spot (S): 20.00 MXN/USD
- Tipo de cambio forward a 1 año cotizado por el banco (F mercado): 20.80 MXN/USD
- Tasa de interés anual en México: 10.0%
- Tasa de interés anual en Estados Unidos: 4.0%
- Capital disponible: USD $1,000,000

1. Calcula el tipo de cambio forward teórico según la Paridad de Tasas de
   Interés Cubierta (Covered Interest Rate Parity).
2. Compara el forward teórico contra el forward de mercado y determina si
   existe una oportunidad de arbitraje de interés cubierto, indicando en qué
   moneda conviene pedir prestado y en cuál invertir.
3. Calcula, paso a paso, la ganancia libre de riesgo de la operación usando
   el capital disponible.
4. Explica en un par de líneas por qué esta oportunidad tiende a desaparecer
   conforme más participantes la detectan.

Muestra el desarrollo completo de cada paso, no solo el resultado final.
```

**Documentos a adjuntar:** ninguno es indispensable, ya que los datos de mercado (spot, forward y tasas de interés) se pueden pegar directamente en el prompt. Si se quiere trabajar con una cotización real en lugar del caso de ejemplo, se sugiere adjuntar una captura o tabla con los tipos de cambio y tasas vigentes de una fuente como Banxico, la Reserva Federal (Fed) o un banco comercial.

## Recursos adicionales

- Plantilla de cálculo en Excel: *(por agregar)*
- Lectura sugerida: capítulo de mercados de divisas y paridad de tasas de interés en el libro de texto del curso.
