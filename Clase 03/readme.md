# Guía de Uso - Clase 03: Listas, Funciones y Lógica de Negocio

En esta clase se profundiza en el manejo de estructuras de datos (listas) y la creación de funciones modulares para resolver problemas específicos.

## Contenido de la Carpeta

A continuación se detalla el funcionamiento del script incluido:

### Gestión de Calificaciones (`Calificaciones.py`)
Un sistema completo para capturar y evaluar el desempeño escolar.
*   **Funcionamiento**: Permite al usuario definir el número de materias, capturar nombres de materias y tres calificaciones por materia (una para cada periodo). Al finalizar la captura, permite consultar los resultados.
*   **Características Principales**:
    - Validaciones: El nombre debe ser alfabético y las calificaciones deben estar entre 0 y 100.
    - Consulta Flexible: Puedes buscar una materia por su nombre o por su número en la lista.
    - Cálculo Automático: Calcula el promedio de los tres periodos y determina si el alumno ha aprobado (promedio >= 60) o reprobado (promedio < 60).
*   **Cómo usar**: Ejecuta el archivo e ingresa el número de materias. Completa la información y realiza las consultas que desees.

## Cómo Ejecutar el Código
1. Asegúrate de tener Python instalado.
2. Abre una terminal en esta carpeta.
3. Ejecuta el script usando el comando:
   ```bash
   python Calificaciones.py
   ```
