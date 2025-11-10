from datetime import datetime
from datos.conexion import Session
from modelos.cuenta import Cuenta
from modelos.transaccion import Transaccion

# Depósito
def realizar_deposito(numero_cuenta, monto, descripcion=None):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if not cuenta:
            print("Cuenta no encontrada.")
            return

        # Validar monto
        try:
            monto = int(monto)
        except ValueError:
            print("El monto debe ser un número entero válido.")
            return

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            return
        if monto > 5000000:
            print("No se puede depositar más de $5.000.000 por operación.")
            return

        cuenta.saldo += monto

        trans = Transaccion(
            id_cuenta=cuenta.id_cuenta,
            tipo_transaccion='depósito',
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )

        session.add(trans)
        session.commit()
        print(f"Depósito realizado correctamente. Nuevo saldo: ${cuenta.saldo:,}")

    except Exception as e:
        session.rollback()
        print(f"Error al realizar depósito: {e}")
    finally:
        session.close()
#def realizar_deposito()


# Retiro
def realizar_retiro(numero_cuenta, monto, descripcion=None):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if not cuenta:
            print("Cuenta no encontrada.")
            return

        try:
            monto = int(monto)
        except ValueError:
            print("El monto debe ser un número entero válido.")
            return

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            return
        if cuenta.saldo < monto:
            print("Saldo insuficiente.")
            return

        cuenta.saldo -= monto

        trans = Transaccion(
            id_cuenta=cuenta.id_cuenta,
            tipo_transaccion='retiro',
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )

        session.add(trans)
        session.commit()
        print(f"Retiro realizado correctamente. Nuevo saldo: ${cuenta.saldo:,}")

    except Exception as e:
        session.rollback()
        print(f"Error al realizar retiro: {e}")
    finally:
        session.close()
#def realizar_retiro()


# Transferencia
def realizar_transferencia(cuenta_origen, cuenta_destino, monto, descripcion=None):
    session = Session()
    try:
        origen = session.query(Cuenta).filter_by(numero_c=cuenta_origen).first()
        destino = session.query(Cuenta).filter_by(numero_c=cuenta_destino).first()

        if not origen or not destino:
            print("Cuenta origen o destino no encontrada.")
            return

        try:
            monto = int(monto)
        except ValueError:
            print("El monto debe ser un número entero válido.")
            return

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            return
        if monto > 5000000:
            print("No se puede transferir más de $5.000.000 por operación.")
            return
        if origen.saldo < monto:
            print("Saldo insuficiente para realizar la transferencia.")
            return

        origen.saldo -= monto
        destino.saldo += monto

        trans_origen = Transaccion(
            id_cuenta=origen.id_cuenta,
            tipo_transaccion='transferencia_salida',
            id_cuenta_destino=destino.id_cuenta,
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )

        trans_destino = Transaccion(
            id_cuenta=destino.id_cuenta,
            tipo_transaccion='transferencia_entrada',
            id_cuenta_destino=origen.id_cuenta,
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )

        session.add_all([trans_origen, trans_destino])
        session.commit()
        print("Transferencia realizada correctamente.")
        print(f"Saldo origen: ${origen.saldo:,} | Saldo destino: ${destino.saldo:,}")

    except Exception as e:
        session.rollback()
        print(f"Error al realizar transferencia: {e}")
    finally:
        session.close()
#def realizar_transferencia()