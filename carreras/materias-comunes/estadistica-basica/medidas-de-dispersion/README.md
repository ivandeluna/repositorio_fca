---
titulo: Medidas de dispersión
tema: Medidas de dispersión
nivel: Introductorio
duracion_estimada: 60 min
tipo: Ejercicio práctico
modalidad: Individual
entregable_alumno: El prompt que usó, ya adaptado. La respuesta de la IA. Un
  párrafo breve que indique si sus cálculos coinciden con los de la IA y, si
  hubo diferencias, quién tenía razón y por qué.
autor: Carmen Borrego-Salcido
fecha: 2026-10-31
tags:
  - Estadística
asistencia_ia: "Redacción elaborada con IA verificada por el profesor "
revisado_por_docente: false
---
## Objetivo de aprendizaje

Que el estudiante calcule e interprete el rango, el rango intercuartílico, la varianza, la desviación estándar y el coeficiente de variación de un conjunto de datos, y los utilice junto con las medidas de tendencia central para describir qué tan homogéneos o dispersos son los datos y comparar la variabilidad entre distintos conjuntos.

#### Teoría

**1. ¿Qué son las medidas de dispersión?**

Las medidas de tendencia central resumen el centro de los datos, pero no dicen qué tan alejados están los valores de ese centro. Las medidas de dispersión (o de variabilidad) cuantifican ese alejamiento. Dos conjuntos pueden tener la misma media y ser muy distintos.

Ejemplo: los conjuntos {48, 50, 52} y {10, 50, 90} tienen media 50, pero el segundo está mucho más disperso. Una media sin una medida de dispersión da una imagen incompleta.

En general, a mayor dispersión, menos representativa es la media y mayor es la incertidumbre o el riesgo asociado a la variable.

**2. Rango (amplitud)**

Es la diferencia entre el valor máximo y el mínimo.

R = x máximo − x mínimo

- Es fácil de calcular e interpretar.
- Solo usa dos datos, por lo que es muy sensible a valores extremos.

**3. Rango intercuartílico (RIC)**

Es la distancia entre el primer y el tercer cuartil, es decir, el rango del 50% central de los datos.

RIC = Q3 − Q1

Donde:

- Q1 = valor que deja 25% de los datos por debajo
- Q3 = valor que deja 75% de los datos por debajo
- No se ve afectado por valores extremos, por lo que es la medida de dispersión recomendada cuando se usa la mediana como medida de centro.
- Se usa para detectar valores atípicos: se consideran atípicos los datos menores a Q1 − 1.5 · RIC o mayores a Q3 + 1.5 · RIC.

**4. Varianza**

Es el promedio de los cuadrados de las desviaciones de cada dato respecto a la media. Se elevan al cuadrado para que las desviaciones positivas y negativas no se cancelen (la suma de las desviaciones simples siempre es cero).

Varianza poblacional:

σ² = Σ(xᵢ − μ)² / N

Varianza muestral:

s² = Σ(xᵢ − x̄)² / (n − 1)

Fórmula de cálculo equivalente (útil para hacerlo a mano):

s² = [Σxᵢ² − n · x̄²] / (n − 1)

Fórmula para datos agrupados en una tabla de frecuencias:

s² = Σ fᵢ(mᵢ − x̄)² / (n − 1)

Donde:

- xᵢ = cada valor observado
- μ = media poblacional; x̄ = media muestral
- N = tamaño de la población; n = tamaño de la muestra
- fᵢ = frecuencia de cada clase
- mᵢ = marca de clase (punto medio del intervalo)

_¿Por qué se divide entre n − 1 en la muestra?_ Porque la media muestral se calcula con los mismos datos, lo que hace que las desviaciones respecto a ella sean, en promedio, ligeramente menores que respecto a la media poblacional. Dividir entre n − 1 (corrección de Bessel) compensa ese sesgo y da un estimador insesgado de la varianza poblacional.

Limitación: sus unidades están al cuadrado (pesos², kilogramos²), lo que dificulta su interpretación directa.

**5. Desviación estándar**

Es la raíz cuadrada de la varianza. Devuelve la medida de dispersión a las unidades originales de los datos.

Población: σ = √σ²

Muestra: s = √s²

- Se interpreta como la distancia típica o promedio de los datos respecto a la media.
- Siempre es mayor o igual a cero; vale cero solo si todos los datos son idénticos.
- Es sensible a valores extremos, pues se basa en la media.
- Si se suma una constante a todos los datos, no cambia; si se multiplican todos los datos por una constante c, la desviación estándar se multiplica por |c|.

