from flask_restful import Resource

from flask import make_response, render_template


# Recursos -> Los recursos que mi servidor tendrá disponible

 # Vamos a crear Recursos - Para nosotros poder crear recursos
# lo haremos a través de clases y objetos
class HolaMundo(Resource):
# Los recursos van a poder ejecutar dos acciones -> métodos
    def get(self):
        return {'Hola': 'Mundo'}

# Será un recurso
class PantallaInicio(Resource):
    def get(self):
        # Renderizamos el contenido del archivo html
        contenido = render_template('index.html')
        # retornamos el contenido renderizado en una respuesta
        return make_response(contenido)

class Despedida(Resource):
    def get(self):
        return 'Adios'