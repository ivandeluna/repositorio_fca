---
titulo: Series de tiempo
tema: "Introducción a series temporales "
nivel: Introductorio
duracion_estimada: 50 min
tipo: Método de enseñanza
modalidad: Individual
entregable_alumno: Gráfica de serie de tiempo (original) y gráfica de la series
  de tiempo descompuesta por componentes
autor: Carmen Borrego-Salcido
fecha: 2026-10-31
asistencia_ia: "Redacción de IA verificada por el profesor "
revisado_por_docente: false
---
## Objetivo de aprendizaje

Que el estudiante comprenda qué es una serie temporal y cuáles son sus 
componentes y características fundamentales, para identificar, describir e 
interpretar el comportamiento de una variable económica o empresarial a lo 
largo del tiempo, como base para el análisis y el pronóstico

## Teoría
1. ¿Qué es una serie temporal?

Es un conjunto de observaciones de una variable, registradas en momentos sucesivos y ordenadas cronológicamente, por lo general a intervalos regulares. Se denota:

Yₜ, con t = 1, 2, …, T

Donde:

Yₜ = valor de la variable en el periodo t
t = índice de tiempo
T = número total de observaciones
Diferencia con los datos de corte transversal. En un corte transversal se 
observan muchas unidades (empresas, países) en un mismo momento, y el orden 
de los datos no importa. En una serie temporal se observa una sola unidad a 
lo largo del tiempo, y el orden sí importa, porque el valor de hoy suele 
depender de los valores pasados. Esta dependencia temporal es lo que distingue 
su análisis del de la regresión con datos de corte transversal.

Ejemplos: exportaciones mensuales de México, tipo de cambio diario, 
inflación trimestral, ventas semanales de una empresa.

2. Clasificación de las series temporales

Criterio	Tipos	Ejemplo
Frecuencia	Anual, trimestral, mensual, semanal, diaria	PIB trimestral; tipo de 
cambio diario
Naturaleza de la variable	Flujo: se acumula durante el periodo	Exportaciones 
del mes
Stock: se mide en un instante	Reservas internacionales al cierre del mes
Número de variables	Univariada: una variable	Ventas mensuales
Multivariada: varias variables relacionadas	Exportaciones, tipo de cambio y 
producción industrial
Unidad de medida	Nominal o real (deflactada)	PIB a precios corrientes o a 
precios constantes


3. Componentes de una serie temporal

Una serie temporal puede descomponerse en cuatro componentes:

Tendencia (Tₜ): movimiento de largo plazo, creciente, decreciente o estable,
que refleja la evolución de fondo de la variable (por ejemplo, el crecimiento 
sostenido de las exportaciones manufactureras).
Estacionalidad (Sₜ): patrón que se repite con regularidad dentro de un periodo
fijo, por lo general de un año, debido a factores como el clima, días festivos
o los calendarios fiscales (por ejemplo, el aumento de ventas en diciembre).
Ciclo (Cₜ): fluctuaciones recurrentes alrededor de la tendencia, de duración
variable y mayor a un año, asociadas a las fases de expansión y contracción 
de la economía.
Componente irregular o aleatorio (Iₜ): variaciones impredecibles y de corto plaz
o debidas a eventos fortuitos (huelgas, desastres naturales, choques inesperados). 
También se le llama ruido o error.

4. Modelos de descomposición

Modelo aditivo:

Yₜ = Tₜ + Sₜ + Cₜ + Iₜ

Es adecuado cuando la magnitud de las fluctuaciones estacionales se mantiene 
aproximadamente constante a lo largo del tiempo, aunque la serie crezca.

Modelo multiplicativo:

Yₜ = Tₜ × Sₜ × Cₜ × Iₜ

Es adecuado cuando la amplitud de las fluctuaciones estacionales crece o decrece
en proporción al nivel de la serie. Es el caso más frecuente en series económicas
con tendencia creciente.

Relación entre ambos: al aplicar logaritmos, un modelo multiplicativo se 
convierte en aditivo:

ln Yₜ = ln Tₜ + ln Sₜ + ln Cₜ + ln Iₜ

Cómo elegir: se observa la gráfica. Si las oscilaciones tienen altura similar a 
lo largo de toda la serie, se usa el modelo aditivo; si se van ensanchando 
conforme la serie sube, se usa el multiplicativo.

5. Estacionariedad

Una serie es estacionaria en sentido débil (o de segundo orden) cuando cumple 
tres condiciones:

Media constante: E(Yₜ) = μ para todo t.
Varianza constante: Var(Yₜ) = σ² para todo t.
La covarianza entre dos observaciones depende solo de la distancia k entre ellas,
y no del momento en que se miden: Cov(Yₜ, Yₜ₊ₖ) = γₖ.
En términos intuitivos, una serie estacionaria fluctúa alrededor de un nivel 
constante, con variabilidad estable y sin tendencia ni cambios de comportamiento 
a lo largo del tiempo.

Una serie con tendencia, con estacionalidad o con varianza que cambia en el 
tiempo no es estacionaria. Esto es relevante porque la mayoría de los modelos 
clásicos de pronóstico (por ejemplo, ARMA y ARIMA) requieren estacionariedad, o 
una transformación que la logre.

Dos series de referencia:

Ruido blanco: serie de variables no correlacionadas, con media cero y varianza 
constante: Yₜ = εₜ. Es estacionaria y no tiene ningún patrón predecible.
Caminata aleatoria: Yₜ = Yₜ₋₁ + εₜ. Es no estacionaria, porque su varianza crec
e con el tiempo. Muchas series financieras, como los precios de activos y el 
tipo de cambio, se comportan de manera cercana a una caminata aleatoria.
Cómo se logra la estacionariedad:

