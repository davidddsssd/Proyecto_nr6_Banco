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
    - Cliente debe existir
    - Número de cuenta con formato 001-0001-000001
    - Número no duplicado
    - Saldo inicial entero y <= 5.000.000
    - Tipo válido: corriente / ahorro / vista
    """
    sesion = Session()
    try:
        # Verificar cliente
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID. Regístrelo primero.")
            return

        # Validar número de cuenta
        if not re.match(r'^\d{3}-\d{4}-\d{6}$', numero_c):
            print("Formato inválido. Ejemplo: 001-0001-000001")
            return

        # Revisar duplicados
        if sesion.query(Cuenta).filter_by(numero_c=numero_c).first():
            print("Ya existe una cuenta con ese número.")
            return

        # Validar saldo
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

        # Validar tipo de cuenta
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