---
titulo: Regresión lineal múltiple
tema: Regresión lineal múltiple
nivel: Intermedio
duracion_estimada: 50 min
tipo: Ejercicio práctico
modalidad: Individual
autor: Carmen Borrego-Salcido
fecha: 2026-10-31
asistencia_ia: Redacción con IA verificada por el profesor
revisado_por_docente: false
---
## Objetivo de aprendizaje

Que el estudiante estime, interprete y evalúe un modelo de regresión lineal 
múltiple a partir de la salida de un paquete estadístico (Excel, R, Stata, etc.),
identifique el significado de cada coeficiente, valore la bondad de ajuste y la 
significancia del modelo, y utilice la ecuación estimada para explicar y predecir
una variable económica.

## Teoría

> Nota de transparencia: "redacción base del profesor, ampliada y pulida con IA"

1. ¿Qué es la regresión lineal múltiple?

Es una técnica que modela la relación entre una variable dependiente (Y) y dos o
más variables independientes o explicativas (X₁, X₂, …, Xₖ). Permite medir el
efecto de cada variable explicativa sobre Y, manteniendo constantes las demás 
(ceteris paribus).

2. Modelo poblacional

Yᵢ = β₀ + β₁X₁ᵢ + β₂X₂ᵢ + … + βₖXₖᵢ + εᵢ

3. Modelo estimado

Ŷᵢ = b₀ + b₁X₁ᵢ + b₂X₂ᵢ + … + bₖXₖᵢ

Donde:

Yᵢ = variable dependiente
Xⱼᵢ = variables independientes
β₀ = intercepto poblacional; β₁, …, βₖ = coeficientes poblacionales
b₀, b₁, …, bₖ = estimadores obtenidos con la muestra
εᵢ = término de error (lo que el modelo no explica)
n = número de observaciones; k = número de variables independientes
4. Estimación por Mínimos Cuadrados Ordinarios (MCO)

MCO elige los coeficientes que minimizan la suma de los errores al cuadrado:

Minimizar Σeᵢ² = Σ(Yᵢ − Ŷᵢ)²

En forma matricial:

b = (X’X)⁻¹ X’Y

5. Interpretación de los coeficientes

b₀ (intercepto): valor esperado de Y cuando todas las X son cero. No siempre 
tiene interpretación económica.
bⱼ (pendiente parcial): cambio esperado en Y cuando Xⱼ aumenta una unidad, 
manteniendo constantes las demás variables.

6. Bondad de ajuste

Descomposición de la varianza:

SCT = SCR + SCE

SCT = Σ(Yᵢ − Ȳ)² (suma de cuadrados total)
SCR = Σ(Ŷᵢ − Ȳ)² (suma de cuadrados de la regresión)
SCE = Σ(Yᵢ − Ŷᵢ)² (suma de cuadrados del error)
Coeficiente de determinación:

R² = SCR / SCT = 1 − SCE / SCT

R² ajustado:

R²aj = 1 − (1 − R²) · (n − 1) / (n − k − 1)

El R² nunca disminuye al agregar variables; el R² ajustado penaliza la inclusión
de variables que no aportan, por lo que es más adecuado para comparar modelos.

Error estándar de la regresión:

s = √[ SCE / (n − k − 1) ]

7. Pruebas de hipótesis

Prueba individual (estadístico t), para cada coeficiente:

H₀: βⱼ = 0 vs. H₁: βⱼ ≠ 0

t = bⱼ / EE(bⱼ), con (n − k − 1) grados de libertad

Se rechaza H₀ si |t| > t crítico o si el valor p < α (por lo general 0.05).

Prueba global (estadístico F), para el modelo completo:

H₀: β₁ = β₂ = … = βₖ = 0 vs. H₁: al menos un βⱼ ≠ 0

F = [SCR / k] / [SCE / (n − k − 1)] = CMR / CME

Se rechaza H₀ si el valor p de F < α.

Intervalo de confianza para cada coeficiente:

bⱼ ± t(α/2, n−k−1) · EE(bⱼ)

8. Supuestos del modelo clásico

Linealidad en los parámetros.
Los errores tienen media cero.
Homocedasticidad: varianza constante de los errores.
No autocorrelación de los errores.
Ausencia de multicolinealidad perfecta (y, en la práctica, que no sea alta).
Normalidad de los errores (necesaria para las pruebas t y F en muestras pequeñas).

9. Multicolinealidad

