from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange

class Validaciones(FlaskForm):
    marca = StringField("Marca", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 3, message="El texto debe estar entre 3 y 10 caracteres")
    ])

    modelo = StringField("Modelo", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 3, message="El texto debe estar entre 3 y 10 caracteres")
    ])

    precio = IntegerField("Precio", validators=[
        DataRequired(message="Debe ingresar algo en este campo")
    ])

    cantidad = IntegerField("Cantidad", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        NumberRange(min=0, max=500, message="Solo se puede ingresar numeros desde el 0 al 500")
    ])

    submit = SubmitField("Enviar")