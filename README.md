# Pharmacy Inventory API - Core Backend

El sistema está diseñado con una arquitectura orientada a servicios (desacoplada). Utiliza UUIDs como identificadores principales para permitir la futura integración de microservicios externos (como módulos de ventas o analíticas) sin comprometer la integridad referencial de la base de datos.

## Requisitos Previos

- Python 3.10 o superior
- pip (Gestor de paquetes de Python)

## Instrucciones de Ejecución Local

Sigue estos pasos en orden para inicializar el proyecto en tu máquina local.

**1. Clonar el repositorio y acceder al directorio**
`git clone <URL_DEL_REPOSITORIO>`
`cd pharmacy_project`

**2. Crear el entorno virtual**
Es obligatorio aislar las dependencias del proyecto.
`python3 -m venv venv`

**3. Activar el entorno virtual**
- En macOS y Linux:
  `source venv/bin/activate`
- En Windows (Command Prompt):
  `venv\Scripts\activate.bat`
- En Windows (PowerShell):
  `.\venv\Scripts\Activate.ps1`

**4. Instalar las dependencias**
`pip install -r requirements.txt`

**5. Inicializar la base de datos local**
El archivo `db.sqlite3` está excluido del control de versiones. Debes crear tu propia instancia local de la base de datos aplicando las migraciones existentes.
`python manage.py migrate`

**6. Levantar el servidor de desarrollo**
`python manage.py runserver`

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Documentación de la API

Una vez que el servidor esté corriendo, puedes consultar los contratos de los endpoints y probar las peticiones directamente desde la interfaz generada por Swagger.

- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
- **Esquema OpenAPI:** `http://127.0.0.1:8000/api/schema/`

## Notas de Integración para Microservicios

- **Desacoplamiento:** El modelo `Stock` no tiene una relación restrictiva de llave foránea hacia `Medicine`. Utiliza un campo `UUIDField` simple (`medicine_id`).
- **Transacciones Seguras:** Para descontar inventario desde un servicio externo, no se debe manipular la tabla `Stock` directamente. Se debe enviar una petición POST al endpoint transaccional `/api/v1/stock/reduce_stock/` proporcionando el `medicine_id` y el `quantity`. El backend gestionará la reducción en base al modelo FIFO (Primeras Entradas, Primeras Salidas).