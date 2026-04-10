# Actividad 2 de la Clase 06: DockerLive Sync-Container

Este proyecto es un entorno de desarrollo basado en **Docker** diseñado para permitir cambios en tiempo real que se reflejan directamente en `localhost:5002`.

## Propósito
El objetivo de este contenedor es centralizar el flujo de trabajo de cada proyecto, proporcionando una experiencia similar a herramientas como "Go Live" de VS Code, pero con la robustez y aislamiento de un contenedor Docker.

## Características
- **Hot-Reloading**: Cualquier cambio realizado en el código fuente (como en [app.py](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/app.py)) se sincroniza con el contenedor para una actualización inmediata.
- **Entorno Aislado**: Todas las dependencias (definidas en [requirements.txt](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/requirements.txt)) se instalan dentro del contenedor, manteniendo limpia la máquina local.
- **Centralización**: Permite que cada proyecto tenga su propia configuración de servidor y puertos definida en [compose.yaml](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/compose.yaml).

## Cómo usarlo
1. Asegúrate de tener Docker instalado y en ejecución.
2. Levanta el contenedor debugeando el codigo
   ```
3. Abre tu navegador en `http://localhost:5002` (generalmente, al debugear lo abre automáticamente).
4. Realiza cambios en `app.py` y observa cómo se actualizan en el navegador.

## Estructura del Proyecto
- [Dockerfile](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/Dockerfile): Define la imagen base de Python y la configuración del entorno.
- [compose.yaml](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/compose.yaml): Orquesta el despliegue del servicio.
- [app.py](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/app.py): Aplicación Flask principal.
- [requirements.txt](file:///c:/Users/abrah/Documents/GitHub/Actividades-Fundamento-DevOps/Clase%2006/Actividad%202/requirements.txt): Lista de dependencias del proyecto.
