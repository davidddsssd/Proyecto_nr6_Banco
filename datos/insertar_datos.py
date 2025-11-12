from datos.conexion import Session

def insertar_objeto(objeto):
    """
    Inserta un objeto en la base de datos
    Necesita la instancia del modelo que se desea guardar
    """
    session = Session()
    try:
        session.add(objeto)
        session.commit()
        print("Objeto insertado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al insertar el objeto: {e}")
    finally:
        session.close()
#def insertar_objeto()