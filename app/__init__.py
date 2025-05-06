from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias de extensiones
db = SQLAlchemy()
migrate = Migrate()  # Instancia de Flask-Migrate

def create_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)
    
    # Configuración de seguridad
    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui_123'  # Obligatorio para CSRF
    
    # Configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mar_de_flores.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)  # Configurar Flask-Migrate

    # Registrar el Blueprint
    from .routes import main  # Importa el Blueprint
    app.register_blueprint(main)  # Registra el Blueprint en la aplicación

    return app
