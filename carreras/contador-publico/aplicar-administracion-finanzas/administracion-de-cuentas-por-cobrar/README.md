# Administración de Cuentas por Cobrar

**Carrera:** Contador Público
**Materia:** Aplicar Administración de las Finanzas
**Tema:** Administración de Cuentas por Cobrar
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá evaluar financieramente una propuesta de cambio en la política de crédito (reducción de los días de cuentas por cobrar mediante un descuento por pronto pago), comparando el ahorro en costo de oportunidad de la inversión liberada contra el costo del descuento otorgado, para decidir si la propuesta conviene a la empresa.

## Teoría

> Nota de transparencia: la explicación teórica fue redactada por el profesor y ampliada/pulida con apoyo de IA; el planteamiento del caso y los criterios de decisión son responsabilidad del profesor.

Las **cuentas por cobrar (CxC)** representan el crédito que una empresa otorga a sus clientes al vender a crédito. Mantener cuentas por cobrar implica un **costo de oportunidad**: el dinero invertido en financiar a los clientes no está disponible para otros usos (inversión, reducción de deuda, etc.).

Una métrica clave es el **DSO (Days Sales Outstanding)** o días promedio de cobro, que indica cuántos días, en promedio, tarda la empresa en cobrar sus ventas a crédito.

**Inversión en cuentas por cobrar (a costo):**

```
Inversión en CxC = (Costo variable anual de ventas a crédito ÷ 360) × DSO
```

Una práctica común para acelerar el cobro es ofrecer un **descuento por pronto pago** (por ejemplo, "2/10 neto 30": 2% de descuento si el cliente paga dentro de los primeros 10 días, de lo contrario debe pagar a 30 días). Esto reduce el DSO promedio, porque una parte de los clientes adelanta su pago, pero tiene un costo: el descuento que se deja de cobrar sobre las ventas de los clientes que sí lo toman.

**Para evaluar si conviene una propuesta de descuento, se compara:**

1. **Ahorro por reducción de la inversión en CxC:** la reducción en el capital invertido en cuentas por cobrar (por el menor DSO), multiplicada por el costo de oportunidad del capital de la empresa.
2. **Costo del descuento otorgado:** el total de ventas a crédito que toman el descuento, multiplicado por el porcentaje de descuento.

```
Beneficio neto de la propuesta = Ahorro por reducción de inversión en CxC − Costo del descuento otorgado
```

Si el beneficio neto es positivo, la propuesta conviene financieramente; si es negativo, el costo del descuento supera el ahorro obtenido y no conviene (aunque pueden existir razones no financieras, como mejorar la relación con clientes o reducir el riesgo de incobrables, que ameritan análisis adicional).

## Ejercicio / caso práctico

Una empresa tiene ventas anuales a crédito de **$12,000,000**, con un costo variable equivalente al **70%** de las ventas ($8,400,000 anuales). Actualmente su política de crédito es "neto 60" y el DSO real es de **60 días**.

El área de finanzas propone cambiar la política a **"2/10 neto 30"**: ofrecer 2% de descuento si el cliente paga dentro de los primeros 10 días, lo cual se estima reduciría el DSO promedio a **30 días**. Se estima que el **60% de los clientes** tomarían el descuento por pronto pago.

El costo de oportunidad del capital de la empresa es del **15% anual**.

Se pide:

1. Calcular la inversión actual en cuentas por cobrar (a costo) con el DSO de 60 días.
2. Calcular la inversión proyectada en cuentas por cobrar si el DSO baja a 30 días.
3. Calcular el ahorro anual por la reducción de la inversión en CxC (aplicando el costo de oportunidad del 15%).
4. Calcular el costo anual del descuento otorgado a los clientes que lo toman.
5. Determinar el beneficio neto de la propuesta y concluir si conviene implementarla.

## Solución / guía de solución

**1. Inversión actual en CxC (DSO = 60 días)**

```
Inversión actual = (8,400,000 ÷ 360) × 60 = $1,400,000
```

**2. Inversión proyectada en CxC (DSO = 30 días)**

```
Inversión proyectada = (8,400,000 ÷ 360) × 30 = $700,000
```

**3. Ahorro por reducción de la inversión en CxC**

Reducción en la inversión: $1,400,000 − $700,000 = **$700,000** liberados.

```
Ahorro anual = 700,000 × 15% = $105,000
```

**4. Costo del descuento otorgado**

```
Costo del descuento = 12,000,000 × 60% × 2% = $144,000
```

**5. Beneficio neto de la propuesta**

```
Beneficio neto = 105,000 − 144,000 = −$39,000
```

**Conclusión:** el beneficio neto es **negativo (−$39,000 anuales)**, por lo que, en términos estrictamente financieros, la propuesta **no conviene**: el costo del descuento otorgado ($144,000) es mayor que el ahorro obtenido por liberar capital de cuentas por cobrar ($105,000). La empresa podría explorar alternativas, como un porcentaje de descuento menor, un plazo de pronto pago distinto, o evaluar si existen beneficios adicionales (mejor relación con clientes, menor riesgo de incobrables) que justifiquen el costo neto.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

```
Actúa como un analista financiero especializado en administración de capital de trabajo. Tengo una empresa con ventas anuales a crédito de $12,000,000 y costo variable del 70% de las ventas. Actualmente el DSO (días promedio de cobro) es de 60 días.

Se propone cambiar la política de crédito a "2/10 neto 30" (2% de descuento por pago dentro de 10 días), lo que reduciría el DSO a 30 días. Se estima que el 60% de los clientes tomarían el descuento. El costo de oportunidad del capital de la empresa es del 15% anual.

1. Calcula la inversión actual en cuentas por cobrar (a costo) y la inversión proyectada con el nuevo DSO.
2. Calcula el ahorro anual por la reducción de la inversión en cuentas por cobrar.
3. Calcula el costo anual del descuento otorgado.
4. Determina el beneficio neto de la propuesta y concluye si conviene implementarla, explicando el razonamiento.

Muestra el procedimiento y las fórmulas utilizadas, no solo el resultado final.
```

**Documentos a adjuntar:** Ninguno — todos los datos del caso (ventas, costo variable, DSO actual y propuesto, porcentaje de descuento y de clientes que lo toman, costo de oportunidad) caben en el prompt. Si se quiere usar el caso de una empresa real, se sugiere adjuntar su Estado de Resultados para obtener ventas y costo variable reales.

## Recursos adicionales

- Plantilla de Excel para el cálculo de inversión en CxC bajo distintos escenarios de DSO y políticas de descuento.
- Lectura sugerida: administración del ciclo de conversión de efectivo y políticas de crédito y cobranza (relacionado con el ejercicio de **Ciclo de Conversión de Efectivo** de esta misma materia).
