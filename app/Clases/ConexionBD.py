import sqlite3


class Conexiones:

    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()

    def crearTablaAutomoviles(self):
        conexion = Conexiones()
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



    