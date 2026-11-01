---
titulo: Análisis de tendencias
materia: Herramientas en la función financiera
tema: Análisis horizontal
nivel: Introductorio
duracion_estimada: 30 min.
tipo: Ejercicio práctico
modalidad: Individual
autor: Carmen Borrego-Salcido
fecha: 2026-11-01
asistencia_ia: Material elaborado con IA y verificado por el profesor
revisado_por_docente: false
---
#### Objetivo de aprendizaje
Que el estudiante aplique el análisis horizontal (absoluto y relativo) a los estados financieros de una empresa de dos o más periodos, para identificar variaciones y tendencias en sus cuentas, interpretar su significado y fundamentar conclusiones que apoyen la toma de decisiones financieras.

#### Teoría

**1. ¿Qué es?**

El análisis horizontal compara una misma cuenta de los estados financieros (balance general o estado de resultados) entre dos o más periodos, para saber cuánto cambió y en qué dirección. Responde a la pregunta: _¿esta cuenta aumentó o disminuyó, y en cuánto?_

**2. Qué se calcula**

Para cada cuenta se calculan dos variaciones:

- **Variación absoluta:** cuánto cambió en pesos.

Variación absoluta = Valor del periodo actual − Valor del periodo anterior

- **Variación relativa:** cuánto cambió en porcentaje, respecto al periodo anterior.

El periodo más antiguo es siempre la **base** (equivale a 100%).

**3. Cómo calcular la variación relativa con regla de tres**

La variación relativa es una regla de tres simple directa: el periodo base corresponde a 100% y se busca a qué porcentaje equivale la variación absoluta.

|Concepto|Porcentaje|
|---|---|
|Periodo base (anterior)|100%|
|Variación absoluta|x|

Fórmula:

x = (Variación absoluta × 100) / Periodo base

Si el resultado es positivo, la cuenta aumentó; si es negativo, disminuyó.

**4. Procedimiento paso a paso**

1. Identifica el periodo base (el más antiguo) y el periodo actual.
2. Calcula la variación absoluta: periodo actual − periodo base.
3. Arma la regla de tres: periodo base = 100%, variación absoluta = x.
4. Calcula x = (variación absoluta × 100) / periodo base.
5. Escribe el resultado con su signo y el símbolo %.
6. Interpreta: ¿es favorable o desfavorable para la empresa?


#### Caso práctico
Estado de resultados (pesos):

|Cuenta|2024|2025|Variación absoluta|Variación relativa|
|---|---|---|---|---|
|Ventas|800,000|920,000|120,000|15%|
|Costo de ventas|500,000|610,000|110,000|22%|
|Utilidad bruta|300,000|310,000|10,000|3.33%|
|Gastos de operación|150,000|138,000|−12,000|−8%|

Cálculo de la primera fila (ventas) con regla de tres:

|Pesos|Porcentaje|
|---|---|
|800,000|100%|
|120,000|x|

x = (120,000 × 100) / 800,000 = **15%**

Cálculo de la tercera fila (utilidad bruta):

x = (10,000 × 100) / 300,000 = **3.33%**

Cálculo de la cuarta fila (gastos de operación, que disminuyeron):

x = (−12,000 × 100) / 150,000 = **−8%**

**6. Cómo interpretar**

- Las ventas crecieron 15%, pero el costo de ventas creció 22%. Como los costos aumentaron más rápido que las ventas, la utilidad bruta creció solo 3.33%.
- Los gastos de operación bajaron 8%, lo cual es favorable.
- En general: que aumenten ventas, utilidades y activos productivos suele ser favorable; que aumenten costos, gastos y deudas más rápido que las ventas suele ser desfavorable. Siempre conviene revisar el contexto de la empresa antes de concluir.

**7. Tendencias con más de dos periodos (números índice)**

Cuando se comparan tres o más años, se toma uno como **año base** (índice 100) y se calcula el índice de cada año con otra regla de tres:

|Pesos|Índice|
|---|---|
|Valor del año base|100|
|Valor del año que se evalúa|x|

x = (Valor del año evaluado × 100) / Valor del año base

_Ejemplo:_ si las ventas fueron 800,000 en 2024 (base) y 920,000 en 2025, el índice de 2025 es (920,000 × 100) / 800,000 = 115. Esto significa que las ventas de 2025 equivalen a 115% de las de 2024.

**8. Cuidados al calcular**

- La base siempre es el periodo anterior (o el año base elegido), no el actual.
- Si el valor base es cero, no se puede calcular la variación relativa.
- Conserva el signo: un resultado negativo indica disminución.
- Compara siempre periodos de igual duración (por ejemplo, años completos contra años completos).

### Prompts sugeridos para el análisis horizontal

#### Instrucciones para el alumno

**Qué debes hacer:** copia el prompt, sustituye lo que aparece entre corchetes por los datos de tu empresa y pégalo en la herramienta de IA que uses. Después compara el resultado de la IA con tus propios cálculos hechos a mano y señala cualquier diferencia.

#### Prompt 1. Calcular el análisis horizontal

> “Actúa como profesor de la materia Herramientas en la función financiera. Realiza el análisis horizontal de los siguientes estados financieros de [nombre de la empresa], de los periodos [año anterior] y [año actual]: [pegar aquí el balance general y el estado de resultados con sus cuentas y montos].
> 
> **Sigue este orden:**
> 
> 1. Presenta una tabla con las columnas: cuenta, periodo anterior, periodo actual, variación absoluta y variación relativa.
> 2. Calcula la variación absoluta como periodo actual menos periodo anterior.
> 3. Calcula la variación relativa con regla de tres: el periodo anterior equivale a 100% y la variación absoluta equivale a x. Muestra la regla de tres de al menos tres cuentas.
> 4. Indica con su signo si cada cuenta aumentó o disminuyó.
> 
> Explica en lenguaje claro, sin código de programación.”

#### Prompt 2. Verificar la solución de la IA

> “Ahora verifica tu propia solución. Recalcula la variación relativa de tres cuentas, comprueba que el periodo anterior se haya usado siempre como base y que los signos sean correctos. Si encuentras alguna diferencia o error, indícalo y corrígelo.”

#### Prompt 3. Interpretar los resultados

> “Actúa como analista financiero. Con base en el análisis horizontal anterior, identifica las cuatro variaciones más relevantes, indica si cada una es favorable o desfavorable para la empresa y explica por qué. Señala si los costos y gastos crecieron más rápido que las ventas, y redacta una conclusión de un párrafo con una recomendación para la toma de decisiones. Aclara qué información adicional necesitarías para confirmar tus conclusiones.”

#### Prompt 4. Calcular tendencias con más de dos periodos

> “Actúa como profesor de la materia Herramientas en la función financiera. Te comparto las ventas de [empresa] de los últimos años: [año 1: monto, año 2: monto, año 3: monto]. Toma el primer año como base (índice 100) y calcula el índice de cada año con regla de tres. Presenta una tabla, muestra el cálculo de cada índice e interpreta la tendencia: si crece, decrece o es irregular, y qué significa cada índice.”

#### Prompt 5. Comprobar la comprensión

> “Actúa como profesor de la materia Herramientas en la función financiera. Hazme 5 preguntas de opción múltiple sobre análisis horizontal (variación absoluta, variación relativa con regla de tres, periodo base, números índice e interpretación), con situaciones aplicadas a empresas. Espera mis respuestas y, al final, retroalimenta cada una explicando por qué es correcta o incorrecta.”
