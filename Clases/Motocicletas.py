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
    def actualizar_precio(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()

        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio = precio + precio * 10/100 WHERE precio")
            conexion.miConexion.commit()
            return "El actualizado ha sido exitoso."
        except:
            return "Ha ocurrido un error al actualizar los precios"
        finally:
            conexion.cerrarConexion()

            