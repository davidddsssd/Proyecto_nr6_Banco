from datos.insertar_datos import insertar_objeto
from modelos.cliente import Cliente
from modelos.direccion import Direccion
from auxiliares import normalizar_cadena
from auxiliares.validaciones import (validar_telefono, validar_correo, formatear_nombre, validar_rut_chileno)
from datos.conexion import Session


def crear_cliente(nombre, apellido, rut, telefono, mail=None, id_direccion=None):
    # Validar campos obligatorios
    if not nombre or not apellido or not rut or not telefono:
        print("Faltan datos obligatorios (nombre, apellido, RUT o teléfono).")
        return

    # Limpieza básica
    nombre = formatear_nombre(nombre.strip())
    apellido = formatear_nombre(apellido.strip())
    rut = rut.strip()
    telefono = telefono.strip()
    if mail:
        mail = mail.strip()

    # Validar RUT chileno
    if not validar_rut_chileno(rut):
        print("El RUT ingresado no es válido. Ejemplo: 12.345.678-9")
        return

    # Validar teléfono chileno
    if not validar_telefono(telefono):
        print("El teléfono ingresado no es válido. Ejemplo: +56912345678 o 912345678")
        return

    # Validar correo
    if mail and not validar_correo(mail):
        print("El correo ingresado no es válido. Ejemplo: ejemplo@dominio.com")
        return

    sesion = Session()
    try:
        # Verificar duplicados
        clientes = sesion.query(Cliente).all()
        for c in clientes:
            if normalizar_cadena(c.rut) == normalizar_cadena(rut):
                print("Ya existe un cliente con ese RUT.")
                return
            if normalizar_cadena(c.telefono) == normalizar_cadena(telefono):
                print("Ya existe un cliente con ese teléfono.")
                return

        # Validar dirección
        if id_direccion is None:
            print("\nDebe indicar una dirección existente (ID entre 1 y 20).")
            direcciones = sesion.query(Direccion).all()
            for d in direcciones:
                print(f"[{d.id_direccion}] {d.calle}, {d.comuna}")
            try:
                id_direccion = int(input("\nIngrese el ID de la dirección: "))
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
                return

        direccion = sesion.query(Direccion).filter_by(id_direccion=id_direccion).first()
        if not direccion:
            print("El ID de dirección no existe en la base de datos.")
            return

        nuevo = Cliente(
            id_direccion=id_direccion,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            telefono=telefono,
            mail=mail
        )

        insertar_objeto(nuevo)
        print("Cliente registrado correctamente con datos válidos.")

    except Exception as e:
        print("Error al registrar cliente:", e)

    finally:
        sesion.close()
#def crear_cliente()

def desactivar_cliente(id_cliente):
    """
    Marca un cliente como inactivo (borrado lógico).
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID.")
            return

        if not cliente.estado_cliente:
            print("El cliente ya se encuentra desactivado.")
            return

        cliente.estado_cliente = False
        sesion.commit()
        print(f"Cliente {cliente.nombre} {cliente.apellido} (ID {cliente.id_cliente}) desactivado correctamente.")
    except Exception as e:
        sesion.rollback()
        print("Error al desactivar cliente:", e)
    finally:
        sesion.close()


def reactivar_cliente(id_cliente):
    """
    Vuelve a activar un cliente previamente desactivado.
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID.")
            return

        if cliente.estado_cliente:
            print("El cliente ya está activo.")
            return

        cliente.estado_cliente = True
        sesion.commit()
        print(f"Cliente {cliente.nombre} {cliente.apellido} (ID {cliente.id_cliente}) reactivado correctamente.")
    except Exception as e:
        sesion.rollback()
        print("Error al reactivar cliente:", e)
    finally:
        sesion.close()