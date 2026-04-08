# Guía para Crear y Ejecutar el Contenedor Docker en "Clase 05"

Esta guía explica paso a paso cómo configurar y ejecutar el contenedor Docker para la carpeta "Clase 05" de este proyecto.

## Paso 1: Instalar Docker
Si no tienes Docker instalado en tu sistema:
1. Ve al sitio web oficial de Docker: https://www.docker.com/get-started
2. Descarga la versión correspondiente a tu sistema operativo (Windows, macOS o Linux).
3. Ejecuta el instalador y sigue las instrucciones para completar la instalación.
4. Reinicia tu computadora si es necesario.
5. Verifica la instalación abriendo una terminal y ejecutando `docker --version`.

## Paso 2: Instalar Extensiones de VS Code
Para trabajar con Docker en Visual Studio Code:
1. Abre VS Code.
2. Ve a la pestaña de Extensiones (icono de cuadrados en la barra lateral izquierda).
3. Busca e instala la extensión "Docker" de Microsoft.
4. Opcionalmente, instala "Docker Compose" si planeas usar archivos compose.

## Paso 3: Abrir el Proyecto en VS Code
1. Abre VS Code.
2. Ve a "File" > "Open Folder" y selecciona la carpeta "Actividades-DevOps" (o la carpeta raíz del proyecto).
3. Navega a la subcarpeta "Clase 05" en el explorador de archivos de VS Code.
V
## Paso 4: Agregar Archivos Docker al Espacio de Trabajo
1. Presiona `Ctrl + Shift + P` para abrir la paleta de comandos.
2. Escribe y selecciona "Containers: Add Docker Files to Workspace".
3. Selecciona "Python: General" como plantilla.
4. Confirma diciendo "Sí" cuando se te pregunte si deseas continuar.
5. Espera a que se ejecute el proceso y se generen los archivos Docker necesarios.

## Paso 5: Modificar requirements.txt
1. Abre el archivo `requirements.txt` en la carpeta "Clase 05".
2. Agrega `pandas` a la lista de dependencias para asegurar que el import sea correcto.
3. Guarda el archivo.

## Paso 6: Ejecutar con Debug
1. En VS Code, abre el archivo `archivo.py`.
2. Ve a la vista de Debug (icono de insecto en la barra lateral).
3. Selecciona la configuración de debug para Python (o crea una nueva si no existe).
4. Haz clic en "Run and Debug" para ejecutar el archivo en modo debug.

## Paso 7: Agregar un Breakpoint y Verificar
1. En el archivo `archivo.py`, haz clic en el margen izquierdo de la última línea para agregar un breakpoint (aparecerá un punto rojo).
2. Ejecuta nuevamente en modo debug.
3. El programa se detendrá en el breakpoint, permitiéndote inspeccionar variables y ver qué sucede.

## Notas Adicionales
- Asegúrate de que Docker esté ejecutándose antes de intentar construir o ejecutar contenedores.
- Si encuentras problemas con los imports, verifica que `pandas` esté correctamente instalado en el entorno.
- Para usar Docker Compose, puedes ejecutar `docker-compose up` en la terminal para los archivos `compose.yaml` o `compose.debug.yaml`.