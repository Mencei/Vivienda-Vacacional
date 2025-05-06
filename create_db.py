from app import create_app, db
from app.models import Reserva

app = create_app()  # Llama a la función para crear la app

with app.app_context():
    db.create_all()
    print("✅ Base de datos creada con éxito")