**6. Coeficiente de variación (CV)**

Es la desviación estándar expresada como porcentaje de la media. Mide la dispersión relativa, por lo que no depende de las unidades.

CV = (s / x̄) × 100

- Permite comparar la variabilidad de variables con distintas unidades o con medias muy diferentes (por ejemplo, ventas en pesos contra número de empleados).
- Como regla práctica, un CV menor a 10% indica datos muy homogéneos, entre 10% y 30% dispersión moderada, y mayor a 30% alta dispersión. Estos umbrales son orientativos y dependen del contexto.
- No es adecuado cuando la media es cercana a cero.
- En finanzas se interpreta como el riesgo por unidad de rendimiento.

**7. Interpretación de la desviación estándar**

_Regla empírica (para distribuciones con forma de campana):_

- Aproximadamente 68% de los datos está entre x̄ − s y x̄ + s
- Aproximadamente 95% está entre x̄ − 2s y x̄ + 2s
- Aproximadamente 99.7% está entre x̄ − 3s y x̄ + 3s

_Teorema de Chebyshev (para cualquier distribución):_

Al menos 1 − 1/k² de los datos se encuentra a menos de k desviaciones estándar de la media, con k > 1.

- Para k = 2: al menos 75% de los datos
- Para k = 3: al menos 88.9% de los datos

_Puntaje estándar (z):_

z = (xᵢ − x̄) / s

Indica a cuántas desviaciones estándar de la media se encuentra un dato. Un valor con |z| mayor a 3 suele considerarse atípico.

**8. Relación entre dispersión y tendencia central**

- Si la distribución es simétrica y sin valores atípicos, lo habitual es reportar la media con la desviación estándar.
- Si es asimétrica o tiene valores atípicos, lo habitual es reportar la mediana con el rango intercuartílico.
- Para comparar la variabilidad entre conjuntos con distintas unidades o escalas, se usa el coeficiente de variación.



#### Caso práctico

Una empresa exportadora de autopartes quiere evaluar qué tan estable es el tiempo de despacho aduanal de sus embarques. Se registró el tiempo de despacho, en horas, de 10 embarques enviados a Estados Unidos durante un mes (datos ficticios, para fines didácticos).

|Embarque|Tiempo de despacho (horas)|
|---|---|
|1|12|
|2|15|
|3|14|
|4|18|
|5|16|
|6|13|
|7|15|
|8|17|
|9|14|
|10|36|

Considera los 10 embarques como una **muestra** (n = 10).

#### Instrucciones para el alumno

**Qué debes hacer:** resuelve cada paso en orden, escribe la fórmula, sustituye los valores y anota el resultado con sus unidades. Al final entrega tus resultados y tu conclusión en una sola hoja.

**Paso 1. Ordena los datos**  
Escribe los 10 tiempos de menor a mayor.

**Paso 2. Calcula la media**  
Usa la fórmula x̄ = Σxᵢ / n.

**Paso 3. Calcula el rango**  
Resta el valor mínimo al valor máximo.

**Paso 4. Calcula el rango intercuartílico**  
Para obtener los cuartiles, divide los datos ordenados en dos mitades de 5 datos cada una. Q1 es la mediana de la mitad inferior y Q3 es la mediana de la mitad superior. Después calcula RIC = Q3 − Q1.

**Paso 5. Calcula la varianza muestral**  
Usa la fórmula s² = Σ(xᵢ − x̄)² / (n − 1). Te conviene hacer una tabla con tres columnas: xᵢ, (xᵢ − x̄) y (xᵢ − x̄)².

**Paso 6. Calcula la desviación estándar**  
Obtén la raíz cuadrada de la varianza.

**Paso 7. Calcula el coeficiente de variación**  
Usa la fórmula CV = (s / x̄) × 100.

**Paso 8. Detecta valores atípicos**  
Calcula los límites Q1 − 1.5 · RIC y Q3 + 1.5 · RIC. Indica si algún embarque queda fuera de ellos.

**Paso 9. Responde las preguntas de interpretación**

