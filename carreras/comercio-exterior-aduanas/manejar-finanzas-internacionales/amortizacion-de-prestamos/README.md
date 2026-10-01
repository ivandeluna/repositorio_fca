# Amortización de Préstamos

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Manejar Finanzas Internacionales
**Tema:** Amortización
**Nivel:** Intermedio
**Duración estimada:** 55 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá construir una tabla de amortización con el sistema francés (pago constante), calcular el saldo insoluto, el interés y el capital correspondientes a un mes específico del crédito, y evaluar el efecto financiero de un pago anticipado a capital (ahorro en intereses y reducción del plazo).

## Teoría

> Nota de transparencia: la explicación teórica fue redactada por el profesor y ampliada/pulida con apoyo de IA; las fórmulas y la interpretación financiera son responsabilidad del profesor.

En comercio exterior es común financiar inventario, maquinaria o capital de trabajo en moneda extranjera mediante créditos que se liquidan en pagos periódicos iguales — el llamado **sistema de amortización francés**. Este sistema calcula un pago fijo que combina capital e interés, de modo que al inicio del crédito el pago se compone principalmente de interés, y conforme avanza el plazo, de más capital.

**Fórmula del pago constante (anualidad):**

```
A = P · i / (1 − (1 + i)^−n)
```

Donde:
- `A` = pago periódico constante
- `P` = monto principal del préstamo
- `i` = tasa de interés periódica (tasa anual ÷ número de periodos por año)
- `n` = número total de periodos

**Para cada periodo, la tabla de amortización se construye así:**

- Interés del periodo = saldo insoluto inicial × `i`
- Capital del periodo = `A` − interés del periodo
- Saldo insoluto final = saldo insoluto inicial − capital del periodo

**Pago anticipado a capital (prepayment):** cuando el acreditado abona una cantidad extra directamente a capital (sin que cuente como pago regular), el saldo insoluto baja de inmediato. Esto tiene dos efectos posibles que el acreditado puede elegir:

1. **Mantener el mismo pago mensual y reducir el plazo** (el crédito se liquida en menos periodos).
2. **Mantener el mismo plazo y reducir el pago mensual** (se recalcula un pago menor para los periodos restantes).

En ambos casos, el abono anticipado reduce el interés total pagado durante la vida del crédito, porque el interés de cada periodo se calcula sobre un saldo insoluto menor.

## Ejercicio / caso práctico

Una empresa importadora solicita un préstamo bancario de **$500,000 MXN** para financiar la compra de mercancía de un proveedor en el extranjero. El banco ofrece una tasa de interés anual del **18%**, a pagar en **12 pagos mensuales iguales** bajo el sistema francés.

Se pide:

1. Calcular el pago mensual constante (`A`).
2. Construir la tabla de amortización completa (12 meses): saldo inicial, interés, capital y saldo final de cada mes.
3. Identificar específicamente, para el **mes 6**: el saldo insoluto inicial, el interés y el capital de ese pago, y el saldo final tras ese pago.
4. Suponer que, justo después de realizar el pago normal del mes 6, la empresa hace un **pago anticipado (prepayment) de $50,000** directamente a capital. Si la empresa decide **mantener el mismo pago mensual** (~$45,840) para los meses restantes, ¿en cuántos meses adicionales terminará de liquidar el crédito, y cuánto ahorra en intereses totales respecto al plan original a 12 meses?

## Solución / guía de solución

**1. Pago mensual constante**

Con `P = 500,000`, tasa mensual `i = 18%/12 = 1.5%` y `n = 12`:

```
A = 500,000 × 0.015 / (1 − (1.015)^−12) = $45,840.00
```

**2. Tabla de amortización completa**

