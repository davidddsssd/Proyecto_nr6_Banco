from datos.conexion import Session
from auxiliares.estandarizar_strings import normalizar_string

from modelos.cliente import Cliente

def obtener_datos_objetos(objeto):
    session = Session()
    try:
        resultados = session.query(objeto).all()
        return resultados
    finally:
        session.close()

#ejemplo (cambiarlo luego)
def obtener_cliente_nombre(nombre):
    listado_clientes = obtener_datos_objetos(Cliente)
    cliente_encontrado = False
    if listado_clientes:
        for nombres in listado_clientes:
            if normalizar_string(nombres.nombre) == normalizar_string(nombres):
                cliente_encontrado = True
    return cliente_encontrado