# insert_sample.py
from datetime import date
from app import create_app, db
from app.models import Reserva

app = create_app()

with app.app_context():
    nueva_reserva = Reserva(
        name="Alejandro",
        first_surname="González",
        second_surname="Pérez",
        gender="Masculino",
        date_of_birth=date(1990, 5, 20),
        id_number="12345678A",
        nationality="Española",
        residence="Gran Canaria",
        mobile_phone="600123456",
        email="alejandro@example.com",
        check_in=date(2025, 7, 1),
        check_out=date(2025, 7, 10),
        payment_type="Tarjeta",
        payment_holder="Alejandro González",
        contract_reference="REF12345"
    )
    db.session.add(nueva_reserva)
    db.session.commit()
    print("✅ Reserva de ejemplo insertada con éxito.")
