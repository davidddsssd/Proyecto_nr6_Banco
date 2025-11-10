from datos.conexion import Session

def modificar_objeto():
    """
    Guarda los cambios realizados a un objeto existente.

    Se asume que el objeto ya fue modificado antes de llamar a esta función.
    """
    session = Session()
    try:
        session.commit()
        print("Objeto modificado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al modificar objeto: {e}")
    finally:
        session.close()
#def modificar_objeto()