| Mes | Saldo inicial | Interés | Capital | Saldo final |
|---|---|---|---|---|
| 1 | 500,000.00 | 7,500.00 | 38,340.00 | 461,660.00 |
| 2 | 461,660.00 | 6,924.90 | 38,915.10 | 422,744.91 |
| 3 | 422,744.91 | 6,341.17 | 39,498.82 | 383,246.08 |
| 4 | 383,246.08 | 5,748.69 | 40,091.31 | 343,154.78 |
| 5 | 343,154.78 | 5,147.32 | 40,692.67 | 302,462.10 |
| 6 | 302,462.10 | 4,536.93 | 41,303.06 | 261,159.04 |
| 7 | 261,159.04 | 3,917.39 | 41,922.61 | 219,236.43 |
| 8 | 219,236.43 | 3,288.55 | 42,551.45 | 176,684.98 |
| 9 | 176,684.98 | 2,650.27 | 43,189.72 | 133,495.26 |
| 10 | 133,495.26 | 2,002.43 | 43,837.57 | 89,657.69 |
| 11 | 89,657.69 | 1,344.87 | 44,495.13 | 45,162.56 |
| 12 | 45,162.56 | 677.44 | 45,162.56 | 0.00 |

Interés total pagado en el plan original (12 meses, sin pago anticipado): **$50,079.96**.

**3. Mes 6 específicamente**

- Saldo insoluto inicial: **$302,462.10**
- Interés del mes 6: **$4,536.93**
- Capital del mes 6: **$41,303.06**
- Saldo final tras el pago normal del mes 6: **$261,159.04**

**4. Pago anticipado de $50,000 tras el mes 6**

Nuevo saldo insoluto inmediatamente después del abono extra:

```
261,159.04 − 50,000 = $211,159.04
```

Manteniendo el mismo pago mensual (~$45,840.00), la nueva tabla para los meses restantes queda:

| Mes adicional | Saldo inicial | Interés | Capital | Pago | Saldo final |
|---|---|---|---|---|---|
| 1 | 211,159.04 | 3,167.39 | 42,672.61 | 45,840.00 | 168,486.43 |
| 2 | 168,486.43 | 2,527.30 | 43,312.70 | 45,840.00 | 125,173.73 |
| 3 | 125,173.73 | 1,877.61 | 43,962.39 | 45,840.00 | 81,211.34 |
| 4 | 81,211.34 | 1,218.17 | 44,621.83 | 45,840.00 | 36,589.51 |
| 5 | 36,589.51 | 548.84 | 36,589.51 | 37,138.35 | 0.00 |

El crédito se liquida en **5 meses adicionales** (en lugar de los 6 meses que faltaban originalmente), con un último pago ajustado de $37,138.35.

**Interés total pagado con el abono anticipado:** intereses de los meses 1–6 ($36,199.02) + intereses de los 5 meses adicionales ($9,339.30) = **$45,538.32**.

**Ahorro en intereses frente al plan original:** $50,079.96 − $45,538.32 = **$4,541.64**, además de liquidar el crédito un mes antes.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

```
Actúa como un asesor financiero especializado en comercio exterior. Tengo un préstamo de $500,000 MXN a 12 meses, con tasa de interés anual del 18%, bajo el sistema de amortización francés (pago mensual constante).

1. Calcula el pago mensual constante.
2. Construye la tabla de amortización completa (12 meses), mostrando para cada mes: saldo inicial, interés, capital y saldo final.
3. Indica específicamente el saldo inicial, interés, capital y saldo final del mes 6.
4. Si justo después del pago del mes 6 hago un pago anticipado de $50,000 directamente a capital y decido mantener el mismo pago mensual para los meses restantes, ¿en cuántos meses adicionales termino de pagar el crédito? ¿Cuánto ahorro en intereses totales comparado con el plan original a 12 meses?

Muestra el procedimiento y las fórmulas utilizadas, no solo el resultado final.
```

**Documentos a adjuntar:** Ninguno — todos los datos del caso (monto, tasa, plazo, monto del pago anticipado) caben en el prompt.

## Recursos adicionales

- Plantilla de Excel para tabla de amortización con función `PAGO`/`PMT` y fórmulas de interés/capital por periodo.
- Lectura sugerida: conceptos de valor del dinero en el tiempo y anualidades ordinarias aplicadas a financiamiento de comercio internacional.
