from datos.conexion import Session

def insertar_objeto(objeto):
    session = Session()
    try:
        session.add(objeto)
        session.commit()
        print("Objeto insertado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al insertar objeto: {e}")
    finally:
        session.close()
#def insertar_objeto()