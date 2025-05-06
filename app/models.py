from app import db

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    first_surname = db.Column(db.String(100), nullable=False)
    second_surname = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    id_number = db.Column(db.String(20), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    residence = db.Column(db.String(100), nullable=False)
    mobile_phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    payment_type = db.Column(db.String(50), nullable=False)
    payment_holder = db.Column(db.String(100), nullable=False)
    contract_reference = db.Column(db.String(100), nullable=True)