Ocurre cuando las variables explicativas están fuertemente correlacionadas 
entre sí. Infla los errores estándar y vuelve inestables los coeficientes. 
Se detecta con la matriz de correlaciones y con el Factor de Inflación de 
la Varianza:

FIVⱼ = 1 / (1 − R²ⱼ)

donde R²ⱼ es el R² de regresar Xⱼ contra las demás variables explicativas. 
Como regla práctica, un FIV mayor a 10 indica un problema serio 
(algunos autores usan 5 como umbral más estricto).

## Ejercicio / caso práctico

Planteamiento. Una consultora en comercio internacional estudia los factores que explican las exportaciones de 15 empresas manufactureras mexicanas. Con datos de un año (ficticios, para fines didácticos), estima el modelo:

Exportaciones = b₀ + b₁(Promoción) + b₂(Tipo de cambio) + b₃(Personal) + e

Variables:

Y: Exportaciones anuales (millones de dólares)
X₁: Promoción, gasto en promoción internacional (millones de pesos)
X₂: Tipo de cambio promedio (pesos por dólar)
X₃: Personal, número de empleados dedicados a comercio exterior

**Datos**

| Empresa | Exportaciones (Y) | Promoción (X1) | Tipo de cambio (X2) | Personal (X3) |
|---|---|---|---|---|
| 1 | 14.2 | 2.0 | 17.2 | 6 |
| 2 | 18.5 | 3.5 | 18.5 | 4 |
| 3 | 12.8 | 1.5 | 17.8 | 9 |
| 4 | 23.0 | 4.0 | 19.0 | 5 |
| 5 | 29.4 | 5.5 | 18.2 | 12 |
| 6 | 12.6 | 2.5 | 17.5 | 3 |
| 7 | 30.1 | 6.0 | 19.4 | 8 |
| 8 | 22.3 | 3.0 | 18.0 | 10 |
| 9 | 24.6 | 4.5 | 18.8 | 7 |
| 10 | 31.8 | 7.0 | 19.6 | 6 |
| 11 | 31.2 | 5.0 | 18.4 | 11 |
| 12 | 10.5 | 2.0 | 17.0 | 5 |
| 13 | 33.9 | 6.5 | 19.2 | 9 |
| 14 | 29.0 | 3.8 | 18.6 | 13 |
| 15 | 18.4 |


## Solución / guía de solución

Guía de solución: regresión lineal múltiple
Paso 1. Identificar el modelo y las variables

Escribe Y (exportaciones, millones de dólares) y las tres X: promoción (millones
de pesos), tipo de cambio (pesos por dólar) y personal (número de empleados).
Identifica n = 15 y k = 3. Los grados de libertad del error son n − k − 1 = 11.

Paso 2. Escribir la ecuación estimada

Toma los coeficientes de la tabla de coeficientes:
Exportaciones = −38.976 + 2.862(Promoción) + 2.339(Tipo de cambio) + 0.971(Personal)
Paso 3. Interpretar los coeficientes

Estructura de cada interpretación: “Por cada [unidad] adicional de [X], 
Y cambia en [b] [unidades de Y], manteniendo constantes las demás variables.”
Verifica que el signo sea congruente con la teoría económica (más promoción, 
más exportaciones; depreciación del peso, más exportaciones).
Revisa si el intercepto tiene sentido: con todas las X en cero queda fuera del 
rango observado, así que no se interpreta.

Paso 4. Prueba global (F)

Hipótesis: H0: β1 = β2 = β3 = 0; H1: al menos un βj ≠ 0.
Estadístico: F = CMR / CME = 285.312 / 2.254 = 126.6.
Criterio: el F crítico con 3 y 11 grados de libertad y α = 0.05 es 
aproximadamente 3.59. También sirve comparar el valor p con α.
Decisión: 126.6 > 3.59 (o p = 8.26E-09 < 0.05), por lo que se rechaza H0.
Conclusión: el modelo es globalmente significativo.

Paso 5. Pruebas individuales (t)

Hipótesis para cada variable: H0: βj = 0; H1: βj ≠ 0.
Estadístico: t = coeficiente / error típico. Por ejemplo, para promoción: 
2.862 / 0.448 = 6.39.
Criterio: el t crítico con 11 grados de libertad y α = 0.05 (dos colas) 
es 2.201.
Decisión: las tres variables superan 2.201 en valor absoluto (6.39, 2.43 y 7.29)
y sus valores p son menores a 0.05, así que todas son significativas.
Verificación con intervalos: ninguno de los intervalos de 95% contiene el cero. 
Se calculan como b ± 2.201 · EE; para promoción, 2.862 ± 2.201(0.448) = [1.876, 3.848].

