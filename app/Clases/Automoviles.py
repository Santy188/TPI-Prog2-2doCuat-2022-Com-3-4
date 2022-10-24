from Clases import ConexionBD

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def mostrar_listado():
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            return autos
        except:
            return "Ha ocurrido un error al aumentar la cantidad disponible :(."
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles = cantidadDisponibles + 1 WHERE marca='{}' and modelo='{}'".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            return "Cantidad disponible aumentada con exito!."
        except:
            return "Ha ocurrido un error al aumentar la cantidad disponible :(."
        finally:
            conexion.cerrarConexion()


    def borrar_automovil(self):
        conexion = ConexionBD.Conexiones()

        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            return "El borrado ha sido exitoso."
        except:
            return "Ha ocurrido un error al eliminar los datos requeridos."
        finally:
            conexion.cerrarConexion()


    def cargar_automovil(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            return "Automovil cargado exitosamente"
        except:
            return "Error al cargar el automovil"
        finally:
            conexion.cerrarConexion()

    
    
    def modificar_automoviles(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            return "Automovil modificado correctamente"
        except:
            return "Error al actualizar un automovil"
        finally:
            conexion.cerrarConexion()  

    @classmethod
    def crearTablaAutomoviles(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
            conexion.miCursor.execute(
                "CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")
            conexion.miConexion.commit()
            return "La operacion ha sido exitosa"
        except:
            return "Operacion fallida, error desconocido"
        finally:
            conexion.cerrarConexion()