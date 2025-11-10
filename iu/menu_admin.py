from negocio.negocio_cliente import crear_cliente
from negocio.negocio_cuentas import crear_cuenta
import re

def menu_admin():
    while True:
        print("\n*** Menú del Administrador ***")
        print("[1] Registrar nuevo cliente")
        print("[2] Crear cuenta bancaria")
        print("[0] Volver al menú anterior")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            # Registro de nuevo cliente
            print("\n--- Nuevo cliente ---")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            rut = input("RUT: ").strip()
            telefono = input("Teléfono: ").strip()
            mail = input("Correo (opcional): ").strip()

            crear_cliente(nombre, apellido, rut, telefono, mail)

        elif opcion == "2":
            # Creación de nueva cuenta bancaria
            print("\n--- Nueva cuenta ---")

            # Validar ID del cliente
            id_cliente_str = input("ID del cliente: ").strip()
            if not id_cliente_str.isdigit():
                print("El ID del cliente debe ser un número válido.")
                continue
            id_cliente = int(id_cliente_str)

            # Validar número de cuenta con formato
            numero_c = input("Número de cuenta (formato 001-0001-000001): ").strip()
            if not re.match(r'^\d{3}-\d{4}-\d{6}$', numero_c):
                print("Formato de número de cuenta inválido. Ejemplo: 001-0001-000001")
                continue

            # Validar saldo inicial
            saldo_str = input("Saldo inicial: ").strip()
            try:
                saldo = float(saldo_str)
            except ValueError:
                print("El saldo inicial debe ser un número válido (por ejemplo: 10000 o 5000.50).")
                continue

            # Validar tipo de cuenta
            tipo = input("Tipo de cuenta (corriente / ahorro / vista): ").strip().lower()
            tipos_validos = ["corriente", "ahorro", "vista"]
            if tipo not in tipos_validos:
                print("Tipo de cuenta inválido. Debe ser: corriente, ahorro o vista.")
                continue

            # Llamar a la función de negocio
            crear_cuenta(id_cliente, numero_c, saldo, tipo)

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")
#def menu_admin()