from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ReservationForm(FlaskForm):
    # Información personal
    name = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    first_surname = StringField('Primer Apellido', validators=[DataRequired(), Length(max=100)])
    second_surname = StringField('Segundo Apellido', validators=[Length(max=100)])
    gender = SelectField('Sexo', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], validators=[DataRequired()])
    date_of_birth = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    id_number = StringField('Número de Documento', validators=[DataRequired(), Length(max=20)])
    nationality = StringField('Nacionalidad', validators=[DataRequired(), Length(max=100)])
    residence = StringField('Lugar de Residencia', validators=[DataRequired(), Length(max=100)])
    mobile_phone = StringField('Teléfono Móvil', validators=[DataRequired(), Length(max=15)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])

    # Datos de la transacción
    check_in = DateField('Fecha de Entrada', format='%Y-%m-%d', validators=[DataRequired()])
    check_out = DateField('Fecha de Salida', format='%Y-%m-%d', validators=[DataRequired()])
    payment_type = StringField('Tipo de Pago', validators=[DataRequired(), Length(max=50)])
    payment_holder = StringField('Titular del Pago', validators=[DataRequired(), Length(max=100)])
    contract_reference = StringField('Número de Referencia del Contrato', validators=[Length(max=100)])

    # Botón de envío
    submit = SubmitField('Confirmar Reserva')