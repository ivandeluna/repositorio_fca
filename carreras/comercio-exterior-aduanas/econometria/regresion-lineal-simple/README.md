# Regresión Lineal Simple

**Carrera:** Comercio Exterior y Aduanas
**Materia:** Econometría
**Tema:** Modelos de regresión — estimación por Mínimos Cuadrados Ordinarios (MCO)
**Nivel:** Introductorio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá estimar los parámetros de un modelo de regresión lineal simple por Mínimos Cuadrados Ordinarios (MCO), interpretar la pendiente y el intercepto en el contexto de un problema de comercio exterior, calcular el coeficiente de determinación (R²), y usar el modelo para hacer una predicción.

## Teoría

> *Nota de transparencia: esta sección se redactó con apoyo de IA a partir del lineamiento temático del profesor. Revisar y ajustar antes de usar en clase.*

La **regresión lineal simple** es el modelo econométrico más básico para describir la relación entre dos variables: una variable dependiente **Y** (la que se quiere explicar o predecir) y una variable independiente **X** (la que se usa para explicarla). El modelo poblacional se escribe como:

$$Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i$$

Donde:
- **β₀** (intercepto) = el valor esperado de Y cuando X = 0.
- **β₁** (pendiente) = el cambio esperado en Y ante un incremento de una unidad en X.
- **ε_i** (término de error) = la parte de Y que el modelo no explica.

Como no observamos los verdaderos β₀ y β₁, se **estiman** a partir de los datos usando el método de **Mínimos Cuadrados Ordinarios (MCO)**, que encuentra la línea recta que minimiza la suma de los errores al cuadrado entre los valores observados y los predichos por el modelo:

$$\hat{\beta}_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2} \qquad \hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}$$

Una vez estimados los coeficientes, el modelo ajustado permite calcular valores predichos (Ŷ) y evaluar qué tan bien se ajusta a los datos mediante el **coeficiente de determinación (R²)**, que va de 0 a 1 e indica qué proporción de la variación de Y es explicada por X:

$$R^2 = \frac{\left[\sum (X_i-\bar{X})(Y_i-\bar{Y})\right]^2}{\sum (X_i-\bar{X})^2 \cdot \sum (Y_i-\bar{Y})^2}$$

**Interpretación práctica:**
- Un **R² cercano a 1** indica que el modelo explica casi toda la variación de Y a partir de X (buen ajuste).
- La **pendiente (β₁)** dice cuánto cambia, en promedio, la variable dependiente por cada unidad que aumenta la variable independiente — es la cifra que más interesa interpretar en un contexto de negocio o de política económica.
- El intercepto (β₀) no siempre tiene una interpretación económica razonable (por ejemplo, un tipo de cambio de cero no existe en la realidad), por lo que a veces solo se reporta como parte del ajuste matemático.

## Ejercicio / caso práctico

Una empresa exportadora de Comercio Exterior en Torreón, Coahuila, quiere entender si existe una relación entre el **tipo de cambio MXN/USD** y el valor de sus **exportaciones mensuales** (en miles de USD). Se recopiló la siguiente información de los últimos 8 meses:

| Mes | Tipo de cambio promedio (X, MXN/USD) | Exportaciones (Y, miles de USD) |
|---|---:|---:|
| 1 | 18.20 | 150 |
| 2 | 18.50 | 158 |
| 3 | 18.90 | 165 |
| 4 | 19.30 | 172 |
| 5 | 19.60 | 180 |
| 6 | 20.10 | 188 |
| 7 | 20.40 | 193 |
| 8 | 20.80 | 200 |

**Se pide:**

1. Estimar la pendiente (β̂₁) y el intercepto (β̂₀) del modelo de regresión lineal simple `Exportaciones = β₀ + β₁ · Tipo de cambio + ε` por Mínimos Cuadrados Ordinarios.
2. Escribir la ecuación del modelo ajustado e interpretar el significado de la pendiente en el contexto del negocio.
3. Calcular el coeficiente de determinación (R²) e interpretar qué tan bien se ajusta el modelo a los datos.
4. Usar el modelo para predecir las exportaciones esperadas si el tipo de cambio promedio del próximo mes fuera de **21.00 MXN/USD**.
5. Mencionar una limitación de este análisis (por ejemplo, ¿es razonable asumir que la relación es causal, o solo correlacional?).

## Solución / guía de solución

**1. Cálculos previos (n = 8):**

- X̄ = 19.475, Ȳ = 175.75
- Σ(X−X̄)(Y−Ȳ) = 113.25
- Σ(X−X̄)² = 5.955
- Σ(Y−Ȳ)² = 2,161.5

**2. Estimación de los coeficientes:**

β̂₁ = 113.25 / 5.955 ≈ **19.02**
β̂₀ = 175.75 − (19.02 × 19.475) ≈ **−194.62**

**Modelo ajustado:**

Exportaciones = −194.62 + 19.02 × Tipo de cambio

**Interpretación de la pendiente:** por cada peso que sube el tipo de cambio MXN/USD, las exportaciones mensuales de la empresa aumentan, en promedio, **19.02 miles de USD** (≈ $19,020 USD), manteniendo todo lo demás constante.

**3. Coeficiente de determinación:**

R² = (113.25)² / (5.955 × 2,161.5) ≈ **0.996**

El modelo explica aproximadamente el **99.6%** de la variación de las exportaciones mensuales a partir del tipo de cambio — un ajuste muy alto para este conjunto de datos.

**4. Predicción para X = 21.00:**

Exportaciones = −194.62 + 19.02 × 21.00 ≈ **204.75 miles de USD**

**5. Limitación:** el modelo muestra una **asociación estadística**, no necesariamente una relación de **causalidad**. Otros factores (demanda del socio comercial, precios internacionales, capacidad de producción) pueden estar moviéndose junto con el tipo de cambio y explicar parte de la relación observada; además, con solo 8 observaciones mensuales el resultado es sensible a datos atípicos o a cambios de tendencia.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso o dataset.

```
Actúa como un profesor de econometría explicando un ejercicio de regresión lineal simple.
Tengo los siguientes datos mensuales de una empresa exportadora:

Mes | Tipo de cambio (X, MXN/USD) | Exportaciones (Y, miles de USD)
1   | 18.20 | 150
2   | 18.50 | 158
3   | 18.90 | 165
4   | 19.30 | 172
5   | 19.60 | 180
6   | 20.10 | 188
7   | 20.40 | 193
8   | 20.80 | 200

1. Estima por Mínimos Cuadrados Ordinarios (MCO) la pendiente y el intercepto
   del modelo Exportaciones = β0 + β1 * Tipo de cambio + error, mostrando las
   sumas intermedias (Sxy, Sxx, Syy).
2. Escribe la ecuación del modelo ajustado e interpreta la pendiente en el
   contexto del negocio.
3. Calcula el coeficiente de determinación (R²) e interpreta el ajuste.
4. Predice las exportaciones esperadas si el tipo de cambio fuera de 21.00.
5. Señala una limitación de interpretar este resultado como causalidad.

Muestra el desarrollo paso a paso, no solo el resultado final.
```

**Documentos a adjuntar:** ninguno es indispensable, ya que la tabla de datos cabe directamente en el prompt. Si se quiere trabajar con datos reales de una empresa, se sugiere adjuntar un archivo de Excel o CSV con la serie histórica de tipo de cambio y exportaciones mensuales.

## Recursos adicionales

- Plantilla de cálculo en Excel: *(por agregar)*
- Lectura sugerida: capítulo de regresión lineal simple y MCO en el libro de texto del curso de Econometría.
