> **Hoja del alumno.** No contiene la solución.

# Costo real de la rotación de personal

**Carrera:** Administración de Empresas
**Materia:** Administración de Recursos Humanos
**Tema:** Rotación de personal y su impacto financiero
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el costo total de la rotación de personal de una empresa descomponiéndolo en sus cuatro componentes (reclutamiento, capacitación, productividad perdida durante la curva de aprendizaje y tiempo de supervisión); verificar críticamente si el asistente de IA omitió o duplicó alguno de ellos; y fundamentar una recomendación de inversión en retención comparándola contra el costo que evita.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; desarrollo de la fórmula de productividad perdida, casos por sector y guía de solución con apoyo de IA. Pendiente de revisión docente.

La **rotación de personal** es la proporción de trabajadores que dejan la organización en un periodo respecto a la plantilla promedio:

$$\text{Índice de rotación} = \frac{\text{Separaciones del periodo}}{\text{Plantilla promedio}} \times 100$$

El índice por sí solo no dice nada sobre el impacto económico. Una rotación de 30 % en un puesto que se aprende en una semana cuesta poco; la misma rotación en un puesto que tarda cuatro meses en alcanzar productividad plena puede comprometer el resultado del ejercicio.

El costo de una separación se descompone en cuatro componentes:

**1. Costo de reclutamiento y reemplazo.** Publicación de vacantes, horas de reclutador, exámenes y estudios socioeconómicos, trámites de alta y baja, finiquito administrativo. Es el componente más visible y el único que casi todas las empresas registran.

**2. Costo de capacitación e inducción.** Horas de instructor, materiales, certificaciones, equipo de protección, y el tiempo del propio trabajador en formación.

**3. Productividad perdida durante la curva de aprendizaje.** Un trabajador nuevo no rinde desde el primer día: alcanza el desempeño pleno después de un periodo que depende del puesto. Durante ese lapso la empresa paga el salario completo y recibe una fracción del rendimiento:

$$\text{Productividad perdida} = \text{Separaciones} \times \text{Días de curva} \times \text{Salario diario} \times (1 - \text{Productividad promedio del periodo})$$

Donde el **salario diario** = salario mensual / 30.

**4. Tiempo de supervisión adicional.** Horas que el jefe directo y los compañeros experimentados dedican a acompañar, corregir y repetir instrucciones, en lugar de a su propio trabajo.

**El punto que suele pasarse por alto.** Los componentes 1 y 2 se registran en la contabilidad: hay facturas y recibos. Los componentes 3 y 4 **no aparecen en ninguna cuenta**, porque son costos de oportunidad, no desembolsos. Por eso la mayoría de las empresas —y la mayoría de las respuestas de un asistente de IA— subestiman de forma sistemática el costo de la rotación.

El costo total suele expresarse como porcentaje de la nómina anual del área, que es la cifra con la que la dirección puede compararlo contra el costo de un programa de retención.

## Ejercicio / caso práctico

En equipos, cada uno trabaja con **una** de las siguientes empresas (ficticias), asignada por el profesor:

| # | Empresa | Sector | Plantilla | Separaciones del año | Salario mensual promedio | Días de curva de aprendizaje | Productividad promedio durante la curva |
|---|---------|--------|-----------|----------------------|--------------------------|------------------------------|------------------------------------------|
| 1 | **Lácteos La Comarca** | Alimentos | 180 | 47 | $9,800 | 75 | 45 % |
| 2 | **Mezclilla Lagunera** | Manufactura textil | 240 | 96 | $7,400 | 45 | 55 % |
| 3 | **Autopartes Gómez** | Metalmecánica | 320 | 58 | $11,200 | 90 | 40 % |
| 4 | **Distribuidora Laguna** | Distribución | 95 | 29 | $10,500 | 60 | 50 % |
| 5 | **Clínica Cerro de las Noas** | Servicios de salud | 130 | 21 | $16,800 | 120 | 35 % |

Costos unitarios por separación, iguales para todas las empresas salvo donde se indica:

| Concepto | Lácteos | Mezclilla | Autopartes | Distribuidora | Clínica |
|----------|---------|-----------|------------|---------------|---------|
| Reclutamiento y reemplazo | $6,200 | $3,800 | $9,400 | $5,600 | $12,500 |
| Capacitación e inducción | $8,500 | $4,200 | $14,000 | $6,800 | $19,000 |
| Horas de supervisión adicional | 22 h | 14 h | 30 h | 18 h | 26 h |
| Costo por hora de supervisión | $320 | $260 | $410 | $340 | $520 |

**Se pide:**