Diferenciación (para eliminar tendencia): ΔYₜ = Yₜ − Yₜ₋₁
Transformación logarítmica (para estabilizar la varianza): ln Yₜ
Diferencia logarítmica, que aproxima la tasa de crecimiento: Δ ln Yₜ = ln Yₜ − ln Yₜ₋₁
6. Autocorrelación

Mide qué tan relacionada está una serie consigo misma en distintos rezagos. 
La autocorrelación de rezago k es:

ρₖ = γₖ / γ₀ = Cov(Yₜ, Yₜ₊ₖ) / Var(Yₜ)

Su estimación muestral es:

rₖ = Σ(Yₜ − Ȳ)(Yₜ₊ₖ − Ȳ) / Σ(Yₜ − Ȳ)²

El numerador se suma desde t = 1 hasta T − k, y el denominador desde t = 1 hasta T.

Donde:

Ȳ = media de la serie
k = rezago (número de periodos de separación)
rₖ toma valores entre −1 y 1
Al graficar rₖ contra k se obtiene el correlograma. Sirve para detectar patrones
: en una serie con tendencia, las autocorrelaciones decaen muy lentamente; en una
serie con estacionalidad, aparecen picos en los rezagos estacionales 
(por ejemplo, k = 12 en datos mensuales); en un ruido blanco, todas son cercanas a cero.

7. Medidas básicas de variación

Variación absoluta: ΔYₜ = Yₜ − Yₜ₋₁

Tasa de variación porcentual: [(Yₜ − Yₜ₋₁) / Yₜ₋₁] × 100

Tasa de variación anual (para datos mensuales): [(Yₜ − Yₜ₋₁₂) / Yₜ₋₁₂] × 100

La comparación contra el mismo periodo del año anterior elimina el efecto de la 
estacionalidad.

Número índice simple: Iₜ = (Yₜ / Y₀) × 100, donde Y₀ es el valor del periodo base.

8. Cómo leer la gráfica de una serie temporal

El primer paso de todo análisis es graficar la serie, con el tiempo en el eje 
horizontal. Conviene preguntarse:

¿Hay tendencia? ¿Es creciente, decreciente o cambia de dirección?
¿Hay un patrón que se repite cada cierto periodo (estacionalidad)?
¿Las oscilaciones se mantienen del mismo tamaño o se amplían (aditivo o multiplicativo)?
¿Hay valores atípicos o quiebres bruscos (por ejemplo, el efecto de la pandemia en 2020)?
¿La serie parece fluctuar alrededor de un nivel constante (estacionaria) o se aleja de él (no estacionaria)?

9. Importancia en la toma de decisiones

El análisis de series temporales permite describir el comportamiento histórico 
de una variable, separar sus componentes, pronosticar valores futuros y evaluar 
el efecto de eventos o políticas. En comercio internacional se aplica, entre 
otros casos, al pronóstico de exportaciones e importaciones, al análisis del 
tipo de cambio, a la planeación de inventarios y de ventas estacionales, y a la 
medición de la inflación y del ciclo económico


## Ejercicio / caso práctico



## Solución / guía de solución

[Opcional — se puede omitir del README.md público y poner en un archivo `solucion.md` aparte si no se quiere exponer a los alumnos.]

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Escribe aquí un prompt listo para copiar y pegar, que guíe a un asistente de IA (Claude, ChatGPT, etc.) a resolver o explicar este ejercicio paso a paso.

```
Prompt para identificar los componentes

“Actúa como profesor de econometría. Te describo una serie temporal: 
[variable, frecuencia, periodo y comportamiento observado, por ejemplo, 
exportaciones mensuales de México de 2015 a 2025]. Indícame qué componentes 
(tendencia, estacionalidad, ciclo e irregular) esperarías encontrar, cuáles 
serían sus causas económicas y si convendría un modelo de descomposición aditivo
o multiplicativo. Justifica tu respuesta en lenguaje claro.”

Prompt para evaluar la estacionariedad

“Actúa como profesor de econometría. Explícame con un ejemplo aplicado al 
comercio internacional qué significa que una serie sea estacionaria. Después 
dime si [tipo de cambio diario peso-dólar] sería estacionaria o no y por qué, y 
qué transformación podría aplicarse para volverla estacionaria. Explica sin usar
código de programación.”

Prompt para interpretar una gráfica

“Actúa como profesor de econometría. Te describo la gráfica de una serie 
temporal: [describir tendencia, picos repetitivos, valores atípicos y cambios 
de nivel]. Ayúdame a interpretarla: identifica sus componentes, indica si parece
estacionaria, y dime qué preguntas debería hacerme antes de pronosticarla.”

```

**Documentos a adjuntar:** [indicar si se requiere adjuntar algún documento, p. ej. "se sugiere agregar el estado de resultados de la empresa" — o escribir "Ninguno: los datos del caso se pueden pegar directamente en el prompt" si no aplica]

## Recursos adicionales

- Lectura sugerida: Introductory econometrics for finance, Chris Brooks, 3era edición, Cambridge University Press. 


---
*Al terminar, crea también un `metadata.yml` en la misma carpeta (ver ejemplo en `carreras/contador-publico/aplicar-administracion-finanzas/ciclo-conversion-efectivo/metadata.yml`) y agrega este ejercicio a la tabla del README.md de su materia.*
