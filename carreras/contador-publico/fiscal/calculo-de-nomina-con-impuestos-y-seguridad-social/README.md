# Cálculo de nómina con impuestos y seguridad social

**Carrera:** Contador Público
**Materia:** Fiscal
**Tema:** Cálculo de nómina con impuestos
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular la nómina semanal de un trabajador aplicando la normatividad laboral, fiscal y de seguridad social vigente en México: determinará las percepciones (incluidos tiempo extra, descanso laborado, faltas y vacaciones), separará los ingresos gravados y exentos, calculará el ISR por sueldos y salarios con la tarifa y el subsidio aplicables, las cuotas obrero-patronales del IMSS, las aportaciones al INFONAVIT y el Impuesto Sobre Nóminas, para obtener el sueldo neto del trabajador y el costo total para el patrón. Además, verificará críticamente el resultado que entregue un asistente de IA contra las fuentes oficiales.

## Teoría

> *Nota de transparencia: redacción teórica elaborada con apoyo de IA y verificada contra las fuentes oficiales citadas (LFT, LISR, LSS, Anexo 8 de la RMF 2026 y publicaciones en el DOF). Los valores corresponden a 2026; actualizarlos cada año antes de usar el ejercicio en clase.*

### 1. Estructura de una nómina

Una nómina se calcula en cuatro pasos:

1. **Percepciones:** todo lo que el patrón paga al trabajador en el periodo (sueldo, tiempo extra, primas, premios, etc.), menos los descuentos por faltas.
2. **Gravado y exento:** cada percepción se separa en la parte que causa ISR y la parte exenta, según el artículo 93 de la LISR.
3. **Deducciones al trabajador:** ISR retenido (con el subsidio para el empleo, si aplica) y cuotas obreras del IMSS. El resultado es el **sueldo neto**.
4. **Costo para el patrón:** percepciones + cuotas patronales del IMSS + SAR/retiro + cesantía y vejez + INFONAVIT + Impuesto Sobre Nóminas (estatal).

### 2. Conceptos laborales (Ley Federal del Trabajo)

- **Salario diario y por hora.** Para una jornada diurna de 8 horas, el salario por hora es el salario diario entre 8. El salario semanal comprende 7 días, porque incluye el pago del día de descanso (art. 69).
- **Tiempo extra (reforma publicada en el DOF el 1 de mayo de 2026).** El nuevo art. 66 permite distribuir el tiempo extra en hasta 4 horas diarias y un máximo de 4 días a la semana, pagado con un **100 % más** (pago doble). Conforme al artículo cuarto transitorio, el máximo semanal de horas extra a pago doble es de **9 horas en 2026 y 2027**, 10 en 2028, 11 en 2029 y 12 en 2030. Las horas que excedan ese límite (hasta 4 adicionales por semana) se pagan con un **200 % más** (pago triple), según el art. 68. La suma de jornada ordinaria y extraordinaria nunca puede exceder 12 horas diarias.
- **Descanso semanal laborado.** Si el trabajador labora su día de descanso sin que se le dé otro en sustitución, recibe, además del salario de ese día, un **salario doble** (art. 73).
- **Prima dominical.** Quien trabaja en domingo recibe una prima adicional de al menos **25 %** sobre su salario diario (art. 71).
- **Faltas injustificadas.** No se paga el día no laborado y, cuando el trabajador no labora todos los días de la semana, se le paga solo la parte proporcional del día de descanso (art. 72). En una semana de 6 días hábiles, cada falta descuenta **1 día + 1/6 del día de descanso**.
- **Vacaciones y prima vacacional.** Desde la reforma de 2023 ("vacaciones dignas"), el trabajador tiene 12 días de vacaciones al cumplir un año, 14 al cumplir dos, **16 al cumplir tres**, 18 al cumplir cuatro y 20 al cumplir cinco (art. 76). Los días de vacaciones se pagan con salario normal y, además, se paga una prima vacacional de al menos **25 %** sobre el salario de esos días (art. 80).
- **Aguinaldo:** mínimo 15 días de salario al año (art. 87). No se paga en este ejercicio, pero sí entra en el cálculo del factor de integración.

### 3. ISR por sueldos y salarios (LISR)

