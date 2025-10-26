from datos.conexion import Session

def insertar_objeto(objeto):
    session = Session()
    session.add(objeto)
    try:
        session.commit()
        print("El objeto se ha insertado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al insertar el objeto: {e}")
    finally:
        session.close()