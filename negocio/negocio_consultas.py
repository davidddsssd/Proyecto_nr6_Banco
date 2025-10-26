from datos.conexion import Session
from modelos.cuenta import Cuenta
from modelos.transaccion import Transaccion

def consultar_saldo(numero_cuenta: str):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if cuenta:
            print(f"Saldo actual: ${cuenta.saldo:.2f}")
            return cuenta.saldo
        else:
            print("Cuenta no encontrada.")
    finally:
        session.close()


def listar_movimientos(numero_cuenta: str):
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()
        if not cuenta:
            print("Cuenta no encontrada.")
            return

        transacciones = session.query(Transaccion).filter_by(id_cuenta=cuenta.id_cuenta).order_by(Transaccion.fecha_transaccion.desc()).all()
        if not transacciones:
            print("No hay transacciones registradas.")
            return

        print(f"\nMovimientos de la cuenta {numero_cuenta}:")
        for t in transacciones:
            print(f"- [{t.fecha_transaccion}] {t.tipo_transaccion.capitalize()} ${t.monto:.2f} | {t.descripcion or ''}")
    finally:
        session.close()