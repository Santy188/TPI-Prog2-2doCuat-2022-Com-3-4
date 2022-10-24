from Clases import ConexionBD

class Motocicleta:
    def __init__(self, marca, modelo, cilindrada = 0, precio = 0, color="white"):
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

    def modificar_motocicleta(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            return "Motocicleta modificada correctamente"
        except:
            return "Error al modificar la motocicleta"
        finally:
            conexion.cerrarConexion()  

    def borrar_motocicleta(self):
        conexion = ConexionBD.Conexiones()

        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM MOTOCICLETAS where marca='{}' and modelo='{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            return "El borrado ha sido exitoso."
        except:
            return "Ha ocurrido un error al eliminar los datos requeridos."
        finally:
            conexion.cerrarConexion()

    def mostrar_listado():
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motos = conexion.miCursor.fetchall()
            return motos
        except:
            return "Ha al mostrar el listado :(."
        finally:
            conexion.cerrarConexion()
    

    @classmethod
    def crearTablaMoto(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
            conexion.miCursor.execute(#current_timestamp
                "CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), cilindrada VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME default current_date)")
            conexion.miConexion.commit()
            return "La operacion ha sido exitosa"
        except:
            return "Operacion fallida, error desconocido"
        finally:
            conexion.cerrarConexion()

    @classmethod
    def aumentar_precios(self):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            #Crear tabla historico motocicletas, copiar los datos y actualizar
            conexion.miCursor.execute("DROP TABLE IF EXISTS historico_motocicletas")
            conexion.miCursor.execute("CREATE TABLE historico_motocicletas (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30), cilindrada VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME)")
            conexion.miCursor.execute("INSERT INTO historico_motocicletas (id_moto, marca, modelo, cilindrada, precio, color, fechaUltimoPrecio) SELECT id_moto, marca, modelo, cilindrada, precio, color, fechaUltimoPrecio FROM MOTOCICLETAS")
            #Actualizar fecha de la tabla motocicletas
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio = precio + precio * 10/100 WHERE precio")
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET fechaUltimoPrecio = current_date WHERE fechaUltimoPrecio")
            conexion.miConexion.commit()
            return "La operacion ha sido exitosa"
        except:
            return "La operacion ha fallado, error desconocido"
        finally:
            conexion.cerrarConexion()
    
    @classmethod
    def mostrar_registros_anteriores(self, fecha):
        conexion = ConexionBD.Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS WHERE fechaUltimoPrecio<'{}'".format(fecha))
            registros = conexion.miCursor.fetchall()
            return registros
        except:
            return "La operacion ha fallado, error desconocido"
        finally:
            conexion.cerrarConexion()