**Ingresos exentos (art. 93) que aplican en este caso:**

| Concepto | Exención |
|---|---|
| Tiempo extra a pago doble y descanso semanal laborado (fr. I) | Para trabajadores que ganan más del salario mínimo: el **50 %** de lo pagado, siempre que no se rebasen los límites de la LFT, con un tope de **5 UMA por semana** (ambos conceptos juntos). Las horas triples rebasan el límite laboral y son totalmente gravadas. |
| Prima dominical (fr. XIV) | Hasta **1 UMA** por cada domingo laborado. |
| Prima vacacional (fr. XIV) | Hasta **15 UMA** en el año. |
| Premios de asistencia y puntualidad | No tienen exención: son totalmente gravados. |

**Retención semanal.** Al ingreso gravado de la semana se le aplica la tarifa del art. 96 para periodos de 7 días, publicada en el Anexo 8 de la RMF 2026:

ISR = (base gravable − límite inferior) × % sobre el excedente + cuota fija

**Subsidio para el empleo.** Por decreto publicado en el DOF el 31 de diciembre de 2025, desde febrero de 2026 equivale al **15.02 % de la UMA mensual** ($535.65 al mes) y se aplica solo a quien percibe ingresos mensuales de hasta **$11,492.66**. En periodos menores a un mes, el monto mensual se divide entre 30.4 y se multiplica por los días del periodo. Si el subsidio es mayor que el ISR, la diferencia no se entrega al trabajador.

### 4. Seguridad social (LSS y Ley del INFONAVIT)

**Salario base de cotización (SBC).** Se integra con el salario diario y las prestaciones (art. 27 LSS). Para prestaciones fijas se usa el **factor de integración**:

Factor = (365 + días de aguinaldo + días de vacaciones × % de prima vacacional) / 365

SBC = salario diario × factor (con tope de 25 UMA)

No integran el SBC los premios de asistencia y de puntualidad, siempre que cada uno no rebase el 10 % del SBC (fr. VII), ni el tiempo extra dentro de los márgenes de la LFT (fr. IX). Lo que sí rebasa esos límites es un **elemento variable**: se suma y se promedia en el bimestre, y se integra al SBC del bimestre siguiente (art. 30).

**Cuotas obrero-patronales 2026** (porcentaje sobre el SBC por día cotizado, salvo la cuota fija):

| Ramo | Patrón | Trabajador | Fundamento |
|---|---:|---:|---|
| Enfermedades y maternidad: cuota fija (sobre UMA) | 20.40 % | — | Art. 106 fr. I |
| Enfermedades y maternidad: excedente de 3 UMA | 1.10 % | 0.40 % | Art. 106 fr. II |
| Prestaciones en dinero | 0.70 % | 0.25 % | Art. 107 |
| Gastos médicos de pensionados | 1.05 % | 0.375 % | Art. 25 |
| Riesgo de trabajo | prima de la empresa | — | Arts. 71–74 |
| Invalidez y vida | 1.75 % | 0.625 % | Art. 147 |
| Guarderías y prestaciones sociales | 1.00 % | — | Art. 211 |
| Retiro | 2.00 % | — | Art. 168 fr. I |
| Cesantía en edad avanzada y vejez | 3.150 % a 7.513 % según SBC (7.513 % desde 4.01 UMA) | 1.125 % | Art. 168 fr. II y transitorios (DOF 16-12-2020) |
| INFONAVIT | 5.00 % | — | Art. 29 Ley del INFONAVIT |

**Faltas injustificadas.** En ausencias menores de 8 días, solo se cotiza el seguro de enfermedades y maternidad (art. 31 LSS). Los demás ramos y el INFONAVIT se calculan sin los días de falta.

### 5. Impuesto Sobre Nóminas (Coahuila)

Es un impuesto estatal a cargo del patrón. En Coahuila la tasa es de **3 %** sobre las erogaciones gravadas (art. 24 de la Ley de Hacienda para el Estado de Coahuila de Zaragoza). Entre las exenciones de esa ley están los premios de asistencia y de puntualidad, *siempre que cada uno no rebase el 10 % del salario base*, y el tiempo extra *cuando no rebase tres horas diarias ni tres veces por semana*. Observa que la ley estatal conserva el límite anterior de "tres veces por semana", aunque la LFT ya permite repartir el tiempo extra en cuatro días.

