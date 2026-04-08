# Guía de Uso - Actividades: Práctica Complementaria

Esta carpeta contiene ejercicios prácticos que complementan el aprendizaje de las clases principales, enfocándose en el uso de librerías externas y lógica de programación aplicada.

## Contenido de la Carpeta

A continuación se detalla el funcionamiento del script incluido:

### Traductor Multilenguaje (`Traductor.py`)
Un programa interactivo que permite realizar traducciones rápidas entre varios idiomas.
*   **Funcionamiento**: Utiliza la librería `deep_translator` para conectarse con el servicio de Google Translate.
*   **Características Principales**:
    - Idiomas Soportados: Español, Inglés, Francés y Alemán.
    - Interfaz de Consola: Menús numerados para seleccionar el idioma de origen y destino.
    - Validaciones: Controla que el texto no sea demasiado largo (máx. 25 caracteres) y que los idiomas de origen y destino no sean el mismo.
*   **Cómo usar**: Ejecuta el archivo y sigue las instrucciones del menú para elegir los idiomas y escribir el texto que deseas traducir.

## Requisitos
Este programa requiere la instalación de la librería `deep_translator`. Puedes instalarla ejecutando:
```bash
pip install deep-translator
```

## Cómo Ejecutar el Código
1. Asegúrate de tener Python instalado y la librería `deep-translator`.
2. Abre una terminal en esta carpeta.
3. Ejecuta el script usando el comando:
   ```bash
   python Traductor.py
   ```
