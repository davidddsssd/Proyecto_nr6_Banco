from datos.conexion import Session

def modificar_objeto():
    session = Session()
    try:
        session.commit()
        print("Objeto modificado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al modificar objeto: {e}")
    finally:
        session.close()