### 6. Valores vigentes 2026

| Concepto | Valor | Fuente |
|---|---:|---|
| UMA diaria (desde el 1 de febrero de 2026) | $117.31 | INEGI |
| UMA mensual | $3,566.22 | INEGI |
| Salario mínimo general (zona general) | $315.04 | CONASAMI, DOF |
| 5 UMA semanales (tope de exención de tiempo extra) | $586.55 | Cálculo: 5 × 117.31 |
| 3 UMA (umbral del excedente de enfermedades y maternidad) | $351.93 | Cálculo: 3 × 117.31 |
| Subsidio para el empleo mensual (15.02 % de la UMA mensual) | $535.65 | Decreto, DOF 31-12-2025 |
| Límite de ingresos mensuales para el subsidio | $11,492.66 | Decreto, DOF 31-12-2025 |
| Tarifa de ISR para 7 días | ver tabla abajo | Anexo 8 RMF 2026, DOF 28-12-2025 |
| Tasa del ISN en Coahuila | 3 % | Ley de Hacienda del Estado de Coahuila, art. 24 |

**Tarifa del art. 96 para pagos de 7 días (2026):**

| Límite inferior | Límite superior | Cuota fija | % sobre el excedente |
|---:|---:|---:|---:|
| 0.01 | 194.46 | 0.00 | 1.92 |
| 194.47 | 1,650.67 | 3.71 | 6.40 |
| 1,650.68 | 2,900.87 | 96.95 | 10.88 |
| 2,900.88 | 3,372.11 | 232.96 | 16.00 |
| 3,372.12 | 4,037.32 | 308.35 | 17.92 |
| 4,037.33 | 8,142.75 | 427.56 | 21.36 |
| 8,142.76 | 12,834.08 | 1,304.45 | 23.52 |
| 12,834.09 | 24,502.45 | 2,407.86 | 30.00 |
| 24,502.46 | 32,669.91 | 5,908.35 | 32.00 |
| 32,669.92 | 98,009.66 | 8,521.94 | 34.00 |
| 98,009.67 | En adelante | 30,737.49 | 35.00 |

## Ejercicio / caso práctico

**Alejandro Martínez** trabaja como auxiliar de almacén en una empresa comercializadora de Torreón, Coahuila. Datos del trabajador y de la empresa:

- Salario diario: **$500.00** (salario por hora: $62.50).
- Jornada diurna de lunes a sábado, de 8:00 a 16:00 horas (8 horas diarias); descansa los domingos.
- Antigüedad: **3 años cumplidos** (16 días de vacaciones). Aguinaldo: 15 días. Prima vacacional: 25 %.
- Premios semanales, calculados sobre el salario semanal de 7 días ($3,500.00):
  - Premio de asistencia: **10 %**. Se pierde en la semana en que hay una falta injustificada (las vacaciones no cuentan como falta).
  - Premio de puntualidad: **12 %**. Alejandro no tuvo retardos en el mes.
- Prima de riesgo de trabajo de la empresa: **1.13065 %**. Entidad: Coahuila (ISN 3 %).
- Periodo: cuatro semanas consecutivas, del lunes 1 al domingo 28 de junio de 2026 (sin días de descanso obligatorio). La nómina se paga semanalmente.

**Semana 1.** Trabajó de lunes a sábado y descansó el domingo; por un aumento en los pedidos hizo horas extra:

| Día | Incidencia |
|---|---|
| Lunes | Jornada normal |
| Martes | Trabajó dos horas adicionales |
| Miércoles | Trabajó dos horas adicionales |
| Jueves | Jornada normal |
| Viernes | Trabajó dos horas adicionales |
| Sábado | Jornada normal |
| Domingo | Descanso |

**Semana 2.** Faltó injustificadamente el martes. La empresa le pidió trabajar el domingo, su día de descanso, sin darle otro día en sustitución.

**Semana 3.** Tomó 5 días de vacaciones (de lunes a viernes), trabajó el sábado y descansó el domingo.

**Semana 4.**

