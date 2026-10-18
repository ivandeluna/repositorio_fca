# Prompts — El proveedor más barato que puede parar la planta

> Copiar y pegar en Claude o ChatGPT, en orden.


### Prompt 1 — clasificación (paso 1)

Pega **solo** nombre, gasto y fuentes alternativas.

```
Actúa como analista de compras.

Empresa: Industrias del Nazas, metalmecánica, 340 empleados.
Gasto anual de compras: $22,500,000 entre 18 proveedores.

[pega aquí: proveedor | gasto anual | fuentes alternativas]

Mandato de la dirección: [el mandato de tu equipo]

1. Clasifica a los proveedores en categorías A, B y C por porcentaje
   acumulado de gasto (80 % / 95 % / resto). Muestra la tabla ordenada
   con el porcentaje individual y el acumulado.
2. Indica qué porcentaje del gasto concentra el 20 % de los proveedores,
   calculado con estos datos y no con el principio general.
3. Propón un plan para cumplir el mandato: qué proveedores tocarías
   y en qué orden.

Usa únicamente los datos que te entregué. Si necesitas información que
no te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

Ahora sí, pega la tabla completa.

```
Te entrego dos columnas que antes no tenías: semanas de resustitución
y efecto si el suministro se interrumpe.

[pega la tabla completa de los 18]

1. ¿Tu plan anterior proponía tocar a algún proveedor cuyo suministro
   provoque paro parcial o total? Nómbralos uno por uno.
2. Clasifica a los 18 en la matriz de Kraljic (apalancado, estratégico,
   rutinario, cuello de botella). Declara el criterio exacto con el que
   separas riesgo alto de riesgo bajo y aplícalo igual a todos.
3. Para cada proveedor de riesgo alto calcula la exposición:
   semanas de resustitución × $410,000 × factor de efecto
   (paro total = 100 %, paro parcial = 45 %).
4. Ordénalos por exposición y compárala contra su gasto anual.

Después responde: ¿en qué lugar de la clasificación ABC quedó el
proveedor con mayor exposición? ¿Por qué no lo detectaste antes?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos (18 proveedores):
[pega la tabla completa]
Margen de contribución que se pierde por semana de paro: $410,000

El tablero debe contener:

1. Encabezado con el nombre de la empresa y un veredicto general
   (rojo si hay proveedores en cuello de botella).
2. Cuatro indicadores: gasto anual total, número de proveedores en
   cuello de botella, exposición total, y la razón entre la exposición
   mayor y el gasto de ese proveedor.
3. CONTROLES EDITABLES para margen semanal de paro, umbral de fuentes
   y umbral de semanas. Al cambiar cualquiera, TODO se recalcula.
4. Matriz de Kraljic con los 18 ubicados: eje X riesgo de suministro,
   eje Y gasto anual en escala logarítmica, tamaño del punto
   proporcional al gasto, rojo si el riesgo es alto.
5. Barras de exposición por proveedor, de mayor a menor, con la razón
   exposición/gasto de cada uno.
6. Curva de Pareto del gasto acumulado, marcando dónde cae el 20 % de
   los proveedores y qué porcentaje del gasto concentra realmente.
7. Panel de alertas generado automáticamente para cada cuello de botella.
8. Tabla de los 18 con ABC, cuadrante y exposición, resaltando los
   cuellos de botella.

Reglas de cálculo:
- ABC por porcentaje acumulado: A hasta 80 %, B hasta 95 %, C el resto.
- Riesgo alto si: fuentes <= umbral, O semanas >= umbral, O efecto de paro.
- Exposición = semanas × margen semanal × factor de efecto
  (paro total 1.00, paro parcial 0.45, los demás 0).
- No inventes ningún dato: todos los números salen de la tabla.

Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
```

---

**Norma P. Rodríguez-Cándido · Facultad de Contaduría y Administración, Universidad Autónoma de Coahuila, Unidad Torreón · Octubre de 2026**
