# Administración de Inventario

**Carrera:** Contador Público
**Materia:** Aplicar Administración de las Finanzas
**Tema:** Administración de Inventario
**Nivel:** Intermedio
**Duración estimada:** 50 min

## Objetivo de aprendizaje

Al terminar este ejercicio, el alumno podrá calcular el **lote económico de pedido (EOQ)**, el **punto de reorden** (con y sin inventario de seguridad) para una política de inventario, e interpretar la relación de ambos conceptos con el enfoque **Justo a Tiempo (JIT)** como filosofía de reducción de inventarios.

## Teoría

> Nota de transparencia: la explicación teórica fue redactada por el profesor y ampliada/pulida con apoyo de IA; el planteamiento del caso y los criterios de decisión son responsabilidad del profesor.

La administración de inventarios busca equilibrar dos costos que se mueven en direcciones opuestas: el **costo de ordenar** (hacer más pedidos implica más costos administrativos y de flete, pero pedidos más pequeños) y el **costo de mantener inventario** (almacenaje, seguros, obsolescencia, costo de oportunidad del capital invertido en inventario).

**Cantidad Económica de Pedido (EOQ — Economic Order Quantity):**

```
EOQ = √(2 · D · S / H)
```

Donde:
- `D` = demanda anual (unidades)
- `S` = costo de ordenar por pedido
- `H` = costo de mantener una unidad en inventario durante un año

El EOQ determina el tamaño de pedido que **minimiza la suma del costo total de ordenar y de mantener inventario**.

**Número de pedidos al año y frecuencia entre pedidos:**

```
Número de pedidos por año = D / EOQ
Días entre pedidos = 365 / Número de pedidos por año
```

**Punto de reorden (ROP — Reorder Point):** es el nivel de inventario en el cual se debe colocar un nuevo pedido, considerando el tiempo que tarda en llegar (tiempo de entrega o *lead time*):

```
ROP = d · L
```

Donde `d` es la demanda diaria promedio (`D / 365`) y `L` es el tiempo de entrega en días. Si la empresa quiere protegerse contra variaciones en la demanda o retrasos del proveedor, se añade un **inventario de seguridad (SS — Safety Stock)**:

```
ROP con inventario de seguridad = (d · L) + SS
```

**Justo a Tiempo (JIT):** es una filosofía de administración de inventarios que busca reducir al mínimo posible (idealmente a cero) el inventario mantenido, recibiendo materiales justo cuando se necesitan en el proceso productivo. JIT no sustituye el cálculo del EOQ o el punto de reorden, sino que busca **reducir drásticamente el costo de ordenar** (mediante relaciones de largo plazo con proveedores, pedidos frecuentes y pequeños, y entregas muy confiables), lo cual —de acuerdo con la propia fórmula del EOQ— reduce el tamaño óptimo de pedido y, por tanto, el inventario promedio que la empresa necesita mantener.

## Ejercicio / caso práctico

Una empresa comercializadora tiene una demanda anual de **7,200 unidades** de un producto. El costo de colocar cada pedido (administrativo, flete, recepción) es de **$150 por pedido**, y el costo de mantener una unidad en inventario durante un año es de **$4 por unidad**.

El tiempo de entrega (*lead time*) del proveedor es de **6 días**, y la empresa quiere mantener un inventario de seguridad de **20 unidades** para protegerse de variaciones en la demanda.

Se pide:

1. Calcular el EOQ (lote económico de pedido).
2. Calcular cuántos pedidos al año se colocarían con ese EOQ, y cada cuántos días (en promedio) se haría un pedido.
3. Calcular el punto de reorden sin inventario de seguridad.
4. Calcular el punto de reorden incluyendo el inventario de seguridad.
5. Explicar, en el contexto de este caso, cómo cambiaría el EOQ si la empresa migrara hacia una filosofía JIT y lograra reducir su costo de ordenar `S`.

## Solución / guía de solución

**1. EOQ**

```
EOQ = √(2 × 7,200 × 150 / 4) = √540,000 ≈ 734.85 unidades
```

Se redondea a **735 unidades** por pedido (en la práctica se redondea al entero conveniente según la unidad de empaque del producto).

**2. Número de pedidos al año y días entre pedidos**

```
Número de pedidos = 7,200 / 734.85 ≈ 9.80 pedidos al año
Días entre pedidos = 365 / 9.80 ≈ 37.25 días
```

Es decir, la empresa colocaría un pedido aproximadamente cada **37 días**, unas **10 veces al año**.

**3. Punto de reorden sin inventario de seguridad**

```
d (demanda diaria) = 7,200 / 365 ≈ 19.73 unidades/día
ROP = d × L = 19.73 × 6 ≈ 118.36 unidades
```

La empresa debería colocar un nuevo pedido cuando el inventario disponible llegue a aproximadamente **118 unidades**.

**4. Punto de reorden con inventario de seguridad**

```
ROP con SS = 118.36 + 20 = 138.36 unidades
```

Considerando el inventario de seguridad, el punto de reorden sube a aproximadamente **138 unidades**.

**5. Efecto de migrar hacia JIT**

La fórmula del EOQ muestra que `EOQ` es directamente proporcional a la raíz cuadrada de `S` (el costo de ordenar). Si la empresa adopta una filosofía JIT y, mediante acuerdos de largo plazo con proveedores, sistemas electrónicos de pedido y mayor confiabilidad logística, logra **reducir su costo de ordenar** (por ejemplo, de $150 a $20 por pedido), el nuevo EOQ sería:

```
EOQ_JIT = √(2 × 7,200 × 20 / 4) = √72,000 ≈ 268.33 unidades
```

Un EOQ mucho menor (de ~735 a ~268 unidades) implica pedidos más pequeños y frecuentes, lo que reduce el inventario promedio que la empresa mantiene y, con ello, el costo de mantenimiento total — justo el objetivo de JIT. Sin embargo, esta reducción solo es sostenible si la empresa también logra mantener **lead times cortos y confiables**, pues de lo contrario el riesgo de quedarse sin inventario (y su costo asociado) aumentaría.

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Copia y pega el siguiente prompt en Claude o ChatGPT, sustituyendo los datos por los de tu propio caso.

```
Actúa como un asesor en administración de operaciones e inventarios. Tengo una empresa con demanda anual de 7,200 unidades de un producto, costo de ordenar de $150 por pedido, y costo de mantener inventario de $4 por unidad al año. El tiempo de entrega del proveedor es de 6 días, y quiero mantener un inventario de seguridad de 20 unidades.

1. Calcula el EOQ (lote económico de pedido).
2. Calcula cuántos pedidos al año se harían y cada cuántos días, en promedio.
3. Calcula el punto de reorden sin inventario de seguridad y con inventario de seguridad.
4. Explica cómo cambiaría el EOQ si, al adoptar una filosofía Justo a Tiempo (JIT), lograra reducir el costo de ordenar a $20 por pedido, y qué implicaciones tiene esto para el inventario promedio de la empresa.

Muestra el procedimiento y las fórmulas utilizadas, no solo el resultado final.
```

**Documentos a adjuntar:** Ninguno — todos los datos del caso (demanda anual, costo de ordenar, costo de mantener, lead time e inventario de seguridad) caben en el prompt.

## Recursos adicionales

- Plantilla de Excel para calcular EOQ, número de pedidos, punto de reorden e inventario de seguridad ante distintos escenarios de demanda y lead time.
- Lectura sugerida: modelos de inventario determinísticos (EOQ) frente a filosofías de administración esbelta de inventarios (JIT, Kanban).
