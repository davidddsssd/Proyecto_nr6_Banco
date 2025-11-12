from datos.insertar_datos import insertar_objeto
from modelos.cuenta import Cuenta
from modelos.cliente import Cliente
from datos.conexion import Session
import re
from datetime import datetime


def crear_cuenta(id_cliente, numero_c, saldo_inicial, tipo_cuenta, estado=True):
    """
    Crea una cuenta bancaria asociada a un cliente existente.

    Validaciones:
    - Cliente debe existir y estar activo
    - Número de cuenta con formato 001-0001-000001
    - Saldo inicial numérico, no negativo y ≤ $5.000.000
    - Tipo de cuenta válido: corriente, ahorro o vista
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID. Regístrelo primero.")
            return
        if not cliente.estado_cliente:
            print("El cliente está desactivado. No se puede crear una cuenta para un cliente deshabilitado.")
            return

        if not re.match(r'^\d{3}-\d{4}-\d{6}$', numero_c):
            print("Formato inválido. Ejemplo: 001-0001-000001")
            return

        if sesion.query(Cuenta).filter_by(numero_c=numero_c).first():
            print("Ya existe una cuenta con ese número.")
            return

        try:
            saldo_inicial = int(saldo_inicial)
        except ValueError:
            print("El saldo inicial debe ser un número entero válido.")
            return

        if saldo_inicial < 0:
            print("El saldo no puede ser negativo.")
            return
        if saldo_inicial > 5000000:
            print("El saldo inicial no puede superar los $5.000.000.")
            return

        tipo_cuenta = tipo_cuenta.lower()
        if tipo_cuenta not in ['corriente', 'ahorro', 'vista']:
            print("Tipo de cuenta inválido. Debe ser: corriente, ahorro o vista.")
            return

        nueva = Cuenta(
            id_cliente=id_cliente,
            numero_c=numero_c,
            saldo=saldo_inicial,
            fecha_apertura=datetime.now(),
            tipo_cuenta=tipo_cuenta,
            estado_cuenta=estado
        )

        insertar_objeto(nueva)
        print(f"Cuenta creada correctamente para {cliente.nombre} {cliente.apellido}.")
        print(f"Número: {numero_c} | Tipo: {tipo_cuenta.capitalize()} | Saldo: ${saldo_inicial:,}")

    except Exception as e:
        print("Error al crear cuenta:", e)
    finally:
        sesion.close()
#def crear_cuenta()


def desactivar_cuenta(id_cuenta):
    """
    Desactiva (cierra lógicamente) una cuenta bancaria existente.
    No elimina los registros, solo cambia el estado_cuenta a False.
    """
    sesion = Session()
    try:
        cuenta = sesion.query(Cuenta).filter_by(id_cuenta=id_cuenta).first()
        if not cuenta:
            print("No se encontró una cuenta con ese ID.")
            return

        if not cuenta.estado_cuenta:
            print("La cuenta ya está desactivada o cerrada.")
            return

        cuenta.estado_cuenta = False
        sesion.commit()

        print(f"Cuenta {cuenta.numero_c} (ID {cuenta.id_cuenta}) desactivada correctamente.")

    except Exception as e:
        sesion.rollback()
        print("Error al desactivar cuenta:", e)
    finally:
        sesion.close()
#def desactivar_cuenta()


def reactivar_cuenta(id_cuenta):
    """
    Reactiva una cuenta bancaria previamente desactivada.
    Cambia el campo estado_cuenta a True.
    """
    sesion = Session()
    try:
        cuenta = sesion.query(Cuenta).filter_by(id_cuenta=id_cuenta).first()
        if not cuenta:
            print("No se encontró una cuenta con ese ID.")
            return

        if cuenta.estado_cuenta:
            print("La cuenta ya está activa.")
            return

        cuenta.estado_cuenta = True
        sesion.commit()

        print(f"Cuenta {cuenta.numero_c} (ID {cuenta.id_cuenta}) reactivada correctamente.")

    except Exception as e:
        sesion.rollback()
        print("Error al reactivar cuenta:", e)
    finally:
        sesion.close()
#def reactivar_cuenta()