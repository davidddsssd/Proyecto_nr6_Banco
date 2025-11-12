from negocio.negocio_cliente import crear_cliente, desactivar_cliente, reactivar_cliente
from negocio.negocio_cuentas import crear_cuenta
from auxiliares.direcciones_base import listar_regiones, listar_comunas_por_region, obtener_comuna
import re

def menu_admin():
    while True:
        print("\n*** Menú del Administrador ***")
        print("[1] Registrar nuevo cliente")
        print("[2] Crear cuenta bancaria")
        print("[3] Desactivar cliente")
        print("[4] Reactivar cliente")
        print("[0] Volver al menú anterior")

        opcion = input("Opción: ").strip()

        # === 1. Registrar nuevo cliente ===
        if opcion == "1":
            print("\n--- Nuevo cliente ---")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            rut = input("RUT: ").strip()
            telefono = input("Teléfono: ").strip()
            mail = input("Correo (opcional): ").strip()

            # Selección de región (solo para organizar las comunas, no se guarda)
            print("\nSeleccione la REGIÓN:")
            regiones = listar_regiones()
            for i, r in enumerate(regiones, start=1):
                print(f"[{i}] {r}")

            try:
                opcion_region = int(input("Región (número): ").strip())
                region = regiones[opcion_region - 1]
            except (ValueError, IndexError):
                print("Región no válida. Intente nuevamente.")
                continue

            # Selección de comuna (ciudad)
            print(f"\nSeleccione la COMUNA de la {region}:")
            comunas = listar_comunas_por_region(region)
            for i, c in enumerate(comunas, start=1):
                print(f"[{i}] {c}")

            try:
                opcion_comuna = int(input("Comuna (número): ").strip())
                comuna = obtener_comuna(region, opcion_comuna)
            except (ValueError, IndexError):
                print("Comuna no válida. Intente nuevamente.")
                continue

            # Validar calle
            while True:
                calle = input("\nCalle: ").strip()
                if not calle.replace(" ", "").isalpha():
                    print("La calle solo puede contener letras y espacios.")
                elif not calle:
                    print("Debe ingresar un nombre de calle.")
                else:
                    break

            # Departamento (opcional)
            departamento = input("Departamento (opcional, presione Enter si no aplica): ").strip()
            if departamento == "":
                departamento = None

            # Número de dirección
            while True:
                numero_d = input("Número de dirección: ").strip()
                if not numero_d.isdigit():
                    print("El número de dirección solo debe contener números.")
                else:
                    break

            # Crear el cliente (la comuna actúa como ciudad)
            crear_cliente(
                nombre=nombre,
                apellido=apellido,
                rut=rut,
                telefono=telefono,
                mail=mail,
                comuna=comuna,
                calle=calle,
                departamento=departamento,
                numero_d=numero_d
            )

        # === 2. Crear nueva cuenta ===
        elif opcion == "2":
            print("\n--- Nueva cuenta ---")
            id_cliente_str = input("ID del cliente: ").strip()
            if not id_cliente_str.isdigit():
                print("El ID del cliente debe ser un número válido.")
                continue
            id_cliente = int(id_cliente_str)

            numero_c = input("Número de cuenta (formato 001-0001-000001): ").strip()
            if not re.match(r'^\d{3}-\d{4}-\d{6}$', numero_c):
                print("Formato de número de cuenta inválido. Ejemplo: 001-0001-000001")
                continue

            saldo_str = input("Saldo inicial: ").strip()
            try:
                saldo = float(saldo_str)
            except ValueError:
                print("El saldo inicial debe ser un número válido (por ejemplo: 10000 o 5000.50).")
                continue

            tipo = input("Tipo de cuenta (corriente / ahorro / vista): ").strip().lower()
            tipos_validos = ["corriente", "ahorro", "vista"]
            if tipo not in tipos_validos:
                print("Tipo de cuenta inválido. Debe ser: corriente, ahorro o vista.")
                continue

            crear_cuenta(id_cliente, numero_c, saldo, tipo)

        # === 3. Desactivar cliente ===
        elif opcion == "3":
            try:
                id_cliente = int(input("ID del cliente a desactivar: ").strip())
            except ValueError:
                print("El ID debe ser un número entero válido.")
                continue
            desactivar_cliente(id_cliente)

        # === 4. Reactivar cliente ===
        elif opcion == "4":
            try:
                id_cliente = int(input("ID del cliente a reactivar: ").strip())
            except ValueError:
                print("El ID debe ser un número entero válido.")
                continue
            reactivar_cliente(id_cliente)

        # === 0. Volver ===
        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")
#def menu_admin()