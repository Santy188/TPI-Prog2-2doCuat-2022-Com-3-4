class ProgramaPrincipal:

    def menu(self):
        while True:
            print("V1.8")
            print("==============CONCESIONARIA===============")
            print("\t[6] Cargar Motocicleta")
            print("\t[5] Mostrar listado")
            print("\t[4] Cargar disponibilidad")
            print("\t[3] Borrar automovil")
            print("\t[2] Modificar Automovil")
            print("\t[1] Cargar Automovil")
            print("\t[0] Salir de menu")
            nro = int(input("\tPor favor ingrese un número "))
            
            if nro == 1:
                marca = input("\tPor favor ingrese la marca del automovil: ")
                modelo = input("\tPor favor ingrese el modelo del automovil: ")
                precio = input("\tPor favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("\tPor favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automoviles.Automovil(marca,modelo,precio,cantidadDisponibles)
                print(nuevo_automovil.cargar_automovil())
            elif nro ==2:
                marca = input("\tPor favor ingrese el nombre de la marca: ")
                modelo = input("\tPor favor ingrese el nombre del modelo: ")
                precio = input("\tPor favor ingrese el nuevo precio: ")
                automovil_a_modificar= Automoviles.Automovil(marca,modelo,precio)
                print(automovil_a_modificar.modificar_automoviles())
            elif nro ==3:
                marca = input("\tPor favor ingrese la marca del auto: ")
                modelo = input("\tPor favor ingrese el modelo del auto: ")
                automovil_a_borrar= Automoviles.Automovil(marca,modelo)
                print(automovil_a_borrar.borrar_automovil())
            elif nro ==4:
                marca = input("\tPor favor ingrese la marca del auto: ")
                modelo = input("\tPor favor ingrese el modelo del auto: ")
                aumentar_cantidad= Automoviles.Automovil(marca,modelo)
                print(aumentar_cantidad.cargar_disponibilidad())
            elif nro == 5:
                mostrar_automoviles = Automoviles.Automovil.mostrar_listado()
                #Verifica si el objeto retornado es una lista, caso contrario es porque ha ocurrido un error
                if isinstance(mostrar_automoviles, list) == True:
                    for autos in mostrar_automoviles:
                        print("Auto: {} Modelo: {} Precio: {}".format(autos[1], autos[2], autos[3]))
                    print("\n")
                else:
                    print(mostrar_automoviles)
            elif nro == 6:
                marca = input("\tPor favor ingrese la marca de la motocicleta: ")
                modelo = input("\tPor favor ingrese el modelo de la motocicleta: ")
                cilindrada = input("\tPor favor ingrese la cilindrada: ")
                precio = input("\tPor favor ingrese el precio de la motocicleta: ")        
                color = input("\tPor favor ingrese el color de la motocicleta: ")
             
                nueva_motocicleta = Motocicletas.Motocicleta(marca, modelo, cilindrada, precio, color)
                print(nueva_motocicleta.cargar_motocicleta())
            elif nro == 7:
                print(Motocicletas.Motocicleta.actualizar_precio())
            elif nro==0:
                print("Saliendo del programa....")
                print("Come back soon!!!")
                break
            else:
                print("Usted ha seleccionado una opcion incorrecta.")
    

programa = ProgramaPrincipal()
#programa.ConexionBD.crearTablas()
#ConexionBD.Conexiones.crearTablaMoto()
#ConexionBD.Conexiones().copiar_tabla()
programa.menu()

from flask import Flask, render_template, request

#Definiendo la aplicacion
app = Flask(__name__)



#Controladores
@app.route('/')
def index():
    return render_template('automoviles.html')

@app.route('/motocicletas/')
def motocicletas():
    return render_template('motocicletas.html')

#Agregar automovil
@app.route('/addautomoviles/', methods = ['GET', 'POST'])
def agregarautomovil():
    precio = request.form['precio']
    boton = request.form['submit']
    return render_template('automoviles.html', precio = precio, boton = boton)
 
#Desplegando la aplicacion
if __name__=="__main__":
    app.run()






    #Controladores
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/automoviles/', methods=['GET', 'POST'])
def automoviles():
    form = Validaciones()
    return render_template('automoviles.html', form = form)

@app.route('/motocicletas/', methods=['GET'])
def motocicletas():
    return render_template('motocicletas.html')




#Controladores Automoviles
@app.route('/automoviles/agregar/', methods=['GET', 'POST'])
def agregarautomovil():
    form = Validaciones()
    if form.validate_on_submit():
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        nuevo_automovil = Automoviles.Automovil(marca,modelo,precio,cantidad)
        resultado = nuevo_automovil.cargar_automovil()
        
        return render_template('automoviles/agregar.html', resultado = resultado)

    return render_template('automoviles/agregar.html')




#Desplegando la aplicacion
if __name__=="__main__":
    app.run(debug=True)