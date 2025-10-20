from datos.conexion import Session

sesion = Session()

def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("El objeto se ha insertado correctamente")
    except Exception as e:
        sesion.rollback()
        print(f"Error al insertar el objeto: {e}")
    finally:
        sesion.close()