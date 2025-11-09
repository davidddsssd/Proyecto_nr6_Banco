from datos.conexion import Session

def eliminar_objeto(objeto):
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