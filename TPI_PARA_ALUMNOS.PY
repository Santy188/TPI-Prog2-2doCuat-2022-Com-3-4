import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("V1.2")
            print("Menu de opciones Concesionaria")
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
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
            if nro ==3:
                marca = input("Por favor ingrese la marca del auto: ")
                modelo = input("Por favor ingrese el modelo del auto: ")
                automovil_a_borrar=Automovil(marca,modelo)
                automovil_a_borrar.borrar_automovil()
            if nro ==4:
                marca = input("Por favor ingrese la marca del auto: ")
                modelo = input("Por favor ingrese el modelo del auto: ")
                aumentar_cantidad=Automovil(marca,modelo)
                aumentar_cantidad.cargar_disponibilidad()
            if nro == 5:
                mostrar_automoviles = Automovil.mostrar_listado()
                print("El listado de autos ordenados es:")
                for autos in mostrar_automoviles:
                    print(autos[1])
                print("\n")
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def mostrar_listado():
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            return autos
        except:
            print("Ha ocurrido un error al aumentar la cantidad disponible :(.")
    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles = cantidadDisponibles + 1 WHERE marca='{}' and modelo='{}'".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Cantidad disponible aumentada con exito!.")
        except:
            print("Ha ocurrido un error al aumentar la cantidad disponible :(.")


    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("El borrado ha sido exitoso.")
        except:
            print("Ha ocurrido un error al eliminar los datos requeridos.")


    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
        
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
#programa.crearTablas()
programa.menu()