> **Hoja del alumno.** No contiene la solución.

# El margen cae y nadie sabe por qué

**Carrera:** Administración de Empresas
**Materia:** Administración Estratégica
**Tema:** Balanced Scorecard, indicadores de resultado e inductores de actuación
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá distinguir un indicador de resultado de un inductor de actuación dentro de un Balanced Scorecard; trazar la cadena causa-efecto que conecta las cuatro perspectivas hasta un deterioro financiero; verificar críticamente si el asistente de IA ubicó el origen en la perspectiva donde solo se manifiesta el síntoma; y proponer una acción correctiva sobre la causa, con su costo comparado contra el daño que evita.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; construcción del tablero, cadena causal y guía de solución con apoyo de IA. Pendiente de revisión docente.

### Las cuatro perspectivas y su orden

El Balanced Scorecard organiza los indicadores en cuatro perspectivas que **no están al mismo nivel**: se encadenan.

$$\text{Aprendizaje y crecimiento} \rightarrow \text{Procesos internos} \rightarrow \text{Cliente} \rightarrow \text{Financiera}$$

La perspectiva financiera es la **última** de la cadena. Todo lo que aparece ahí es consecuencia de algo que ocurrió antes, en alguna de las otras tres. Por eso un estado financiero siempre llega tarde: informa de un daño que se produjo meses atrás.

### Indicador de resultado contra inductor de actuación

- Un **indicador de resultado** mide qué pasó. Llega tarde y no se puede accionar directamente: margen, rentabilidad, días de cartera, participación de mercado.
- Un **inductor de actuación** mide algo que, si cambia hoy, modifica el resultado mañana: horas de capacitación, número de preparaciones, costo de no calidad, rotación de personal.

El error clásico de gestión es **actuar sobre el indicador de resultado**. Reforzar cobranza cuando los días de cartera suben es el ejemplo perfecto: si el cliente paga tarde porque le entregaron tarde, meter dos cobradores no cambia nada.

### Cómo se lee un tablero

No se lee indicador por indicador. Se lee buscando **si los que están en rojo forman una cadena**. Cuatro indicadores en rojo repartidos al azar son cuatro problemas; cuatro indicadores en rojo encadenados son **un solo problema** visto en cuatro momentos distintos.

## Ejercicio / caso práctico

**Industrias del Nazas, S.A. de C.V.**, metalmecánica de Torreón, 340 empleados, ventas de $218,000,000. Implantó un Balanced Scorecard hace un año.

Las ventas crecieron 11.2 %, por encima de la meta de 8 %. El margen operativo cayó de 11.4 % a 9.8 % en seis meses. El director general no entiende por qué.

**Lo que la dirección ya intentó:**

- Reforzar cobranza con dos personas. Los días de cartera siguieron subiendo.
- Negociar precio con los proveedores de lámina. Se logró 3 %, sin efecto visible.
- Congelar contrataciones y **recortar a la mitad el presupuesto de capacitación**.

### Tablero al cierre del semestre

| Perspectiva | Indicador | Meta | Real | Estado |
|-------------|-----------|------|------|--------|
| **Financiera** | Margen operativo | 12.0 % | 9.8 % | 🔴 |
| | Rendimiento sobre capital | 18.0 % | 16.4 % | 🟡 |
| | Días de cartera | 45 d | 62 d | 🔴 |
| | Crecimiento en ventas | 8.0 % | 11.2 % | 🟢 |
| **Cliente** | Índice de satisfacción | 90 pts | 87 pts | 🟡 |
| | Retención de clientes | 92.0 % | 94.1 % | 🟢 |
| | Entregas completas y a tiempo | 95.0 % | 88.6 % | 🔴 |
| | Participación de mercado | 14.0 % | 13.2 % | 🟡 |
| **Procesos internos** | Ciclo de pedido | 5.0 d | 7.4 d | 🔴 |
| | Merma de producción | 2.0 % | 2.6 % | 🟡 |
| | Rotación de inventario | 8.0 x | 6.9 x | 🟡 |
| | Costo de no calidad | 1.5 % | 2.9 % | 🔴 |
| **Aprendizaje** | Horas de capacitación por empleado | 24 h | 17 h | 🔴 |
| | Rotación de personal | 12.0 % | 15.8 % | 🟡 |
| | Puestos clave cubiertos | 90.0 % | 92.0 % | 🟢 |
| | Índice de clima laboral | 80 pts | 78 pts | 🟡 |

