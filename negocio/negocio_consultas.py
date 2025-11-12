from datos.conexion import Session
from modelos.cuenta import Cuenta
from modelos.transaccion import Transaccion


def consultar_saldo(numero_cuenta):
    """
    Muestra el saldo actual de una cuenta según su número.
    Solo se permite si la cuenta está activa.
    """
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()

        if not cuenta:
            print("❌ Cuenta no encontrada.")
            return

        # 🔒 Validar si la cuenta está activa
        if not cuenta.estado_cuenta:
            print("⚠️ Esta cuenta está desactivada. No puede consultar el saldo.")
            return

        print(f"💰 Saldo actual de la cuenta {numero_cuenta}: ${cuenta.saldo:,}")
        return cuenta.saldo

    except Exception as e:
        print(f"❌ Error al consultar saldo: {e}")
    finally:
        session.close()
#def consultar_saldo()


def listar_movimientos(numero_cuenta):
    """
    Lista todas las transacciones de una cuenta activa,
    ordenadas por fecha descendente.
    """
    session = Session()
    try:
        cuenta = session.query(Cuenta).filter_by(numero_c=numero_cuenta).first()

        if not cuenta:
            print("❌ Cuenta no encontrada.")
            return

        # 🔒 Validar si la cuenta está activa
        if not cuenta.estado_cuenta:
            print("⚠️ La cuenta está desactivada. No se pueden ver movimientos.")
            return

        transacciones = (
            session.query(Transaccion)
            .filter_by(id_cuenta=cuenta.id_cuenta)
            .order_by(Transaccion.fecha_transaccion.desc())
            .all()
        )

        if not transacciones:
            print(f"📭 No hay transacciones registradas para la cuenta {numero_cuenta}.")
            return

        print(f"\n📋 Movimientos de la cuenta {numero_cuenta}:")
        print("-" * 70)
        for t in transacciones:
            tipo = t.tipo_transaccion.replace("_", " ").capitalize()
            descripcion = t.descripcion or ""
            print(f"[{t.fecha_transaccion}] {tipo} ${t.monto:,} | {descripcion}")
        print("-" * 70)

    except Exception as e:
        print(f"❌ Error al listar movimientos: {e}")
    finally:
        session.close()
#def listar_movimientos()