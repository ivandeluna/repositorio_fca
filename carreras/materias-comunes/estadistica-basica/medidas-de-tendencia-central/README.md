# Medidas de Tendencia Central

**Carrera:** Materias Comunes (Contador Público, Comercio Exterior y Aduanas, Administración de Empresas)
**Materia:** Estadística Básica
**Tema:** Medidas de tendencia central: media, mediana y moda
**Nivel:** Introductorio
**Duración estimada:** 30 min

## Objetivo de aprendizaje

Que el estudiante calcule e interprete la media, la mediana y la moda de un conjunto de datos, distinga en qué situaciones conviene utilizar cada una, y reconozca su relación en una distribución normal, para resumir información cuantitativa y apoyar la toma de decisiones.

## Teoría

> Nota de transparencia: esta sección se redactó con apoyo de IA a partir del lineamiento temático del profesor. Revisar y ajustar antes de usar en clase.

Las medidas de tendencia central son valores que resumen un conjunto de datos mediante un número representativo, ubicado hacia el centro de la distribución. Las tres principales son la media, la mediana y la moda.

**1. Media aritmética**

Es el promedio de los datos: la suma de todos los valores dividida entre el número de observaciones. Utiliza toda la información del conjunto, pero es sensible a los valores extremos.

Fórmula para datos no agrupados:

$$\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}$$

Fórmula para datos agrupados en una tabla de frecuencias:

$$\bar{x} = \frac{\sum (f_i \cdot m_i)}{n}$$

Donde:
- x̄ = media muestral (para la población se usa μ)
- xᵢ = cada valor observado
- n = número total de observaciones
- fᵢ = frecuencia de cada clase
- mᵢ = marca de clase (punto medio del intervalo)

**2. Mediana**

Es el valor que divide los datos ordenados en dos mitades iguales: 50% de las observaciones queda por debajo y 50% por encima. No se ve afectada por valores extremos, por lo que es preferible en distribuciones asimétricas (por ejemplo, ingresos o precios de vivienda).

Procedimiento: ordenar los datos de menor a mayor y aplicar:
- Si *n* es impar: Me = valor en la posición (n + 1) / 2
- Si *n* es par: Me = (valor en la posición n/2 + valor en la posición (n/2)+1) / 2

Fórmula para datos agrupados:

$$Me = L_i + \frac{\left(\frac{n}{2} - F_a\right)}{f_m} \cdot c$$

Donde:
- Li = límite inferior de la clase mediana
- n = total de observaciones
- Fa = frecuencia acumulada de la clase anterior a la mediana
- fm = frecuencia de la clase mediana
- c = amplitud del intervalo

**3. Moda**

Es el valor que aparece con mayor frecuencia. Un conjunto puede ser amodal (sin moda), unimodal (una moda), bimodal (dos) o multimodal (más de dos). Es la única medida aplicable a datos cualitativos (por ejemplo, la marca más vendida).

Fórmula para datos no agrupados: Mo = valor con mayor frecuencia absoluta.

Fórmula para datos agrupados:

$$Mo = L_i + \frac{d_1}{d_1 + d_2} \cdot c$$

Donde:
- Li = límite inferior de la clase modal (la de mayor frecuencia)
- d1 = diferencia entre la frecuencia de la clase modal y la de la clase anterior
- d2 = diferencia entre la frecuencia de la clase modal y la de la clase siguiente
- c = amplitud del intervalo

**Relación entre las tres medidas**

- Distribución normal (simétrica): media = mediana = moda, y las tres coinciden en el centro de la campana.
- Asimetría positiva (cola a la derecha): moda < mediana < media.
- Asimetría negativa (cola a la izquierda): media < mediana < moda.

## Ejercicio / caso práctico

> Esta sección no estaba en el borrador original — se agregó para que el ejercicio tenga un caso numérico concreto, siguiendo el formato del resto del repositorio. Revísala y ajústala libremente.

Una sucursal registró el número de clientes atendidos durante 9 días hábiles:

| Día | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Clientes atendidos | 18 | 22 | 19 | 25 | 22 | 20 | 22 | 60 | 21 |