1. ¿Qué indica la desviación estándar sobre el tiempo de despacho de estos embarques? Escríbelo con tus palabras y con unidades.
2. Según el CV, ¿la dispersión es baja, moderada o alta?
3. ¿Qué embarque es atípico y qué efecto tiene sobre el rango y sobre la desviación estándar?
4. Si quitaras el embarque atípico, ¿esperarías que la desviación estándar aumentara o disminuyera? Explica por qué (no hace falta calcularlo).
5. Para describir el despacho típico de esta empresa, ¿recomendarías reportar la media con la desviación estándar, o la mediana con el rango intercuartílico? Justifica tu respuesta.

**Qué debes entregar:** una tabla con los resultados de los pasos 2 a 7 (media, rango, RIC, varianza, desviación estándar y CV), la conclusión del paso 8 y las respuestas del paso 9.

### Guía de solución: medidas de dispersión

**Paso 1. Ordenar los datos**

12, 13, 14, 14, 15, 15, 16, 17, 18, 36

**Paso 2. Media**


x̄ = Σxᵢ / n = (12 + 13 + 14 + 14 + 15 + 15 + 16 + 17 + 18 + 36) / 10 = 170 / 10 = **17 horas**

**Paso 3. Rango**

R = 36 − 12 = **24 horas**

**Paso 4. Rango intercuartílico**

- Mitad inferior: 12, 13, 14, 14, 15. Su mediana es Q1 = 14
- Mitad superior: 15, 16, 17, 18, 36. Su mediana es Q3 = 17
- RIC = Q3 − Q1 = 17 − 14 = **3 horas**

Nota para el docente: existen varios métodos para calcular cuartiles. Excel (función QUARTILE.INC) da Q1 = 14 y Q3 = 16.75, con un RIC de 2.75. Por eso el ejercicio indica el método de las mitades; conviene aclararlo si algún alumno usa software.

**Paso 5. Varianza muestral**

Tabla de desviaciones:

|xᵢ|xᵢ − x̄|(xᵢ − x̄)²|
|---|---|---|
|12|−5|25|
|13|−4|16|
|14|−3|9|
|14|−3|9|
|15|−2|4|
|15|−2|4|
|16|−1|1|
|17|0|0|
|18|1|1|
|36|19|361|
|**Suma**|**0**|**430**|

Verificación: la suma de las desviaciones debe ser cero.

s² = 430 / (10 − 1) = 430 / 9 = **47.78 horas²**

Con la fórmula de cálculo se obtiene lo mismo: [Σxᵢ² − n · x̄²] / (n − 1) = [3,320 − 10(17²)] / 9 = (3,320 − 2,890) / 9 = 430 / 9.

**Paso 6. Desviación estándar**

s = √47.78 = **6.91 horas**

**Paso 7. Coeficiente de variación**

CV = (6.91 / 17) × 100 = **40.66%**

**Paso 8. Valores atípicos**

- Límite inferior: Q1 − 1.5 · RIC = 14 − 1.5(3) = 9.5
- Límite superior: Q3 + 1.5 · RIC = 17 + 1.5(3) = 21.5
- Cualquier dato fuera del intervalo [9.5, 21.5] es atípico. El embarque 10 (36 horas) supera el límite superior, así que **es atípico**. Los demás están dentro del intervalo.

**Tabla resumen de resultados**

|Medida|Resultado|
|---|---|
|Media|17 horas|
|Rango|24 horas|
|Rango intercuartílico|3 horas|
|Varianza|47.78 horas²|
|Desviación estándar|6.91 horas|
|Coeficiente de variación|40.66%|

**Paso 9. Respuestas a las preguntas de interpretación**

1. La desviación estándar de 6.91 horas indica que, en promedio, el tiempo de despacho de un embarque se aleja unas 6.9 horas de la media de 17 horas.
2. Con un CV de 40.66%, la dispersión es **alta** (mayor a 30%): la media es poco representativa del despacho típico.
3. El embarque 10 (36 horas) es el atípico. Por sí solo hace que el rango sea 24 horas y aporta 361 de las 430 unidades de la suma de cuadrados (84%), lo que infla la varianza y la desviación estándar. Es una evidencia clara de que ambas medidas son sensibles a valores extremos.
4. La desviación estándar **disminuiría** mucho, porque el dato atípico es el que aporta casi toda la variabilidad. Para que el docente pueda verificarlo: sin ese embarque, la media sería 14.89 horas, el rango 6 horas, la desviación estándar 1.90 horas y el CV 12.8%.
5. Conviene reportar la **mediana (15 horas) con el rango intercuartílico (3 horas)**, porque ambas no se ven afectadas por el valor atípico y describen mejor el despacho típico. La media (17) queda arrastrada hacia arriba por el dato de 36 horas, y la desviación estándar se infla por el mismo motivo. Aun así, el embarque atípico no debe ignorarse: conviene investigar qué lo causó (inspección, falta de documentos, etc.), pues puede señalar un problema operativo.

