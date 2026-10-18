# Prompts — costo real de la rotacion de personal

> Copiar y pegar en Claude o ChatGPT, **en orden**. No adelantes el prompt 2.

### Prompt 1 — primera respuesta (paso 1)

```
Actúa como analista de recursos humanos.

[pega aquí el renglón de tu empresa del archivo datos.csv, con encabezados]
Nómina anual del área = plantilla × salario mensual × 12

Calcula:
1. El índice de rotación del año.
2. El costo por separación DESGLOSADO en sus cuatro componentes:
   reclutamiento, capacitación, productividad perdida durante la curva
   de aprendizaje, y tiempo de supervisión adicional.
3. El costo anual total de la rotación.
4. Ese costo como porcentaje de la nómina anual del área.

Muestra la fórmula y la sustitución numérica de cada componente.
Usa únicamente los datos que te entregué: si falta algo, dilo en lugar
de suponerlo. No apliques reglas generales de la literatura.
No me des una recomendación final: esa decisión la tomaré yo.
```

### Prompt 2 — confrontación (paso 3)

```
Revisa tu respuesta anterior:

1. ¿Incluiste los cuatro componentes? Si omitiste alguno, agrégalo.
2. En la productividad perdida, ¿multiplicaste por
   (1 − productividad promedio)? Muestra la operación completa.
3. ¿Usaste alguna cifra que yo no te haya entregado? Señálala.
4. Calcula qué porcentaje del costo total representa cada componente.

Después responde: si el índice de rotación de otra empresa fuera el doble
que el de ésta, ¿su costo de rotación sería necesariamente mayor?
Explica de qué depende.
```

### Prompt 3 — construir el tablero (paso 4)

```
Genera un tablero en UN SOLO archivo HTML, autocontenido, sin librerías
externas ni conexión a internet. Debe abrirse en cualquier navegador y
poderse imprimir.

Datos:
[pega aquí el contenido de datos.csv]
Nómina anual del área = plantilla × salario mensual × 12

El tablero debe tener:
1. Selector de empresa y CONTROLES EDITABLES para: días de curva de
   aprendizaje, productividad durante la curva y número de separaciones.
2. Cuatro indicadores arriba: índice de rotación, costo anual total,
   costo como % de la nómina, y % del costo que no tiene factura.
3. Barras horizontales de los cuatro componentes, en azul los que tienen
   factura y en rojo los costos de oportunidad, con su % del total.
4. Dos barras comparando lo que la empresa registra en contabilidad
   contra lo que de verdad cuesta, con la diferencia marcada.
5. Tabla de las cinco empresas con todos los componentes.

Reglas:
- No inventes ningún dato: todos los números salen de los datos que te di.
- Dibuja los gráficos en SVG generado por ti. No uses librerías ni imágenes.
- Los controles deben recalcular TODO al instante, sin recargar la página.
```

---

**Nota para el alumno:** si la IA te pide datos que no tienes, dilo en la hoja de trabajo. Que los pida es buena señal; que los invente, no.

---

**Norma P. Rodríguez-Cándido · Facultad de Contaduría y Administración, Universidad Autónoma de Coahuila, Unidad Torreón · Octubre de 2026**
