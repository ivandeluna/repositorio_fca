> **Hoja del alumno.** No contiene la solución.

# El mejor cliente de la empresa está perdiendo dinero

**Carrera:** Administración de Empresas
**Materia:** Administración de Ventas
**Tema:** Rentabilidad por cliente y costo de servir
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular la rentabilidad neta por cliente incorporando el costo de servir y el costo financiero del crédito; verificar críticamente si el asistente de IA se quedó en el margen bruto; y fundamentar una decisión de depuración o renegociación de cartera distinguiendo entre clientes que destruyen valor y clientes que solo son pequeños.

## Teoría

> ⚠️ **Nota de transparencia:** redacción base del profesor; construcción del caso, cálculo de costos de servir y guía de solución con apoyo de IA. Pendiente de revisión docente.

### Por qué el margen bruto miente

El reporte de ventas de casi cualquier empresa ordena a los clientes por facturación o por margen bruto. Ese margen solo resta el costo de lo vendido, y da por supuesto que **atender a un cliente cuesta lo mismo que atender a otro**. No es cierto.

Un cliente que coloca 186 pedidos al año, pide 44 líneas en cada uno, exige 186 entregas, recibe 22 visitas del vendedor, devuelve 41 veces y paga a 105 días **consume un volumen de recursos radicalmente distinto** de otro que coloca 9 pedidos, recibe 9 entregas y paga a 30 días. Ninguno de esos consumos aparece en el costo de ventas.

### Los tres niveles de margen

$$\text{Margen bruto} = \text{Ventas} - \text{Costo de lo vendido}$$

$$\text{Costo de servir} = \sum (\text{transacciones} \times \text{costo unitario de cada actividad})$$

$$\text{Costo financiero} = \text{Ventas} \times \text{días de crédito} \times \frac{\text{tasa anual}}{365}$$

$$\text{Margen neto por cliente} = \text{Margen bruto} - \text{Costo de servir} - \text{Costo financiero}$$

El costo de servir se construye igual que un costeo por actividades, pero con generadores comerciales: número de pedidos, líneas por pedido, entregas, visitas y devoluciones.

### La curva de ballena

Al ordenar los clientes por margen neto acumulado, suele aparecer una curva que sube, alcanza un máximo y **vuelve a bajar**: la utilidad acumulada llega a superar la utilidad total de la empresa, y los últimos clientes se la comen. Esa forma —conocida como curva de ballena— es la evidencia visual de que hay clientes que destruyen valor mientras figuran como importantes en el reporte de ventas.

La conclusión correcta rara vez es «despidamos a ese cliente». Suele ser renegociar: pedido mínimo, frecuencia de entrega, plazo de pago o precio.

## Ejercicio / caso práctico

**Distribuidora Industrial Laguna, S.A. de C.V.** factura $42,100,000 al año entre doce clientes. Su tasa de financiamiento es del 18 % anual.

| Cliente | Ventas | Margen bruto | Pedidos | Líneas por pedido | Entregas | Visitas | Devoluciones | Días de crédito |
|---------|--------|--------------|---------|-------------------|----------|---------|--------------|------------------|
| Autoservicios del Norte | $8,400,000 | 18.5 % | 96 | 42 | 96 | 24 | 14 | 75 |
| Cadena Hogar Express | $6,900,000 | 15.2 % | 186 | 44 | 186 | 22 | 41 | 105 |
| Grupo Constructor Nazas | $5,600,000 | 21.2 % | 18 | 6 | 18 | 9 | 1 | 60 |
| Industrial Torreón | $4,300,000 | 24.1 % | 24 | 8 | 24 | 11 | 2 | 45 |
| Súper Abastos Lerdo | $3,700,000 | 19.8 % | 92 | 29 | 92 | 16 | 17 | 75 |
| Ferretera La Laguna | $3,200,000 | 26.8 % | 28 | 11 | 28 | 12 | 2 | 45 |
| Mayoreo del Bravo | $2,400,000 | 25.5 % | 31 | 12 | 31 | 13 | 4 | 45 |
| Materiales Gómez | $2,100,000 | 29.5 % | 22 | 9 | 22 | 10 | 3 | 30 |
| Distribuidora Cerro | $1,800,000 | 31.2 % | 14 | 7 | 14 | 6 | 1 | 30 |
| Constructora Peñoles | $1,500,000 | 28.8 % | 12 | 5 | 12 | 7 | 1 | 60 |
| Comercial Matamoros | $1,250,000 | 33.5 % | 11 | 5 | 11 | 5 | 0 | 30 |
| Talleres Unidos | $950,000 | 34.8 % | 9 | 4 | 9 | 4 | 1 | 30 |

**Costos unitarios de las actividades comerciales:**

