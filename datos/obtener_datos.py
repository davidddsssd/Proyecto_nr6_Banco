from datos.conexion import Session

def obtener_datos_objetos(objeto):
    """
    Obtiene todos los registros de una tabla específica
    Necesita la clase del modelo (Ej. Cliente, Cuenta, etc.)
    Retorna una lista de objetos encontrados en la tabla
    """
    session = Session()
    try:
        resultados = session.query(objeto).all()
        return resultados
    finally:
        session.close()
#def obtener_datos_objetos()