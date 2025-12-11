# Las rutas de acceso a cada recurso
from recursos import *

# Tener el objeto api
def crear_rutas(api):
    # Quiero que puedas acceder a este recurso por medio de tal ruta
    # 1. El recurso que va a ejecutar - Invocar
    # 2. La dirección de este recurso
    api.add_resource(HolaMundo, '/hola')
    # La ruta de inicio
    api.add_resource(PantallaInicio, '/')

    api.add_resource(Despedida, '/adios')


# Diccionarios - JSON