Paso 6. Bondad de ajuste

R² = SCR / SCT = 855.935 / 880.724 = 0.9719, es decir, el modelo explica 97.19% 
de la variación de las exportaciones.
R² ajustado = 1 − (1 − 0.9719)(14 / 11) = 0.9642.
Error típico = √2.254 = 1.501 millones de dólares.
Explica por qué se reporta el R² ajustado: penaliza la inclusión de variables, y
con solo 15 observaciones y 3 regresores esa corrección importa.
Paso 7. Diagnóstico de multicolinealidad

Compara cada FIV con el umbral (10, o 5 si se quiere más estricto). 
Los tres FIV son menores a 3.61, así que no hay multicolinealidad grave.
Para matizar: promoción y tipo de cambio están correlacionadas entre sí 
(r ≈ 0.85), lo que ensancha el error típico del tipo de cambio y lo convierte en
la variable con significancia más débil.

Paso 8. Predicción

Sustituye en la ecuación: −38.976 + 2.862(5) + 2.339(18.5) + 0.971(9) = −38.976 + 14.310 + 43.272 + 8.742.
Resultado: aproximadamente 27.35 millones de dólares. Con los coeficientes sin 
redondear el software da 27.36; esa diferencia se debe solo al redondeo.
Aclara que es una predicción puntual y que los valores usados están dentro del 
rango observado en la muestra.

Paso 9. Comparar la importancia relativa de las variables

Los coeficientes no son comparables directamente porque dependen de las unidades.
Usa coeficientes estandarizados: beta = b · (desviación estándar de X / desviación estándar de Y).
Resultados: promoción ≈ 0.61, personal ≈ 0.38, tipo de cambio ≈ 0.23. La promoción tiene el mayor efecto relativo.
Paso 10. Conclusión general

Redacta un párrafo que integre: significancia global, variables significativas, 
ajuste del modelo, ausencia de multicolinealidad grave y recomendación para la 
empresa (por ejemplo, que la inversión en promoción es el factor con mayor efecto
sobre las exportaciones).

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Escribe aquí un prompt listo para copiar y pegar, que guíe a un asistente de IA (Claude, ChatGPT, etc.) a resolver o explicar este ejercicio paso a paso.

```
[“Actúa como profesor de econometría de licenciatura. Te comparto el planteamiento y la salida de una regresión lineal múltiple para que me guíes en su resolución completa.

Contexto: se estudian los factores que explican las exportaciones anuales de 15 empresas manufactureras mexicanas. La variable dependiente es [exportaciones, en millones de dólares] y las independientes son [promoción internacional, en millones de pesos], [tipo de cambio, en pesos por dólar] y [personal dedicado a comercio exterior, en número de empleados].

Datos y salida: [pegar aquí la tabla de datos, las estadísticas de la regresión, el ANOVA, los coeficientes y los FIV].

Resuelve en este orden, mostrando las fórmulas y la sustitución de valores en cada paso:

Identifica n, k y los grados de libertad del error.
Escribe la ecuación estimada.
Interpreta cada coeficiente con sus unidades y bajo el supuesto ceteris paribus, y explica si el intercepto tiene sentido económico.
Realiza la prueba F global con α = 0.05: hipótesis, estadístico, criterio de decisión y conclusión.
Realiza la prueba t individual de cada variable con α = 0.05 y verifica con los intervalos de confianza.
Interpreta el R², el R² ajustado y el error típico, y explica por qué se reportan ambos R².
Evalúa la multicolinealidad con los FIV.
Predice las exportaciones de una empresa con [5] millones de pesos en promoción, tipo de cambio de [18.5] y [9] empleados en comercio exterior.
Determina qué variable tiene mayor efecto relativo, calculando e interpretando los coeficientes estandarizados.
Redacta una conclusión general en un párrafo, con una recomendación para la empresa.
Explica en lenguaje claro, sin código de programación, y señala al final los errores más comunes que un estudiante podría cometer en este ejercicio.”]
```

**Documentos a adjuntar:** [Ninguno: los datos del caso se pueden pegar directamente en el prompt" si no aplica]

## Recursos adicionales

- Lectura sugerida: Introducción a la probabilidad y estadística, Mendenhall, Beaver y Beaver, 14ª edición, 2015, Cengage Learning.
- Lectura sugerida: Introductory econometrics for finance, Chris Brooks, 3era edición, Cambridge University Press. 
