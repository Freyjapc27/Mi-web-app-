# Desde la libreria importa Flask
from flask import Flask

# Desde flask_rewstful importamos la clase API y la clase Resource
from flask_restful import Api, Resource

from rutas import crear_rutas

#API (aplication programing interfaces)
# Vamos a crear un objeto de tipo Flask (app)

app = Flask(__name__)  # Under method (servidor)
# Creamos un objeto de tipo API y como argumento y
# le pasamos el objeto app

# El parametro/argumento que espera recibir es el obejto de Flask
api = Api(app)  # (programa)
# la APIi será el programa que se comunique con el dsipositivo físico

crear_rutas(api)


# Del objeto app ejecutamos el método run
app.run(port=8080, debug=True)

# 127.0.0.1:8080 -> LoopBack (IP Local o de retro alimentacion)
# Recusrso = Inforamación


