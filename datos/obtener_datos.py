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

def obtener_cliente_nombre(nombre_buscado: str) -> bool:
    listado_clientes = obtener_datos_objetos(Cliente)
    if not listado_clientes:
        return False

    nombre_normalizado = normalizar_string(nombre_buscado)
    for cliente in listado_clientes:
        if normalizar_string(cliente.nombre) == nombre_normalizado:
            return True
    return False