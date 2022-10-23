from AutosController import AutosController
from Clases import Automoviles
from Clases import Motocicletas
from Clases import Forms
from flask import Flask, render_template, request, redirect

print("GESTOR CONCESIONARIA V1.9")

#Definiendo la aplicacion
app = Flask(__name__, template_folder='templates' ,static_folder='static')

#Utilizando Blueprint para conectar los controladores
app.register_blueprint(AutosController, url_prefix="")

#Contraseña para conectar los formularios
app.secret_key = "lgjt4evVARBM"



#Pagina principal
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/motocicletas/', methods=['GET'])
def motocicletas():
    return render_template('motocicletas.html')


#Desplegando la aplicacion
if __name__=="__main__":
    app.run(debug=True)

