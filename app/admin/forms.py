from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, TextAreaField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


class TourForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=128)])
    description = TextAreaField('Description')
    date = DateField('Date')
    price = IntegerField('Price')
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')