### Datos complementarios del periodo

| Concepto | Hace 6 meses | Actual |
|----------|--------------|--------|
| Ventas anualizadas | $196,000,000 | $218,000,000 |
| Utilidad de operación | $22,344,000 | $21,364,000 |
| Reprocesos y garantías | $3,920,000 | $6,322,000 |
| Fletes urgentes por retraso | $840,000 | $2,180,000 |
| Presupuesto de capacitación | $1,600,000 | $800,000 |
| Personal con menos de 1 año de antigüedad | 18 % | 31 % |

**Se pide (cinco pasos):**

---

### Paso 1 · Diagnosticar con la IA · 10 min
**Entregable:** la respuesta de la IA, copiada.

Usa el **prompt 1**. Pégale el tablero completo pero **no los datos complementarios**. Pídele que explique por qué cae el margen y que proponga dos acciones correctivas.

---

### Paso 2 · Clasificar los indicadores · 5 min
**Entregable:** una tabla de cinco renglones.

Toma estos **cinco indicadores en rojo** y clasifícalos:

| Indicador en rojo | ¿Resultado o inductor? | ¿Por qué? |
|---|---|---|
| Margen operativo | | |
| Días de cartera | | |
| Entregas completas y a tiempo | | |
| Costo de no calidad | | |
| Horas de capacitación | | |

**Pregunta:** si solo uno de estos se puede accionar hoy, ¿cuál es?

---

### Paso 3 · Trazar la cadena y confrontar · 10 min
**Entregable:** la cadena de cuatro eslabones, dibujada.

El profesor entrega ahora los **datos complementarios**. Usa el **prompt 2** para devolvérselos a la IA.

Dibuja la cadena causa-efecto con flechas, empezando **en la perspectiva donde se origina**:

```
[            ] → [            ] → [            ] → [            ]
```

Y cuantifícala: suma el aumento de reprocesos y el de fletes urgentes. Compáralo contra la caída de la utilidad de operación.

**Responde por escrito:** ¿en qué perspectiva empezó el diagnóstico de la IA? ¿Por qué ahí?

---

### Paso 4 · Construir el tablero · 15 min
**Entregable:** un archivo HTML que funcione.

Usa el **prompt 3** para generar un tablero interactivo con las cuatro perspectivas, sus semáforos y la cadena causal resaltada. Debe permitir **simular**:

1. Restituir el presupuesto de capacitación a $1,600,000. ¿Qué indicadores se mueven y en qué orden temporal?
2. Contratar dos cobradores más. ¿Qué se mueve?
3. ¿Cuál de las dos acciones cambia el margen en doce meses?

> Referencia en `materiales/tablero-bsc.html`.

---

### Paso 5 · Decidir y presentar · 10 min
**Entregable:** 6–8 líneas.

Propón una acción sobre la **causa** y otra sobre el **síntoma**. Para cada una: costo, tiempo hasta ver efecto, y qué indicador del tablero avisaría si está funcionando.

**Plenaria.** Pregunta de cierre: **la dirección recortó capacitación para proteger el margen. ¿Qué efecto tuvo esa decisión sobre el margen?**

---

## Prompts sugeridos

Ver `materiales/03-prompts.md`.

📎 **Documentos a adjuntar:** Ninguno. Si el equipo trabaja con una empresa real, se sugiere adjuntar su tablero de indicadores del último semestre y el estado de resultados comparativo.

## Recursos adicionales

- Kaplan, R. S. y Norton, D. P. (1996). *The Balanced Scorecard: Translating Strategy into Action*. Harvard Business School Press.
- Kaplan, R. S. y Norton, D. P. (2004). *Strategy Maps: Converting Intangible Assets into Tangible Outcomes*. Harvard Business School Press.
- Kaplan, R. S. y Norton, D. P. (1992). The Balanced Scorecard: Measures That Drive Performance. *Harvard Business Review*, 70(1), 71–79.
- `materiales/` — caso para el alumno, hoja de trabajo, prompts, rúbrica, datos en CSV y tablero de referencia.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** construcción del tablero de 16 indicadores, cadena causal, datos complementarios, prompts y rúbrica; pendiente de revisión docente.
