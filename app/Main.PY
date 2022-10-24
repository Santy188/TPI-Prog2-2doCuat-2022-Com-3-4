from AutosController import AutosController
from MotosController import MotosController
from Clases import Automoviles
from Clases import Motocicletas
from Clases import Forms
from flask import Flask, render_template, request, redirect

print("GESTOR CONCESIONARIA V2.3")

#Definiendo la aplicacion
app = Flask(__name__, template_folder='templates' ,static_folder='static')


#Utilizando Blueprint para conectar los controladores
app.register_blueprint(AutosController, url_prefix="")
app.register_blueprint(MotosController, url_prefix="")

#Contraseña para conectar los formularios
app.secret_key = "lgjt4evVARBM"



#Pagina principal
@app.route('/')
def index():
    return render_template('index.html')



#INICIANDO LA APLICACION
#CUANDO EL MODO DEBUG ESTA ACTIVADO LOS CAMBIOS SE HACEN EN TIEMPO REAL.
if __name__=="__main__":
    app.run(debug=False)

