from copy import copy
from Clases import ConexionBD

class Motocicleta:
    def __init__(self, marca, modelo, cilindrada, precio, color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.precio = precio
        self.color = color
       
    def cargar_motocicleta(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()

        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(marca, modelo, cilindrada, precio, color) VALUES('{}','{}','{}','{}','{}')".format(self.marca, self.modelo, self.cilindrada, self.precio, self.color))
            conexion.miConexion.commit()
            return "Motocicleta cargada exitosamente"
        except:
            return "Error al agregar una motocicleta"
        finally:
            conexion.cerrarConexion()

    def borrar_motocicleta(self):
        conexion = ConexionBD.Conexiones()

        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM MOTOCICLETA where marca='{}' and modelo='{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            return "El borrado ha sido exitoso."
        except:
            return "Ha ocurrido un error al eliminar los datos requeridos."
        finally:
            conexion.cerrarConexion()
    
    @classmethod
    def actualizar_precio_fecha(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()

        try:
            #conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio = precio + precio * 10/100 WHERE precio")
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET fechaUltimoPrecio = current_timestamp WHERE fechaUltimoPrecio")
            conexion.miConexion.commit()
            return "El actualizado ha sido exitoso."
        except:
            return "Ha ocurrido un error al actualizar los precios"
        finally:
            conexion.cerrarConexion()

    def crearTablaMoto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
            conexion.miCursor.execute(
                "CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), cilindrada VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME default current_timestamp)")
            conexion.miConexion.commit()
            return "La operacion ha sido exitosa"
        except:
            return "Operacion fallida, error desconocido"
        finally:
            conexion.cerrarConexion()


    def copiar_tabla(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DROP TABLE IF EXISTS historico_motocicletas")
            conexion.miCursor.execute("CREATE TABLE historico_motocicletas (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), cilindrada VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME)")
            conexion.miCursor.execute("INSERT INTO historico_motocicletas (id_moto, marca, modelo, cilindrada, precio, color, fechaUltimoPrecio) SELECT id_moto, marca, modelo, cilindrada, precio, color, fechaUltimoPrecio FROM MOTOCICLETAS")
            conexion.miConexion.commit()
            return "La operacion ha sido exitosa"
        except:
            return "Operacion fallida, error desconocido"
        finally:
            conexion.cerrarConexion()
            