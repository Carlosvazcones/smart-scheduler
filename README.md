# Scheduler Web Application

## Descripción del proyecto

Este proyecto consiste en una aplicación web sencilla para gestionar tareas basadas en condiciones meteorológicas. Permite al usuario:

* Registrar nuevas tareas con nombre y ciudad asociada.
* Listar tareas guardadas.
* Obtener información meteorológica actual para la ciudad de cada tarea (temperatura, viento, condición).
* Calcular un puntaje (score) que indica la adecuación del clima para la tarea, según preferencias de temperatura mínima/máxima, tolerancia a lluvia y viento máximo.

La arquitectura está dividida en dos componentes principales:

1. **Backend**: API construida con FastAPI, Python y Docker.
2. **Frontend**: Interfaz web estática servida por Nginx (sin usar Angular).

---

## Backend (FastAPI)

### Ubicación del código

* Carpeta raíz: `smart-scheduler`
* Código principal: `app/main.py`
* Servicios:

  * `app/services/weather.py` (integración con OpenWeatherMap)
  * `app/services/score.py` (lógica de cálculo de puntaje)

### Pasos para ejecutar localmente

1. **Variables de entorno**

   * Crear archivo `firebase-service-account.json` en la raíz con las credenciales de Firebase (opcional).
2. **Instalación de dependencias**

   ```bash
   cd smart-scheduler
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   ```
3. **Configuración de CORS**

   * Se habilitó `CORSMiddleware` en `app/main.py` para permitir peticiones desde `http://localhost:4200`(frontend estático).
4. **Levantar servidor**

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
5. **Pruebas unitarias**

   ```bash
   pytest -q
   ```

### Dockerización

1. Ejecutar:

   ```bash
   docker compose up --build -d
   ```
2. Ver estado:

   ```bash
   docker compose ps
   ```

---

## Frontend (Sencillo, sin framework)

### Ubicación de archivos

* Directorio estático: `frontend/`
* Archivo principal HTML: `frontend/index.html`
* Script JS: `frontend/main.js`
* Estilos: `frontend/styles.css`

### Detalles de implementación

* **HTTP API**: Todas las llamadas se hacen usando `fetch` a `http://localhost:8000`.
* **Carga de tareas**: Función `loadTasks()` en `main.js`.
* **Formulario**: Elemento `<form id="task-form">` con listeners en JS.
* **Presentación**: Lista en `<ul id="task-list">` y resultado de score en `<div id="score-result">`.

#POR QUE NO USE ANGULAR?

## Errores y decisiones de diseño

Durante el desarrollo se evaluó usar Angular para el frontend, pero se presentaron múltiples errores recurrentes asociados a componentes standalone, configuración de `app.module.ts` y problemas de rutas. Para cumplir con la entrega y tener una solución funcional en el tiempo disponible, se optó por una interfaz mínima en JavaScript puro.

---

## Entrega del proyecto

* **Repositorio**: Estructura con carpetas `app/`, `frontend/`, `docker-compose.yml`, `Dockerfile` y `requirements.txt`.
* **Documentación**: Este README.md.