| Día | Incidencia |
|---|---|
| Lunes | Jornada normal |
| Martes | Trabajó tres horas adicionales |
| Miércoles | Trabajó tres horas adicionales |
| Jueves | Trabajó tres horas adicionales |
| Viernes | Trabajó tres horas adicionales |
| Sábado | Falta injustificada |
| Domingo | La empresa le pide trabajar su día de descanso, sin sustitución |

**Se pide** (en equipos; el profesor asigna una semana a cada equipo):

1. **Percepciones (≈10 min).** Calcula todas las percepciones de la semana, incluidos los descuentos por falta. Indica si el tiempo extra respeta los límites de la LFT reformada y cuántas horas se pagan dobles y cuántas triples.
2. **Gravado y exento (≈8 min).** Separa cada percepción en parte gravada y parte exenta de ISR, citando la fracción del art. 93 de la LISR.
3. **ISR y subsidio (≈7 min).** Calcula el ISR semanal con la tarifa de 7 días y determina si procede el subsidio para el empleo.
4. **IMSS, INFONAVIT e ISN (≈10 min).** Calcula el factor de integración y el SBC, las cuotas obreras y patronales de la semana (considera los días de falta) y el ISN.
5. **Resultado y verificación con IA (≈10 min).** Obtén el sueldo neto y el costo para el patrón. Después ejecuta el prompt sugerido (abajo) con los datos de tu semana y compara: ¿qué valores usó la IA (UMA, tarifa, subsidio, tasas)? ¿coinciden con la tabla de valores vigentes 2026? Anota cada diferencia y explica cuál cálculo es el correcto.
6. **Plenaria (≈5 min).** Cada equipo presenta su semana y se arma el resumen del mes.

## Solución / guía de solución

*Guía para el profesor. Cálculos redondeados a dos decimales.*

**Datos base comunes:**

- Factor de integración = (365 + 15 + 16 × 0.25) / 365 = 384 / 365 = **1.0521**
- SBC fijo = 500 × 1.0521 = **$526.03** (equivale a 4.48 UMA, por lo que la tasa patronal de cesantía y vejez es 7.513 %).
- Excedente de 3 UMA = 526.03 − 351.93 = $174.10 diarios.
- **Subsidio para el empleo: no procede.** El límite mensual de $11,492.66 equivale a unos $2,646 por semana (11,492.66 / 30.4 × 7), y Alejandro gana más que eso en todas las semanas.
- En este periodo se cotiza con el SBC fijo. El excedente del premio de puntualidad sobre el 10 % del SBC y las horas triples son elementos variables: se integran al SBC del bimestre siguiente.

### Semana 1: tiempo extra dentro del límite

| Percepción | Importe | Exento ISR | Gravado ISR |
|---|---:|---:|---:|
| Sueldo (7 × 500) | 3,500.00 | — | 3,500.00 |
| Horas extra dobles (6 h × 62.50 × 2) | 750.00 | 375.00 | 375.00 |
| Premio de asistencia (10 %) | 350.00 | — | 350.00 |
| Premio de puntualidad (12 %) | 420.00 | — | 420.00 |
| **Total** | **5,020.00** | **375.00** | **4,645.00** |

Las 6 horas extra están dentro del límite de 9 horas semanales, así que todas son dobles. Exención: 50 % de 750 = 375.00, menor que el tope de 586.55.

ISR = (4,645.00 − 4,037.33) × 21.36 % + 427.56 = 129.80 + 427.56 = **$557.36**

### Semana 2: falta y domingo laborado

| Percepción | Importe | Exento ISR | Gravado ISR |
|---|---:|---:|---:|
| Sueldo (7 × 500) | 3,500.00 | — | 3,500.00 |
| Descuento por falta (1 día) | −500.00 | — | −500.00 |
| Descuento proporcional del día de descanso (500 / 6) | −83.33 | — | −83.33 |
| Descanso laborado: salario doble adicional (2 × 500) | 1,000.00 | 500.00 | 500.00 |
| Prima dominical (25 % × 500) | 125.00 | 117.31 | 7.69 |
| Premio de puntualidad (12 %) | 420.00 | — | 420.00 |
| **Total** | **4,461.67** | **617.31** | **3,844.36** |

