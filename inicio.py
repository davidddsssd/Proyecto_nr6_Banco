from datos.obtener_datos import obtener_datos_objetos
from modelos.direccion import Direccion

def listado_direccion():
    listado_direccion = obtener_datos_objetos(Direccion)
    if listado_direccion:
        for direccion in listado_direccion:
            print(f'{direccion.id_direccion} {direccion.comuna} {direccion.calle} {direccion.departamente} {direccion.numero_d}')