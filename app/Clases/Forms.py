from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, Length, NumberRange
from datetime import datetime

class ValidacionesAutos(FlaskForm):
    marca = StringField("Marca", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    modelo = StringField("Modelo", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    precio = IntegerField("Precio", validators=[
        DataRequired(message="Debe ingresar algo en este campo")
    ])

    cantidad = IntegerField("Cantidad", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        NumberRange(min=0, max=500, message="Solo se puede ingresar numeros desde el 0 al 500")
    ])

    submit = SubmitField("Enviar")


class ValidacionesMotos(FlaskForm):
    marca = StringField("Marca", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    modelo = StringField("Modelo", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    precio = IntegerField("Precio", validators=[
        DataRequired(message="Debe ingresar algo en este campo")
    ])

    cilindrada = StringField("Cilindrada", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    color = StringField("Color", validators=[
        DataRequired(message="Debe ingresar algo en este campo"),
        Length(max = 10, min= 2, message="El texto debe estar entre 2 y 10 caracteres")
    ])

    submit = SubmitField("Enviar")

class ValidarDateTime(FlaskForm):
    fecha = DateField("Fecha", format='%Y-%m-%d', validators=[
        DataRequired(message="Debe ingresar una fecha en este campo")
    ])

    submit = SubmitField("Enviar")