#### Errores frecuentes que conviene señalar

- Dividir entre n en lugar de n − 1 al calcular la varianza de una muestra.
- Olvidar que la varianza está en unidades al cuadrado, o reportar la desviación estándar sin unidades.
- Calcular la raíz cuadrada antes de sumar los cuadrados de las desviaciones.
- Cometer un error aritmético y no darse cuenta de que la suma de las desviaciones no da cero.
- Calcular los cuartiles sin ordenar antes los datos.
- Concluir que el dato atípico “se elimina” sin investigar su causa.
- Interpretar el CV sin considerar que sus umbrales (10% y 30%) son orientativos.

## Prompt sugerido para hacerlo con Claude o ChatGPT

Copia y pega el prompt que corresponda en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

#### Prompt 1. Resolver el ejercicio completo

> “Actúa como profesor de estadística descriptiva de licenciatura. Te comparto un caso práctico para que me guíes en su resolución completa.
> 
> **Contexto:** una empresa exportadora de autopartes registró el tiempo de despacho aduanal, en horas, de 10 embarques. Los datos son una muestra: [12, 15, 14, 18, 16, 13, 15, 17, 14, 36].
> 
> **Resuelve en este orden, escribiendo la fórmula, sustituyendo los valores y dando el resultado con sus unidades:**
> 
> 1. Ordena los datos de menor a mayor.
> 2. Calcula la media.
> 3. Calcula el rango.
> 4. Calcula el rango intercuartílico. Obtén Q1 y Q3 dividiendo los datos ordenados en dos mitades de 5 datos y tomando la mediana de cada mitad.
> 5. Calcula la varianza muestral, mostrando una tabla con las columnas xᵢ, (xᵢ − media) y (xᵢ − media)².
> 6. Calcula la desviación estándar.
> 7. Calcula el coeficiente de variación.
> 8. Calcula los límites Q1 − 1.5 · RIC y Q3 + 1.5 · RIC, e indica si hay valores atípicos.
> 9. Interpreta los resultados en el contexto de los tiempos de despacho: qué dice la desviación estándar, si la dispersión del CV es baja, moderada o alta, y qué medidas conviene reportar para describir el despacho típico.
> 
> Explica en lenguaje claro, sin código de programación, y presenta al final una tabla resumen con todos los resultados.”

#### Prompt 2. Verificar la solución de la IA

> “Ahora verifica tu propia solución. Comprueba que la suma de las desviaciones respecto a la media sea cero, recalcula la varianza con la fórmula de cálculo [Σxᵢ² − n · media²] / (n − 1) y confirma que coincide con la anterior. Si encuentras alguna diferencia o error, indícalo y corrígelo.”

#### Prompt 3. Entender el efecto del valor atípico

> “Actúa como profesor de estadística descriptiva. En el ejercicio anterior, el embarque de 36 horas resultó atípico. Calcula la media, el rango, la desviación estándar y el coeficiente de variación sin ese dato, y compáralos en una tabla con los resultados originales. Explica por qué cambian tanto estas medidas, mientras que el rango intercuartílico casi no cambia, y qué debería hacer la empresa con ese embarque antes de decidir si lo elimina del análisis.”

#### Prompt 4. Comprobar la comprensión

> “Actúa como profesor de estadística descriptiva. Hazme 5 preguntas de opción múltiple sobre medidas de dispersión (rango, rango intercuartílico, varianza, desviación estándar y coeficiente de variación), con situaciones aplicadas al comercio internacional. Espera mis respuestas y, al final, retroalimenta cada una explicando por qué es correcta o incorrecta.”

**Documentos a adjuntar:** opcional — puedes adjuntar un archivo de Excel con tus propios datos para que la IA calcule las tres medidas directamente sobre ellos. No es indispensable, ya que los datos del caso caben en el prompt. Puedes cambiar los datos del ejemplo y subir en Excel los tuyos

## Recursos adicionales
- Lectura sugerida: _Introducción a la probabilidad y estadística_, Mendenhall, Beaver y Beaver, 14ª edición, 2015, Cengage Learning.
