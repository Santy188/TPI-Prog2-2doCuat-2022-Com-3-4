
from Clases import ConexionBD
from Clases import Automoviles
from Clases import Motocicletas

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
            elif nro==0:
                print("Saliendo del programa....")
                print("Come back soon!!!")
                break
            else:
                print("Usted ha seleccionado una opcion incorrecta.")
    

programa = ProgramaPrincipal()
#programa.ConexionBD.crearTablas()
ConexionBD.Conexiones.crearTablaMoto()
programa.menu()