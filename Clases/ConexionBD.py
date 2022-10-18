
import sqlite3


class Conexiones:

    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute(
            "CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")
        conexion.miConexion.commit()
        conexion.cerrarConexion()


    @classmethod
    def crearTablaMoto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute(
            "CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), cilindrada VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME default current_timestamp)")
        conexion.miConexion.commit()
        conexion.cerrarConexion()
