# 🌸 Mar de Flores - Sistema de Reservas

Este proyecto es una aplicación desarrollada en Python y Flask para gestionar reservas de clientes en un entorno web. Utiliza SQLAlchemy como ORM y una base de datos MySQL para almacenar los datos de las reservas.

## 🧱 Tecnologías usadas

- Python 3.x
- Flask
- SQLAlchemy
- MySQL
- Visual Studio Code

## 📦 Estructura del proyecto

/mardeflores
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── templates/
│ └── (archivos HTML)
│
├── .gitignore
├── README.md
└── run.py


## 📋 Modelo de datos

El modelo `Reserva` incluye los siguientes campos:

- `id` (int, PK)
- `name`
- `first_surname`
- `second_surname`
- `gender`
- `date_of_birth`
- `id_number`
- `nationality`
- `residence`
- `mobile_phone`
- `email`
- `check_in`
- `check_out`
- `payment_type`
- `payment_holder`
- `contract_reference`

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/mardeflores.git
   cd mardeflores

Crea un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
flask run
🔒 Conexión con la base de datos
La conexión a MySQL se gestiona desde la configuración de Flask. Asegúrate de incluir tus credenciales de acceso y el nombre de la base de datos (mardeflores.db) en tu config.py o archivo .env.

✅ Estado del proyecto
Proyecto en desarrollo (versión inicial funcional).

📄 Licencia
Este proyecto es de uso educativo y personal.
