# Prompts — el mejor cliente esta perdiendo dinero

> Copiar y pegar en Claude o ChatGPT, **en orden**. No adelantes el prompt 2.

### Prompt 1 — primera respuesta (paso 1)

```
Actúa como analista comercial.

Distribuidora Industrial Laguna factura $42,100,000 al año entre doce
clientes. Tasa de financiamiento: 18 % anual.

[pega aquí SOLO las columnas: cliente, ventas, margen_bruto_pct]

Mandato de la dirección: [el mandato de tu equipo]

1. Calcula el margen bruto en pesos de cada cliente y ordénalos.
2. Identifica a los clientes más y menos rentables.
3. Propón un plan para cumplir el mandato: a qué clientes te enfocarías
   y a cuáles no.

Usa únicamente los datos que te entregué. Si para responder bien
necesitas información que no te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

```
Te entrego las columnas que antes no tenías: pedidos, líneas por pedido,
entregas, visitas, devoluciones y días de crédito.

[pega el archivo datos.csv completo]

Costos unitarios:
- Procesamiento de pedido: $840 por pedido
- Captura y surtido: $65 por línea de pedido
- Entrega: $1,250 por entrega
- Visita del vendedor: $1,900 por visita
- Gestión de devolución: $3,200 por devolución
Tasa de financiamiento: 18 % anual

1. Calcula para cada cliente: costo de servir, costo financiero
   (ventas × días de crédito × 18 % / 365) y margen neto.
2. Ordena a los clientes por margen bruto y por margen neto, lado a lado.
3. Señala cuántos lugares se movió cada uno.
4. Identifica a los clientes con margen neto negativo.

Después responde: ¿tu plan anterior se enfocaba en algún cliente que
destruye valor? ¿Por qué no lo detectaste?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos:
[pega aquí el contenido de datos.csv]
Costos unitarios: pedido $840, línea $65, entrega $1,250, visita $1,900, devolución $3,200. Tasa 18 % anual.

El tablero debe tener:
1. CONTROLES EDITABLES para los cinco costos unitarios y la tasa.
2. Cuatro indicadores: ventas totales, margen bruto total, margen neto
   total y número de clientes que destruyen valor.
3. CURVA DE BALLENA: clientes ordenados de mayor a menor margen neto,
   con la utilidad acumulada; marca dónde alcanza su máximo.
4. Ranking doble lado a lado: por margen bruto y por margen neto, con
   líneas que conecten al mismo cliente para ver cuánto se movió.
5. Barras de descomposición por cliente: margen bruto, costo de servir,
   costo financiero y margen neto.
6. Tabla de los doce con todas las columnas, resaltando los negativos.

Reglas:
- No inventes ningún dato: todos los números salen de los datos que te di.
- Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
- Los controles deben recalcular TODO al instante, sin recargar la página.
```

---

**Nota para el alumno:** si la IA te pide datos que no tienes, dilo en la hoja de trabajo. Que los pida es buena señal; que los invente, no.

---

**Norma P. Rodríguez-Cándido · Facultad de Contaduría y Administración, Universidad Autónoma de Coahuila, Unidad Torreón · Octubre de 2026**