Sin premio de asistencia por la falta. ISR = (3,844.36 − 3,372.12) × 17.92 % + 308.35 = 84.63 + 308.35 = **$392.98**

### Semana 3: vacaciones

| Percepción | Importe | Exento ISR | Gravado ISR |
|---|---:|---:|---:|
| Sueldo (7 × 500, incluye 5 días de vacaciones) | 3,500.00 | — | 3,500.00 |
| Prima vacacional (5 × 500 × 25 %) | 625.00 | 625.00 | — |
| Premio de asistencia (10 %) | 350.00 | — | 350.00 |
| Premio de puntualidad (12 %) | 420.00 | — | 420.00 |
| **Total** | **4,895.00** | **625.00** | **4,270.00** |

La prima vacacional queda exenta completa porque es menor que 15 UMA ($1,759.65), suponiendo que no recibió otra prima vacacional en el año. ISR = (4,270.00 − 4,037.33) × 21.36 % + 427.56 = 49.70 + 427.56 = **$477.26**

### Semana 4: horas triples, falta y domingo laborado

| Percepción | Importe | Exento ISR | Gravado ISR |
|---|---:|---:|---:|
| Sueldo (7 × 500) | 3,500.00 | — | 3,500.00 |
| Descuento por falta y proporcional del descanso | −583.33 | — | −583.33 |
| Horas extra dobles (9 h × 62.50 × 2) | 1,125.00 | 586.55* | 1,538.45* |
| Horas extra triples (3 h × 62.50 × 3) | 562.50 | — | 562.50 |
| Descanso laborado: salario doble adicional | 1,000.00 | (incluido en *) | (incluido en *) |
| Prima dominical | 125.00 | 117.31 | 7.69 |
| Premio de puntualidad (12 %) | 420.00 | — | 420.00 |
| **Total** | **6,149.17** | **703.86** | **5,445.31** |

\* El 50 % de horas dobles y descanso laborado es (1,125 + 1,000) / 2 = 1,062.50, pero el tope es de 5 UMA = 586.55. El resto (1,538.45) es gravado.

Las 12 horas extra se reparten en 4 días de 3 horas: es válido con la LFT reformada, pero en 2026 solo 9 horas son dobles; las 3 restantes se pagan triples (art. 68) y son totalmente gravadas. ISR = (5,445.31 − 4,037.33) × 21.36 % + 427.56 = 300.74 + 427.56 = **$728.30**

### Cuotas IMSS e INFONAVIT por semana

Semanas 1 y 3: 7 días cotizados en todos los ramos. Semanas 2 y 4: 7 días en enfermedades y maternidad, y 6 días en los demás ramos y en el INFONAVIT (por la falta).

| Concepto | Semanas 1 y 3 (7 días) | Semanas 2 y 4 (6 días*) |
|---|---:|---:|
| **Trabajador:** E. y M. excedente (174.10 × 0.40 % × 7) | 4.87 | 4.87 |
| Prestaciones en dinero (0.25 %) | 9.21 | 9.21 |
| Gastos médicos de pensionados (0.375 %) | 13.81 | 13.81 |
| Invalidez y vida (0.625 %) | 23.01 | 19.73 |
| Cesantía y vejez (1.125 %) | 41.42 | 35.51 |
| **Total cuotas obreras** | **92.32** | **83.13** |
| **Patrón:** E. y M. cuota fija (117.31 × 20.40 % × 7) | 167.52 | 167.52 |
| E. y M. excedente (1.10 %) | 13.41 | 13.41 |
| Prestaciones en dinero (0.70 %) | 25.78 | 25.78 |
| Gastos médicos de pensionados (1.05 %) | 38.66 | 38.66 |
| Riesgo de trabajo (1.13065 %) | 41.63 | 35.69 |
| Invalidez y vida (1.75 %) | 64.44 | 55.23 |
| Guarderías y prestaciones sociales (1 %) | 36.82 | 31.56 |
| Retiro (2 %) | 73.64 | 63.12 |
| Cesantía y vejez (7.513 %) | 276.64 | 237.12 |
| INFONAVIT (5 %) | 184.11 | 157.81 |
| **Total patronal** | **922.65** | **825.90** |

\* Enfermedades y maternidad (cuota fija, excedente, prestaciones en dinero y gastos médicos de pensionados) se cotiza los 7 días.

