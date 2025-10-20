from datos.conexion import Session

def obtener_datos_objetos(objeto):
    session = Session()
    try:
        resultados = session.query(objeto).all()
        return resultados
    finally:
        session.close()