from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Reserva
from app.forms import ReservationForm

main = Blueprint('main', __name__)  # Crea el Blueprint

# Ruta de inicio
@main.route('/')
def inicio():
    """Página de inicio"""
    return render_template('inicio.html')

# Ruta del formulario de reserva
@main.route('/reservar', methods=['GET', 'POST'])
def mostrar_formulario_reserva():
    """Maneja el formulario de reserva"""
    form = ReservationForm()
    
    if form.validate_on_submit():
        try:
            # Crea la reserva
            reserva = Reserva(
                name=form.name.data,
                first_surname=form.first_surname.data,
                second_surname=form.second_surname.data,
                gender=form.gender.data,
                date_of_birth=form.date_of_birth.data,
                id_number=form.id_number.data,
                nationality=form.nationality.data,
                residence=form.residence.data,
                mobile_phone=form.mobile_phone.data,
                email=form.email.data,
                check_in=form.check_in.data,
                check_out=form.check_out.data,
                payment_type=form.payment_type.data,
                payment_holder=form.payment_holder.data,
                contract_reference=form.contract_reference.data
            )
            db.session.add(reserva)
            db.session.commit()
            
            flash('Reserva realizada con éxito!', 'success')
            return redirect(url_for('main.confirmacion_reserva'))
        
        except Exception as e:
            db.session.rollback()
            print(f"Error al procesar la reserva: {e}")  # Depuración
            flash(f'Error al procesar la reserva: {str(e)}', 'error')
    else:
        print("Formulario no válido")  # Depuración
        print(form.errors)  # Muestra los errores de validación

    return render_template('reservar.html', form=form)

# Ruta de confirmación
@main.route('/confirmacion')
def confirmacion_reserva():
    """Muestra la página de confirmación"""
    return render_template('confirmacion.html')

# Ruta para listar reservas
@main.route('/reservas')
def listar_reservas():
    """Muestra todas las reservas"""
    reservas = Reserva.query.all()
    return render_template('reservas.html', reservas=reservas)

# Ruta para eliminar una reserva
@main.route('/eliminar-reserva/<int:id>', methods=['POST'])
def eliminar_reserva(id):
    """Elimina una reserva específica"""
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva eliminada correctamente', 'success')
    return redirect(url_for('main.listar_reservas'))
