from modelos.cliente import Cliente
from modelos.direccion import Direccion
from auxiliares import normalizar_cadena
from auxiliares.validaciones import (
    validar_telefono,
    validar_correo,
    formatear_nombre,
    validar_rut_chileno
)
from datos.conexion import Session


def crear_cliente(nombre, apellido, rut, telefono, mail=None,
                  comuna=None, calle=None, departamento=None, numero_d=None):
    """
    Crea un nuevo cliente junto con su dirección asociada,
    usando una única sesión para evitar conflictos entre objetos.
    """

    if not nombre or not apellido or not rut or not telefono or not comuna or not calle or not numero_d:
        print("Faltan datos obligatorios (nombre, apellido, rut, teléfono o dirección).")
        return

    # Normalización de texto
    nombre = formatear_nombre(nombre.strip())
    apellido = formatear_nombre(apellido.strip())
    rut = rut.strip()
    telefono = telefono.strip()
    if mail:
        mail = mail.strip()

    # Validaciones
    if not validar_rut_chileno(rut):
        print("El RUT ingresado no es válido. Ejemplo: 12345678-9")
        return

    if not validar_telefono(telefono):
        print("El teléfono ingresado no es válido. Ejemplo: 912345678")
        return

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
                sesion.close()
                return
            if normalizar_cadena(c.telefono) == normalizar_cadena(telefono):
                print("Ya existe un cliente con ese teléfono.")
                sesion.close()
                return

        # Crear dirección y cliente dentro de la misma sesión
        nueva_direccion = Direccion(
            comuna=comuna.strip(),
            calle=calle.strip(),
            departamento=departamento,
            numero_d=str(numero_d).strip()
        )
        sesion.add(nueva_direccion)
        sesion.flush()  # genera el id_direccion sin cerrar la sesión

        nuevo_cliente = Cliente(
            id_direccion=nueva_direccion.id_direccion,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            telefono=telefono,
            mail=mail
        )
        sesion.add(nuevo_cliente)
        sesion.commit()

        print(f"\nCliente '{nombre} {apellido}' registrado correctamente.")
        print(f"Dirección guardada: {calle} #{numero_d}, {comuna}")

    except Exception as e:
        sesion.rollback()
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
#def desactivar_cliente()


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
#def reactivar_cliente()