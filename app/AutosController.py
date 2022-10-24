from Clases import Automoviles
from Clases import Motocicletas
from Clases import Forms
from flask import Flask, Blueprint, render_template, request, redirect

#Definiendo blueprint
AutosController = Blueprint("AutosController", __name__, static_folder="static", template_folder="templates")



#CONTROLADOR AUTOMOVILES
@AutosController.route('/automoviles/', methods=['GET', 'POST'])
def automoviles():
    return redirect('agregar')


#AGREGAR AUTOMOVILES
@AutosController.route('/automoviles/agregar/', methods=['GET', 'POST'])
def agregarAutomovil():
    form = Forms.ValidacionesAutos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        nuevo_automovil = Automoviles.Automovil(marca,modelo,precio,cantidad)
        nuevo_automovil = nuevo_automovil.cargar_automovil()
        return render_template('automoviles/estado.html', resultado = nuevo_automovil)
    return render_template('automoviles/agregar.html', form = form)


#MODIFICAR AUTOMOVILES
@AutosController.route('/automoviles/modificar/', methods=['GET', 'POST'])
def modificarAutomovil():
    form = Forms.ValidacionesAutos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']

        automovil_a_modificar= Automoviles.Automovil(marca,modelo,precio)
        automovil_a_modificar = automovil_a_modificar.modificar_automoviles()
        return render_template('automoviles/estado.html', resultado = automovil_a_modificar)
    return render_template('automoviles/modificar.html', form = form)


#ELIMINAR AUTOMOVILES
@AutosController.route('/automoviles/eliminar/', methods=['GET', 'POST'])
def eliminarAutomovil():
    form = Forms.ValidacionesAutos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']

        automovil_a_borrar= Automoviles.Automovil(marca,modelo)
        automovil_a_borrar = automovil_a_borrar.borrar_automovil()
        return render_template('automoviles/estado.html', resultado = automovil_a_borrar)
    return render_template('automoviles/eliminar.html', form = form)


#MOSTRAR AUTOMOVILES
@AutosController.route('/automoviles/mostrar_listado/', methods=['GET', 'POST'])
def mostrarAutomoviles():
    mostrar_automoviles = Automoviles.Automovil.mostrar_listado()
    return render_template('automoviles/mostrar_listado.html', mostrar_automoviles = mostrar_automoviles)


#AUMENTAR DISPONIBILIDAD
@AutosController.route('/automoviles/cargar_disponibilidad/', methods=['GET', 'POST'])
def disponibilidadAutomovil():
    form = Forms.ValidacionesAutos()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']

        aumentar_cantidad= Automoviles.Automovil(marca,modelo)
        aumentar_cantidad = aumentar_cantidad.cargar_disponibilidad()
        return render_template('automoviles/estado.html', resultado = aumentar_cantidad)
    return render_template('automoviles/cargar_disponibilidad.html', form = form)


#CREAR TABLA MOTOCICLETAS
@AutosController.route('/automoviles/crear_tabla_automoviles/', methods=['GET', 'POST'])
def crear_tabla_auto():
    form = Forms.ValidacionesAutos()
    if request.method == 'POST':
        crear_tabla = Automoviles.Automovil.crearTablaAutomoviles()
        return render_template('automoviles/estado.html', resultado = crear_tabla)
    return render_template('automoviles/crear_tabla_automoviles.html', form = form)