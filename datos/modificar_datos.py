from datos.conexion import Session

def modificar_objeto(objeto):
    """
    Modifica un objeto existente en la base de datos
    Necesita la instacia un modelo que ya exista en la BD
    """
    session = Session()
    try:
        session.merge(objeto)
        session.commit()
        print("Objeto modificado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al modificar al objeto: {e}")
    finally:
        session.close()
#def modificar_objeto()