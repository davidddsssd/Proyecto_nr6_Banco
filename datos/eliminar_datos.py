from datos.conexion import Session

def eliminar_objeto(objeto):
    """
    Elimina un objeto existente en la base de datos.

    Parámetros:
        objeto: instancia del modelo SQLAlchemy que se desea eliminar.
    """
    session = Session()
    try:
        session.delete(objeto)
        session.commit()
        print("Objeto eliminado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar objeto: {e}")
    finally:
        session.close()
#def eliminar_objeto()