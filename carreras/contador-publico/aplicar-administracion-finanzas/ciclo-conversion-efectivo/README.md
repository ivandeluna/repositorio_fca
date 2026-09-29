# Ciclo de Conversión de Efectivo

**Carrera:** Contador Público
**Materia:** Aplicar Administración de las Finanzas
**Tema:** Administración del capital de trabajo
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el Ciclo de Conversión de Efectivo (CCE) de una empresa a partir de su información financiera, interpretar qué significa el resultado para la liquidez del negocio, y proponer acciones concretas para acortarlo.

## Teoría

> *Nota de transparencia: esta sección se redactó con apoyo de IA a partir del lineamiento temático del profesor. Revisar y ajustar antes de usar en clase.*

El **Ciclo de Conversión de Efectivo** (CCE), también llamado ciclo de caja, mide el tiempo (en días) que transcurre desde que una empresa paga por sus insumos o inventario hasta que cobra el efectivo de la venta de ese inventario a sus clientes. Es uno de los indicadores más usados en la administración del capital de trabajo porque conecta tres áreas operativas clave: inventarios, cuentas por cobrar y cuentas por pagar.

Se calcula combinando tres periodos:

1. **Días de Inventario (DIO — *Days Inventory Outstanding*):** cuántos días, en promedio, permanece el inventario en almacén antes de venderse.

   $$DIO = \frac{Inventario\ promedio}{Costo\ de\ ventas} \times 365$$

2. **Días de Cuentas por Cobrar (DSO — *Days Sales Outstanding*):** cuántos días tarda la empresa en cobrar a sus clientes después de una venta a crédito.

   $$DSO = \frac{Cuentas\ por\ cobrar\ promedio}{Ventas\ a\ crédito} \times 365$$

3. **Días de Cuentas por Pagar (DPO — *Days Payable Outstanding*):** cuántos días tarda la empresa en pagar a sus proveedores.

   $$DPO = \frac{Cuentas\ por\ pagar\ promedio}{Costo\ de\ ventas} \times 365$$

La fórmula del ciclo completo es:

$$CCE = DIO + DSO - DPO$$

**Interpretación:**

- Un **CCE positivo y alto** indica que la empresa tarda mucho en convertir sus inversiones en inventario y cuentas por cobrar de vuelta en efectivo, lo que puede generar presión de liquidez y necesidad de financiamiento externo (capital de trabajo).
- Un **CCE bajo o negativo** (común en empresas como supermercados o retailers grandes) indica que la empresa cobra a sus clientes antes de tener que pagar a sus proveedores, lo que le permite operar con menos capital de trabajo propio.
- Acortar el CCE —vendiendo inventario más rápido, cobrando más rápido, o negociando mejores plazos de pago con proveedores— libera efectivo para la operación sin necesidad de deuda adicional.

## Ejercicio / caso práctico

La empresa **Comercial Laguna, S.A. de C.V.**, dedicada a la venta al mayoreo de artículos de ferretería en Torreón, Coahuila, presenta la siguiente información financiera correspondiente al último ejercicio anual:

| Concepto | Monto (MXN) |
|---|---:|
| Costo de ventas anual | $18,250,000 |
| Ventas anuales a crédito | $24,000,000 |
| Inventario promedio | $2,500,000 |
| Cuentas por cobrar promedio | $2,300,000 |
| Cuentas por pagar promedio | $1,900,000 |

**Se pide:**

1. Calcular el DIO, DSO y DPO de la empresa (usa 365 días).
2. Calcular el Ciclo de Conversión de Efectivo (CCE).
3. Interpretar el resultado: ¿la empresa tiene un ciclo de efectivo sano o representa presión sobre su liquidez?
4. Proponer **dos acciones concretas** que la administración podría tomar para reducir el CCE, indicando sobre cuál de los tres componentes (DIO, DSO o DPO) actuaría cada una.

## Solución / guía de solución

**1. Cálculo de los tres componentes:**

- DIO = (2,500,000 / 18,250,000) × 365 ≈ **50.0 días**
- DSO = (2,300,000 / 24,000,000) × 365 ≈ **35.0 días**
- DPO = (1,900,000 / 18,250,000) × 365 ≈ **38.0 días**

**2. Ciclo de Conversión de Efectivo:**

CCE = 50.0 + 35.0 − 38.0 = **47.0 días**

**3. Interpretación:**

Comercial Laguna tarda, en promedio, 47 días desde que paga sus insumos hasta que recibe el efectivo de sus ventas. Es un ciclo moderado para una empresa de mayoreo, pero significa que la empresa debe financiar casi mes y medio de operación con capital propio o líneas de crédito de corto plazo antes de recuperar el efectivo invertido en cada ciclo de venta.

**4. Ejemplos de acciones (respuesta abierta, guía para el profesor):**

- *Sobre DIO:* mejorar la rotación de inventario con un sistema de reabastecimiento más frecuente y en menores cantidades (reduce inventario promedio inmovilizado).
- *Sobre DSO:* ofrecer descuentos por pronto pago a clientes mayoristas o reforzar la gestión de cobranza (reduce días de cuentas por cobrar).
- *Sobre DPO:* renegociar plazos de pago más largos con proveedores clave, siempre cuidando no dañar la relación comercial ni perder descuentos por pronto pago.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso o empresa.

```
Actúa como un asesor financiero especializado en administración del capital de trabajo.
Con los siguientes datos anuales de una empresa:

- Costo de ventas: $18,250,000
- Ventas a crédito: $24,000,000
- Inventario promedio: $2,500,000
- Cuentas por cobrar promedio: $2,300,000
- Cuentas por pagar promedio: $1,900,000

1. Calcula los Días de Inventario (DIO), Días de Cuentas por Cobrar (DSO) y
   Días de Cuentas por Pagar (DPO), usando 365 días.
2. Calcula el Ciclo de Conversión de Efectivo (CCE).
3. Interpreta el resultado: ¿qué tan sano es el ciclo de efectivo de esta empresa?
4. Propón dos acciones concretas para reducir el CCE, indicando sobre cuál de
   los tres componentes (DIO, DSO o DPO) actuaría cada una.

Muestra el desarrollo paso a paso, no solo el resultado final.
```

**Documentos a adjuntar:** se sugiere agregar el **Estado de Resultados** y el **Balance General** (o al menos el detalle de inventarios, cuentas por cobrar y cuentas por pagar) de la empresa que se quiera analizar, para que la IA calcule los promedios y el CCE a partir de cifras reales en lugar de los datos de ejemplo.

## Recursos adicionales

- Plantilla de cálculo en Excel: *(por agregar — agregar aquí el archivo .xlsx si el profesor prepara uno)*
- Lectura sugerida: capítulo de administración del capital de trabajo en cualquier libro de texto de finanzas corporativas usado en el curso.