### Impuesto Sobre Nóminas (Coahuila, 3 %)

| Semana | Percepciones | Exento ISN | Base | ISN |
|---|---:|---:|---:|---:|
| 1 | 5,020.00 | 1,100.00 (horas extra 750 + asistencia 350) | 3,920.00 | 117.60 |
| 2 | 4,461.67 | — | 4,461.67 | 133.85 |
| 3 | 4,895.00 | 350.00 (asistencia) | 4,545.00 | 136.35 |
| 4 | 6,149.17 | — (horas extra en 4 días: rebasa "tres veces por semana") | 6,149.17 | 184.48 |

El premio de asistencia (exactamente 10 %) no rebasa el límite y queda exento. El de puntualidad (12 %) lo rebasa: aquí se toma como gravado completo, por la redacción literal de la ley estatal.

### Resumen del mes

| Concepto | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Total |
|---|---:|---:|---:|---:|---:|
| Percepciones | 5,020.00 | 4,461.67 | 4,895.00 | 6,149.17 | 20,525.84 |
| ISR retenido | 557.36 | 392.98 | 477.26 | 728.30 | 2,155.90 |
| Cuotas obreras IMSS | 92.32 | 83.13 | 92.32 | 83.13 | 350.90 |
| **Sueldo neto** | **4,370.32** | **3,985.56** | **4,325.42** | **5,337.74** | **18,019.04** |
| Cuotas patronales IMSS, RCV e INFONAVIT | 922.65 | 825.90 | 922.65 | 825.90 | 3,497.10 |
| ISN | 117.60 | 133.85 | 136.35 | 184.48 | 572.28 |
| **Costo total para el patrón** | **6,060.25** | **5,421.42** | **5,954.00** | **7,159.55** | **24,595.22** |

**Puntos de discusión:**

- Por cada peso neto que recibe Alejandro, la empresa desembolsa aproximadamente $1.36 (24,595.22 / 18,019.04).
- En la semana 4 el tope de exención de 5 UMA hace que la mayor parte del tiempo extra y del descanso laborado quede gravada.
- **Criterios que pueden variar:** el descuento proporcional del día de descanso por falta; si el premio de puntualidad que rebasa el 10 % se grava completo o solo en el excedente (ISN e IMSS); el cálculo semanal de las cuotas IMSS, que en la práctica se determinan por mes o por bimestre en el SUA; y si el límite de ingresos del subsidio para el empleo se compara con el ingreso mensualizado o con el gravado.
- **Errores típicos de la IA:** usar la UMA de 2025 ($113.14), las tarifas de ISR de 2023, el subsidio para el empleo anterior a 2024 o el límite de "3 horas, 3 veces por semana" sin considerar la reforma de mayo de 2026.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT. Sustituye los datos entre corchetes por los de tu semana o los de tu propio caso.