| Actividad | Generador | Costo unitario |
|-----------|-----------|----------------|
| Procesamiento de pedido | pedido | $840 |
| Captura y surtido de línea | línea de pedido | $65 |
| Entrega | entrega | $1,250 |
| Visita del vendedor | visita | $1,900 |
| Gestión de devolución | devolución | $3,200 |

**Mandato de la dirección.** Uno distinto por equipo:

| Equipo | Instrucción que recibió |
|--------|--------------------------|
| 1 | «Suban las ventas 10 % sin aumentar la fuerza de ventas.» |
| 2 | «Depuren la cartera: queremos menos clientes y más utilidad.» |
| 3 | «Prioricen a los clientes grandes, ahí está el negocio.» |
| 4 | «Reduzcan el capital de trabajo invertido en clientes.» |
| 5 | «Suban la utilidad neta sin perder ningún cliente.» |

**Se pide (cinco pasos):**

---

### Paso 1 · Rankear con la IA · 10 min
**Entregable:** la respuesta de la IA, copiada.

Usa el **prompt 1**. Pégale **solo** las columnas de cliente, ventas y margen bruto. **No le des todavía** las columnas de pedidos, líneas, entregas, visitas, devoluciones ni días de crédito.

Pídele el ranking de clientes y un plan para cumplir el mandato de tu equipo.

---

### Paso 2 · Anotar la predicción · 5 min
**Entregable:** tres nombres, escritos antes de calcular.

Antes de seguir, escriban en una hoja:

1. ¿Cuál creen que es el cliente **más** rentable de los doce?
2. ¿Cuál el **menos** rentable?
3. ¿Cuántos creen que están **perdiendo** dinero?

Guarden la hoja. Se compara al final.

---

### Paso 3 · Recibir el dato que faltaba · 10 min
**Entregable:** la tabla de margen neto, completa.

El profesor entrega ahora las columnas de actividad y de crédito, y la tabla de costos unitarios. Usa el **prompt 2**.

| Cliente | Margen bruto | Costo de servir | Costo financiero | Margen neto | Margen neto % | Lugar en bruto | Lugar en neto |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

**Responde por escrito:** ¿cuántos lugares se movió el cliente que más cambió de posición? ¿Por qué la IA no pidió estos datos?

---

### Paso 4 · Construir el tablero · 15 min
**Entregable:** un archivo HTML que funcione.

Usa el **prompt 3** para generar un tablero con la curva de ballena, el ranking doble y los controles editables. Ábrelo y prueba:

1. ¿En qué cliente alcanza su máximo la utilidad acumulada?
2. Sube el costo de una entrega de $1,250 a $1,900. ¿Cuántos clientes quedan en negativo?
3. Baja el plazo de Cadena Hogar Express de 105 a 45 días. ¿Alcanza para volverlo rentable?

> Puedes comparar con `materiales/tablero-rentabilidad-clientes.html`. No es «la respuesta correcta»: es una referencia.

---

### Paso 5 · Decidir y presentar · 10 min
**Entregable:** 6–8 líneas.

Reformula el mandato de tu equipo en una propuesta que incluya: qué clientes se renegocian y con qué condición concreta (pedido mínimo, frecuencia de entrega, plazo, precio), cuáles no se tocan, y qué pasaría con la utilidad total si la propuesta funciona.

**Plenaria.** Se comparan las predicciones del paso 2 contra el resultado. Pregunta de cierre: **¿por qué la respuesta no es «dejar de venderle al cliente que pierde»?**

---

## Prompts sugeridos

Ver `materiales/03-prompts.md`, listos para copiar y pegar.

📎 **Documentos a adjuntar:** Ninguno: los datos se pegan directamente. Si el equipo trabaja con una empresa real, se sugiere adjuntar el reporte de ventas por cliente del último ejercicio y, si existe, el registro de pedidos, entregas y devoluciones.

## Recursos adicionales

- Kaplan, R. S. y Narayanan, V. G. (2001). Measuring and Managing Customer Profitability. *Journal of Cost Management*, 15(5), 5–15.
- Kaplan, R. S. y Anderson, S. R. (2007). *Time-Driven Activity-Based Costing*. Harvard Business School Press.
- Cooper, R. y Kaplan, R. S. (1991). Profit Priorities from Activity-Based Costing. *Harvard Business Review*, 69(3), 130–135.
- `materiales/` — caso para el alumno, hoja de trabajo, prompts, rúbrica, datos en CSV y tablero de referencia.

---

**Autor:** Norma P. Rodríguez-Cándido · **Actualizado:** 2026-10-13 · **Asistencia de IA:** construcción del caso de doce clientes, cálculo de costos de servir, prompts, tabla de errores típicos y rúbrica; pendiente de revisión docente.
