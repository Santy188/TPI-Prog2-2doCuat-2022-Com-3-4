
from Clases import ConexionBD
from Clases import Automoviles

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("V1.7.1")
            print("Menu de opciones Concesionaria")
            print("5- Mostrar listado")
            print("4- Cargar disponibilidad")
            print("3- Borrar automovil")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
            
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automoviles.Automovil(marca,modelo,precio,cantidadDisponibles)
                print(nuevo_automovil.cargar_automovil())
            elif nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar= Automoviles.Automovil(marca,modelo,precio)
                print(automovil_a_modificar.modificar_automoviles())
            elif nro ==3:
                marca = input("Por favor ingrese la marca del auto: ")
                modelo = input("Por favor ingrese el modelo del auto: ")
                automovil_a_borrar= Automoviles.Automovil(marca,modelo)
                print(automovil_a_borrar.borrar_automovil())
            elif nro ==4:
                marca = input("Por favor ingrese la marca del auto: ")
                modelo = input("Por favor ingrese el modelo del auto: ")
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
            elif nro==0:
                print("Saliendo del programa....")
                print("Come back soon!!!")
                break
            else:
                print("Usted ha seleccionado una opcion incorrecta.")
    

programa = ProgramaPrincipal()
#programa.ConexionBD.crearTablas()
programa.menu()