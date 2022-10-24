from Clases import Automoviles
from Clases import Motocicletas
from Clases import Forms
from flask import Flask, Blueprint, render_template, request, redirect

MotosController = Blueprint("MotosController", __name__, static_folder="static", template_folder="templates")

#CONTROLADORES DE MOTOCICLETAS
@MotosController.route('/motocicletas/', methods=['GET', 'POST'])
def motocicletas():
    return redirect('agregar')


#AGREGAR MOTOCICLETA
@MotosController.route('/motocicletas/agregar/', methods=['GET', 'POST'])
def agregarMotocicleta():
    form = Forms.ValidacionesMotos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
        cilindrada = request.form['cilindrada']
        precio = request.form['precio']   
        color = request.form['color']
             
        nueva_motocicleta = Motocicletas.Motocicleta(marca, modelo, cilindrada, precio, color)
        nueva_motocicleta = nueva_motocicleta.cargar_motocicleta()
        return render_template('motocicletas/estado.html', resultado = nueva_motocicleta)
    return render_template('motocicletas/agregar.html', form = form)


#MODIFICAR MOTOCICLETA
@MotosController.route('/motocicletas/modificar/', methods=['GET', 'POST'])
def modificarMotocicleta():
    form = Forms.ValidacionesMotos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']   
             
        modificar_motocicleta = Motocicletas.Motocicleta(marca, modelo, None, precio)
        modificar_motocicleta = modificar_motocicleta.modificar_motocicleta()
        return render_template('motocicletas/estado.html', resultado = modificar_motocicleta)
    return render_template('motocicletas/modificar.html', form = form)


#ELIMINAR MOTOCICLETA
@MotosController.route('/motocicletas/eliminar/', methods=['GET', 'POST'])
def borrarMotocicleta():
    form = Forms.ValidacionesMotos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
             
        eliminar_motocicleta = Motocicletas.Motocicleta(marca, modelo)
        eliminar_motocicleta = eliminar_motocicleta.borrar_motocicleta()
        return render_template('motocicletas/estado.html', resultado = eliminar_motocicleta)
    return render_template('motocicletas/eliminar.html', form = form)


#MOSTRAR LISTADO DE MOTOCICLETAS
@MotosController.route('/motocicletas/mostrar_listado/', methods=['GET', 'POST'])
def mostrarMotocicletas():
    mostrar_motocicletas = Motocicletas.Motocicleta.mostrar_listado()
    return render_template('motocicletas/mostrar_listado.html', mostrar_listado = mostrar_motocicletas)


#CREAR TABLA MOTOCICLETAS
@MotosController.route('/motocicletas/crear_tabla_motocicleta/', methods=['GET', 'POST'])
def crear_tabla_moto():
    form = Forms.ValidacionesMotos()
    if request.method == 'POST':
        crear_tabla = Motocicletas.Motocicleta.crearTablaMoto()
        return render_template('motocicletas/estado.html', resultado = crear_tabla)
    return render_template('motocicletas/crear_tabla_motocicleta.html', form = form)


#ACTUALIZAR PRECIO, FECHA Y CREAR TABLA HISTORICO MOTOCICLETAS
@MotosController.route('/motocicletas/aumentar_precios/', methods=['GET', 'POST'])
def actualizar_precios():
    form = Forms.ValidacionesMotos()
    if request.method == 'POST':
        actualizar_precios = Motocicletas.Motocicleta.aumentar_precios()
        return render_template('motocicletas/estado.html', resultado = actualizar_precios)
    return render_template('motocicletas/aumentar_precios.html', form = form)


#MOSTRAR REGISTROS ANTERIORES A UNA FECHA
@MotosController.route('/motocicletas/mostrar_registros/', methods=['GET', 'POST'])
def mostrar_registros():
    form = Forms.ValidarDateTime()
    if form.validate_on_submit():
        fecha = request.form['fecha']
        mostrar_registros = Motocicletas.Motocicleta.mostrar_registros_anteriores(fecha)
        return render_template('motocicletas/mostrar_listado.html', mostrar_listado = mostrar_registros)
    return render_template('motocicletas/mostrar_registros.html', form = form)
