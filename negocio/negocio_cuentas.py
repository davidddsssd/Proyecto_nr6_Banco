from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cuenta import Cuenta
from modelos.cliente import Cliente
from datos.conexion import Session
import re
from datetime import datetime


def crear_cuenta(id_cliente, numero_c, saldo_inicial, tipo_cuenta, estado=True):
    """
    Crea una nueva cuenta bancaria asociada a un cliente existente.
    Validaciones:
    - Cliente debe existir
    - Número de cuenta con formato 001-0001-000001
    - Número de cuenta no duplicado
    - Saldo inicial numérico y <= 5.000.000
    - Tipo de cuenta válido (corriente, ahorro, vista)
    """

    sesion = Session()

    try:
        # Validar que el cliente exista
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID. Regístrelo antes de crear la cuenta.")
            return

        # Validar formato del número de cuenta
        patron_cuenta = re.compile(r'^\d{3}-\d{4}-\d{6}$')
        if not patron_cuenta.match(numero_c):
            print("Formato de número de cuenta inválido. Ejemplo correcto: 001-0001-000001")
            return

        # Verificar que el número de cuenta no se repita
        cuenta_existente = sesion.query(Cuenta).filter_by(numero_c=numero_c).first()
        if cuenta_existente:
            print("Ya existe una cuenta con ese número.")
            return

        # Validar que el saldo sea numérico
        try:
            saldo_inicial = float(saldo_inicial)
        except ValueError:
            print("El saldo inicial debe ser un número válido.")
            return

        # Validar monto máximo de saldo inicial
        if saldo_inicial < 0:
            print("El saldo inicial no puede ser negativo.")
            return
        if saldo_inicial > 5000000:
            print("El saldo inicial no puede superar los $5.000.000.")
            return

        # Validar tipo de cuenta
        tipo_cuenta = tipo_cuenta.lower()
        tipos_validos = ['corriente', 'ahorro', 'vista']
        if tipo_cuenta not in tipos_validos:
            print("Tipo de cuenta inválido. Debe ser: corriente, ahorro o vista.")
            return

        # Crear nueva cuenta
        nueva = Cuenta(
            id_cliente=id_cliente,
            numero_c=numero_c,
            saldo=saldo_inicial,
            fecha_apertura=datetime.now(),
            tipo_cuenta=tipo_cuenta,
            estado_cuenta=estado
        )

        # Insertar en la base de datos
        insertar_objeto(nueva)
        print(f"Cuenta creada correctamente para {cliente.nombre} {cliente.apellido}.")
        print(f"   Número de cuenta: {numero_c}")
        print(f"   Tipo: {tipo_cuenta.capitalize()} | Saldo inicial: ${saldo_inicial:,.2f}")

    except Exception as e:
        print("Error al crear cuenta:", e)

    finally:
        sesion.close()
#def crear_cuenta()