```
Eres un contador público especialista en nómina en México, con dominio de la
Ley Federal del Trabajo (LFT), la Ley del Impuesto Sobre la Renta (LISR), la
Ley del Seguro Social (LSS), la Ley del INFONAVIT y la Resolución Miscelánea
Fiscal (RMF) del ejercicio 2026.

Calcula la nómina de un trabajador, desde las percepciones hasta el sueldo
neto y el costo total para el patrón, aplicando la normatividad laboral y
fiscal vigente en México.

# Datos
- Ejercicio fiscal: 2026
- Periodo de pago: semanal (7 días), semana [n] de junio de 2026
- Salario diario: $500.00; jornada diurna de 8 horas, de lunes a sábado
- Antigüedad: 3 años cumplidos (16 días de vacaciones)
- Aguinaldo: 15 días. Prima vacacional: 25 %
- Premios semanales sobre salario de 7 días: asistencia 10 % (se pierde si
  hay falta injustificada), puntualidad 12 %
- Incidencias de la semana: [describe día por día: horas extra, faltas,
  vacaciones, descanso laborado sin sustitución]
- Otras deducciones: ninguna
- Prima de riesgo de trabajo de la empresa: 1.13065 %
- Entidad federativa: Coahuila (Impuesto Sobre Nóminas)

# Marco normativo a considerar
1. LFT: arts. 66 y 68 reformados (DOF 1-may-2026) y su artículo cuarto
   transitorio sobre el máximo semanal de horas extra; arts. 69, 71, 72 y 73
   (descanso semanal, prima dominical, faltas, descanso laborado); arts. 76
   y 80 (vacaciones y prima vacacional); art. 87 (aguinaldo).
2. LISR: art. 93 (exenciones), art. 94 (ingresos por salarios), art. 96
   (retención y tarifa de 7 días del Anexo 8 de la RMF 2026).
3. Subsidio para el empleo: decreto vigente en 2026.
4. LSS e INFONAVIT: integración del SBC (arts. 27 y 30), cuotas por ramo,
   ausencias (art. 31), cesantía y vejez patronal según la tabla de 2026.
5. ISN: Ley de Hacienda para el Estado de Coahuila (tasa y exenciones).

# Procedimiento (sigue este orden y muestra cada cálculo)
1. Determina los valores vigentes: salario mínimo, UMA diaria y mensual,
   porcentaje y límite de ingresos del subsidio para el empleo, y tarifa
   semanal del art. 96. Búscalos en fuentes oficiales actuales; no los des
   por sabidos de memoria. Cita la fuente de cada valor.
2. Calcula las percepciones del periodo e indica si el tiempo extra respeta
   los límites de la LFT y cuántas horas son dobles y cuántas triples.
3. Separa cada percepción en gravada y exenta, aplicando los límites en UMA.
4. Calcula el factor de integración y el SBC (tope de 25 UMA).
5. Calcula el ISR: base gravable, límite inferior, excedente, porcentaje y
   cuota fija. Indica si procede el subsidio para el empleo.
6. Calcula las cuotas obreras del IMSS por ramo.
7. Calcula las cuotas patronales del IMSS, retiro, cesantía y vejez,
   INFONAVIT y el ISN.
8. Obtén el sueldo neto del trabajador y el costo total para el patrón.

# Formato de la respuesta
- Resumen de datos y supuestos utilizados.
- Tabla de valores vigentes con su fuente.
- Tablas de percepciones (gravado/exento), deducciones, cuotas patronales y
  resultados finales.
- Cada fórmula escrita con los números sustituidos.
- Sección final de observaciones y advertencias: criterios que pueden
  variar, datos que conviene confirmar y diferencias entre fuentes.

# Reglas
- Usa pesos mexicanos con dos decimales.
- No inventes tasas, tablas ni montos. Si no puedes confirmar un valor, dilo
  y explica cómo obtenerlo.
- Redacta en español, con lenguaje claro y nivel de licenciatura.
- Indica que el resultado es un ejercicio de cálculo y no sustituye la
  asesoría de un contador público.
```

**Prompt de seguimiento (para la verificación):**

```
Compara los valores que usaste con estos valores oficiales de 2026:
UMA diaria $117.31; UMA mensual $3,566.22; subsidio para el empleo 15.02 %
de la UMA mensual con límite de ingresos de $11,492.66 mensuales; tarifa de
7 días del Anexo 8 de la RMF 2026 (adjunta); ISN de Coahuila 3 %.
Si alguno no coincide, rehaz el cálculo y explica qué cambió en el resultado.
```

**Documentos a adjuntar:** se sugiere adjuntar el **Anexo 8 de la RMF 2026** (tarifas de ISR), descargable del portal del SAT, para que la IA no use tarifas de años anteriores. Si se trabaja con un caso real, agregar también el recibo de nómina o la lista de incidencias del periodo.

## Recursos adicionales

- Ley Federal del Trabajo, reforma publicada en el DOF el 1 de mayo de 2026 (jornada de 40 horas y tiempo extra): [Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_ref52_01may26.pdf).
- Anexo 8 de la RMF 2026 (tarifas de ISR), DOF 28-12-2025: [SAT](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf).
- Ley del Impuesto Sobre la Renta (arts. 93, 94 y 96), Ley del Seguro Social y Ley del INFONAVIT, en el portal de leyes federales de la Cámara de Diputados.
- Valor de la UMA 2026: INEGI.
- Ley de Hacienda para el Estado de Coahuila de Zaragoza (Impuesto Sobre Nóminas).
