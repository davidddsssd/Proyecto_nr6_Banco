from datetime import datetime
from datos.conexion import Session
from modelos.cuenta import Cuenta
from modelos.transaccion import Transaccion

def realizar_deposito(numero_cuenta, monto, descripcion=None):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if not cuenta:
            print("Cuenta no encontrada.")
            return

        cuenta.saldo += float(monto)
        trans = Transaccion(
            id_cuenta=cuenta.id_cuenta,
            tipo_transaccion='depósito',
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )
        session.add(trans)
        session.commit()
        print(f"Depósito realizado. Nuevo saldo: ${cuenta.saldo}")
    except Exception as e:
        session.rollback()
        print(f"Error al depositar: {e}")
    finally:
        session.close()


def realizar_retiro(numero_cuenta, monto, descripcion=None):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if not cuenta:
            print("Cuenta no encontrada.")
            return
        if cuenta.saldo < float(monto):
            print("Saldo insuficiente.")
            return

        cuenta.saldo -= float(monto)
        trans = Transaccion(
            id_cuenta=cuenta.id_cuenta,
            tipo_transaccion='retiro',
            monto=monto,
            descripcion=descripcion,
            fecha_transaccion=datetime.now()
        )
        session.add(trans)
        session.commit()
        print(f"Retiro realizado. Nuevo saldo: ${cuenta.saldo}")
    except Exception as e:
        session.rollback()
        print(f"Error al retirar: {e}")
    finally:
        session.close()


def realizar_transferencia(cuenta_origen, cuenta_destino, monto, descripcion=None):
    session = Session()
    try:
        origen = session.query(Cuenta).filter_by(numero_c=cuenta_origen).first()
        destino = session.query(Cuenta).filter_by(numero_c=cuenta_destino).first()

        if not origen or not destino:
            print("Cuenta origen o destino no encontrada.")
            return
        if origen.saldo < float(monto):
            print("Saldo insuficiente para transferir.")
            return

        origen.saldo -= float(monto)
        destino.saldo += float(monto)

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
        print("Transferencia realizada con éxito.")
    except Exception as e:
        session.rollback()
        print(f"Error en la transferencia: {e}")
    finally:
        session.close()