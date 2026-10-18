# Prompts — el margen cae y nadie sabe por que

> Copiar y pegar en Claude o ChatGPT, **en orden**. No adelantes el prompt 2.

### Prompt 1 — primera respuesta (paso 1)

```
Actúa como consultor de gestión.

Industrias del Nazas, metalmecánica de Torreón, 340 empleados,
ventas de $218,000,000. Las ventas crecieron 11.2 % y el margen
operativo cayó de 11.4 % a 9.8 % en seis meses.

La dirección ya intentó: reforzar cobranza con dos personas,
negociar el precio de la lámina (logró 3 %) y recortar a la mitad
el presupuesto de capacitación.

[pega aquí el contenido de datos.csv: el tablero de 16 indicadores]

1. Identifica los indicadores fuera de meta.
2. Explica por qué cae el margen operativo aunque las ventas crezcan.
3. Propón dos acciones correctivas.

Usa únicamente los datos del tablero. Si necesitas información que no
te di, dilo en lugar de suponerla.
```

### Prompt 2 — confrontación (paso 3)

```
Te entrego datos complementarios que antes no tenías:

Concepto | Hace 6 meses | Actual
Ventas anualizadas | $196,000,000 | $218,000,000
Utilidad de operación | $22,344,000 | $21,364,000
Reprocesos y garantías | $3,920,000 | $6,322,000
Fletes urgentes por retraso | $840,000 | $2,180,000
Presupuesto de capacitación | $1,600,000 | $800,000
Personal con menos de 1 año | 18 % | 31 %

1. ¿En qué perspectiva del Balanced Scorecard empezó tu diagnóstico
   anterior? ¿Por qué ahí?
2. Traza la cadena causa-efecto completa, de cuatro eslabones,
   empezando por la perspectiva donde se ORIGINA el problema.
3. Clasifica cada indicador en rojo como indicador de resultado o
   inductor de actuación, y justifica.
4. Cuantifica: suma el aumento de reprocesos y el de fletes urgentes,
   y compáralo contra la caída de la utilidad de operación.

Después responde: la dirección recortó capacitación para proteger el
margen. ¿Qué efecto tuvo esa decisión sobre el margen?
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos:
[pega aquí el contenido de datos.csv]
Caída de la utilidad de operación: de $22,344,000 a $21,364,000.

El tablero debe tener:
1. Las cuatro perspectivas con sus 16 indicadores, meta contra real,
   y semáforo verde/ámbar/rojo.
2. La CADENA CAUSA-EFECTO dibujada arriba, con los cuatro eslabones
   conectados por flechas, resaltando los indicadores que la forman.
3. Cuatro indicadores: número de rojos, número de ámbares, caída del
   margen en puntos, y el sobrecosto de reprocesos más fletes.
4. Un SIMULADOR: al restituir el presupuesto de capacitación, mostrar
   qué indicadores se moverían y en qué orden temporal (3, 6, 12 meses),
   marcando claramente que es una proyección y no un dato.
5. Tabla de datos complementarios comparando los dos periodos.

Reglas:
- No inventes ningún dato: todos los números salen de los datos que te di.
- Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
- Los controles deben recalcular TODO al instante, sin recargar la página.
```

---

**Nota para el alumno:** si la IA te pide datos que no tienes, dilo en la hoja de trabajo. Que los pida es buena señal; que los invente, no.

---

**Norma P. Rodríguez-Cándido · Facultad de Contaduría y Administración, Universidad Autónoma de Coahuila, Unidad Torreón · Octubre de 2026**