(El día 8 coincidió con una promoción especial, lo que disparó la afluencia ese día.)

**Se pide:**

1. Calcula la media aritmética del número de clientes atendidos por día.
2. Calcula la mediana.
3. Determina la moda y clasifica la distribución (amodal, unimodal, bimodal o multimodal).
4. Compara las tres medidas: ¿por qué difieren tanto la media respecto a la mediana y la moda? Identifica el valor atípico y explica su efecto.
5. Si tuvieras que reportarle a la gerencia "cuántos clientes atiende la sucursal en un día típico", ¿qué medida usarías y por qué?

## Solución / guía de solución

**1. Media:**

Suma = 18+22+19+25+22+20+22+60+21 = 229; n = 9

$$\bar{x} = \frac{229}{9} \approx 25.4 \text{ clientes}$$

**2. Mediana:**

Datos ordenados: 18, 19, 20, 21, 22, 22, 22, 25, 60

Como n = 9 (impar), Me = valor en la posición (9+1)/2 = posición 5 → **Me = 22**

**3. Moda:**

El valor 22 aparece 3 veces (más que cualquier otro) → **Mo = 22** — distribución **unimodal**.

**4. Comparación:**

La media (25.4) es claramente mayor que la mediana y la moda (ambas en 22), porque el día 8 (60 clientes) es un **valor atípico** que arrastra el promedio hacia arriba. La mediana y la moda, al no verse afectadas por valores extremos, reflejan mejor el comportamiento "normal" de la sucursal.

**5. Recomendación:**

Para describir el día típico conviene usar la **mediana** (o la moda, que coincide): ambas indican que, en un día normal, la sucursal atiende alrededor de 22 clientes, sin que el día de la promoción distorsione esa lectura. La media sigue siendo útil para otros fines (por ejemplo, calcular el total esperado de clientes en el mes), pero no para describir "lo típico" cuando hay valores atípicos.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el prompt que corresponda en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

```
Prompt para la media
"Actúa como profesor de estadística descriptiva. Calcula la media aritmética
del siguiente conjunto de datos: [insertar datos]. Muestra la fórmula
utilizada, sustituye los valores paso a paso, presenta el resultado final e
interpreta su significado en el contexto de [describir el contexto, por
ejemplo, ventas mensuales de una empresa]. Indica también si hay valores
atípicos que puedan distorsionar el resultado."

Prompt para la mediana
"Actúa como profesor de estadística descriptiva. Calcula la mediana del
siguiente conjunto de datos: [insertar datos]. Ordena primero los datos de
menor a mayor, indica si n es par o impar, aplica la fórmula correspondiente
paso a paso, presenta el resultado e interpreta su significado en el
contexto de [describir el contexto]. Explica en qué casos la mediana sería
más representativa que la media para estos datos."

Prompt para la moda
"Actúa como profesor de estadística descriptiva. Determina la moda del
siguiente conjunto de datos: [insertar datos]. Elabora la tabla de
frecuencias, identifica el valor o valores con mayor frecuencia, indica si
la distribución es amodal, unimodal, bimodal o multimodal, e interpreta el
resultado en el contexto de [describir el contexto]."

Prompt para gráfico de distribución normal
"Genera una imagen de una distribución normal (campana de Gauss) con media
de [100] y desviación estándar de [15]. Marca con líneas verticales de
distinto color la media, la mediana y la moda, y agrega una leyenda que
identifique cada una. Como en una distribución normal las tres coinciden en
el centro, colócalas sobre el mismo punto y añade etiquetas con flechas
para que se distingan. Incluye un título, nombres en los ejes (valores de
la variable y frecuencia o densidad) y una explicación breve de por qué en
esta distribución media, mediana y moda son iguales."
```

**Documentos a adjuntar:** opcional — puedes adjuntar un archivo de Excel con tus propios datos para que la IA calcule las tres medidas directamente sobre ellos. No es indispensable, ya que los datos del caso caben en el prompt.

## Recursos adicionales

- Archivo de Excel con datos *(por agregar)*
- Lectura sugerida: *Introducción a la probabilidad y estadística*, Mendenhall, Beaver y Beaver, 14ª edición, 2015, Cengage Learning.
