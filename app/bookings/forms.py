from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):
    people = IntegerField('Numero de personas', validators=[DataRequired(), ])
    submit = SubmitField('Hacer Reserva')