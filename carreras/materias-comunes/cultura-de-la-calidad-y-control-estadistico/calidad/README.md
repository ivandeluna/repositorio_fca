---
titulo: Herramientas de Calidad
carrera: Materias Comunes
materia: Cultura de la Calidad y Control Estadístico
tema: Despliegue de la Función de calidad
nivel: Introductorio
duracion_estimada: 50 minutos
tipo: Ejercicio práctico
modalidad: Equipos
entregable_alumno: Reporte con la casa de la calidad y el análisis de los resultados
autor: Isela Carrera
fecha: 2026-11-05
asistencia_ia: "El ejemplo lo genera Gemini "
revisado_por_docente: false
---
# [Nombre del ejercicio/método]

**Carrera:** [Contador Público / Comercio Exterior y Aduanas / Administración de Empresas]
**Materia:** [Cultura de la Calidad y Control estadístico]
**Tema:** [Despliegue de la Función Calidad QFD]
**Nivel:** [Introductorio]
**Duración estimada:** [50 min]

## Objetivo de aprendizaje

[Aprender a utlizar la herramienta del Despliegue de la Calidad (QFD) como herramienta de mejora continua]

## Teoría

> Nota de transparencia: indicar aquí qué partes de esta sección fueron redactadas por el profesor y cuáles se apoyaron en IA (ej. "redacción base del profesor, ampliada y pulida con IA").

[El Despligue de La Función de Calidad es una herramienta que se usa en el Control Total de la Calidad para ayudar en los objetivos de la mejora continua. El QFD es una matriz cuyos renglones se pone principalmente las necesidades o requeriimientos del cliente, y en las columnas se pone de encabezado las especificaciones posibles a modificar. Se hace una relacion de ponderación entre que especificación y requerimiento tiene mayor relación, 9 muy fuerte, 3 mediana, 1 debil y 0 ninguna. La necesidad tiene tambén una ponderación, una vez teniendo esta ponderación se debe de multiplicar para sacar la de cada casilla y sumarla el total por cada fila. La suma total dirá que especificación es la más necesarios]

## Ejercicio / caso práctico

[Complete la casa de la calidad de un problema de Manufactura de  buje o rodamiento de bronce sinterizado autolubricado.] 
[1.	Llene con la ponderación la relación entre las especificaciones y la necesidad del cliente. Para llenar esta casa de la calidad puede consultar con búsqueda en internet que tanta relación existe entre la necesidad del cliente y las especificaciones] [
[2.	Saque la ponderación y súmela al final de cada columna.]
[3.	Indique si hay especificaciones que puedan afcetar positivamente o negativamente entre ellas que seria el tejado de la casa nada mas cheque 5] 
[4.	Saque las conclusiones]

 Requerimientos del Cliente / Ensamble (QUÉS) | Importancia (1-5) | Rugosidad superficial Ra (↓) | Concentricidad / Tolerancia geométrica (↓) | Dureza del material (↑) | Porosidad volumétrica (○) | Impregnación de aceite (↑) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ajuste preciso sin holgura ni vibración** | 5 | 9 &nbsp; 5*9=45 | | | | |
| **Baja fricción y deslizamiento suave** | 5 | 9 | | | | |
| **Larga vida útil sin desgaste prematuro** | 4 | | | | | |
| **Bajo nivel de ruido operacional** | 3 | | | | | |
| **Resistencia a deformación bajo carga** | 4 | | | | 9, 9*4= 38 | |
| **Puntaje técnico absoluto** | — | | | | | |
| **Importancia relativa (%)** | — | | | | | |
| **Especificación meta (Tolerancia)** | — | $Ra \le 0.4\ \mu\text{m}$ | Runout $\le 0.015\text{ mm}$ | 85 a 95 HB | $18\% \pm 2\%$ | $\ge 90\%\text{ vol. de poros}$ |

## Solución / guía de solución

[Opcional — se puede omitir del README.md público y poner en un archivo `solucion.md` aparte si no se quiere exponer a los alumnos.]

## Prompt sugerido para hacerlo con Claude o ChatGPT

> Me puedes decir si existe relación entre la Rugosidad Superficial de un rodamiento y su ajuste preciso sin holgura ni vibración y que importancia tiene del 1 al 9

```
[Prompt sugerido — reemplazar con el prompt real del ejercicio]
```¨¨


**Documentos a adjuntar:** [indicar si se requiere adjuntar algún documento, p. ej. "se sugiere agregar el estado de resultados de la empresa" — o escribir "Ninguno: los datos del caso se pueden pegar directamente en el prompt" si no aplica]

## Recursos adicionales

- [Plantillas, lecturas, datasets de apoyo, enlaces]

---
*Al terminar, crea también un `metadata.yml` en la misma carpeta (ver ejemplo en `carreras/contador-publico/aplicar-administracion-finanzas/ciclo-conversion-efectivo/metadata.yml`) y agrega este ejercicio a la tabla del README.md de su materia.*
