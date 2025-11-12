from datos.conexion import Session

def modificar_objeto(objeto):
    """
    Modifica un objeto existente en la base de datos.

    Parámetros:
        objeto: instancia de un modelo SQLAlchemy que ya exista en la base de datos.

    Ejemplo de uso:
        cliente.nombre = "Nuevo Nombre"
        modificar_objeto(cliente)
    """
    session = Session()
    try:
        session.merge(objeto)   # Sincroniza el objeto con la base de datos
        session.commit()
        print("Objeto modificado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al modificar objeto: {e}")
    finally:
        session.close()
#def modificar_objeto()