1. **Calcular con la IA (≈10 min).** Usa el prompt sugerido con los datos de tu empresa. Pídele el índice de rotación, el costo por separación desglosado, el costo anual total y su peso sobre la nómina.

2. **Verificar a la IA (≈15 min).** Revisa componente por componente y llena la tabla. Marca cualquier componente que la IA haya omitido, duplicado o calculado con la fórmula equivocada.

    | Componente | ¿Lo incluyó la IA? | Monto de la IA | Tu recálculo | ¿Coincide? | Qué pasó |
    |------------|--------------------|----------------|--------------|------------|----------|
    | Reclutamiento y reemplazo | | | | | |
    | Capacitación e inducción | | | | | |
    | Productividad perdida | | | | | |
    | Supervisión adicional | | | | | |
    | **Total anual** | | | | | |

    Al terminar, responde: **¿qué porcentaje del costo total representa el componente que la IA omitió o calculó mal?**

3. **Decidir (≈10 min).** La dirección evalúa un programa de retención con un costo anual del 2 % de la nómina, que según el proveedor reduciría la rotación a la mitad. En 5–6 líneas, recomienda si conviene o no, usando tu cifra corregida. Indica al menos un supuesto del proveedor que no estás dispuesto a dar por bueno.

4. **Plenaria (≈10 min).** Cada equipo presenta su cifra total y el error de la IA más interesante que encontró. Se contrasta por qué la empresa con la rotación más alta no es necesariamente la que más pierde.

## Prompt sugerido para hacerlo con Claude o ChatGPT

Copia y pega el siguiente prompt, sustituyendo los datos entre corchetes por los de tu empresa.

```
Actúa como analista de recursos humanos.

Empresa: [nombre]
Sector: [sector]
Plantilla promedio: [n] trabajadores
Separaciones en el año: [n]
Salario mensual promedio: $[monto]
Días que tarda un trabajador nuevo en alcanzar productividad plena: [n]
Productividad promedio durante ese periodo: [%]
Costo de reclutamiento y reemplazo por separación: $[monto]
Costo de capacitación e inducción por separación: $[monto]
Horas de supervisión adicional por trabajador nuevo: [n] h
Costo por hora de supervisión: $[monto]
Nómina anual del área: [plantilla × salario mensual × 12]

Calcula:
1. El índice de rotación del año.
2. El costo por separación, DESGLOSADO en sus cuatro componentes:
   reclutamiento, capacitación, productividad perdida durante la curva
   de aprendizaje, y tiempo de supervisión adicional.
3. El costo anual total de la rotación.
4. Ese costo como porcentaje de la nómina anual del área.

Muestra la fórmula y la sustitución numérica de cada componente.
Usa únicamente los datos que te entregué: si falta algo, dilo en lugar
de suponerlo. No apliques reglas generales de la literatura.
No me des una recomendación final: esa decisión la tomaré yo.
```

**Prompt de seguimiento (verificación)**

```
Revisa tu respuesta anterior:

1. ¿Incluiste los cuatro componentes? Si omitiste alguno, agrégalo.
2. En la productividad perdida, ¿multiplicaste por (1 − productividad
   promedio)? Muestra la operación completa.
3. ¿Usaste alguna cifra que yo no te haya entregado? Señálala.
4. Calcula qué porcentaje del costo total representa cada componente.

Después responde: si el índice de rotación de otra empresa fuera el doble
que el de ésta, ¿su costo de rotación sería necesariamente mayor?
Explica de qué depende.
```

📎 **Documentos a adjuntar:** Ninguno: los datos del caso se pueden pegar directamente en el prompt. Si el equipo trabaja con una empresa real, se sugiere adjuntar el reporte de altas y bajas del periodo y el tabulador de sueldos del área, con los datos personales suprimidos.

## Recursos adicionales

- Cascio, W. F. y Boudreau, J. W. (2011). *Investing in People: Financial Impact of Human Resource Initiatives* (2.ª ed.). Pearson Education / FT Press.
- Cascio, W. F. (2000). *Costing Human Resources: The Financial Impact of Behavior in Organizations* (4.ª ed.). South-Western College Publishing.
- Chiavenato, I. (2020). *Administración de recursos humanos: el capital humano de las organizaciones* (11.ª ed.). McGraw-Hill.
- `tablero-rotacion.html` — **tablero de referencia ya funcionando.** Ábrelo y cambia los días de curva o la productividad.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** desarrollo de la fórmula de productividad perdida, construcción de los cinco casos, prompts, tabla de errores típicos y rúbrica; pendiente de revisión docente.
