from negocio.negocio_cliente import (crear_cliente, modificar_cliente)
from negocio.negocio_cuentas import crear_cuenta
from auxiliares.direcciones_base import (listar_regiones, listar_comunas_por_region, obtener_comuna)
from iu.submenus import (menu_estado, menu_listados)
import re


def menu_admin():
    """
    Menú del administrador
    Permite gestionar clientes, cuentas, listados y estado de registros.
    """
    try:
        while True:
            print("\n==== Menú del Administrador ====")
            print("[1] Registrar nuevo cliente")
            print("[2] Crear cuenta bancaria")
            print("[3] Modificar cliente")
            print("[4] Desactivar / Reactivar")
            print("[5] Listar información")
            print("[0] Volver al menú anterior")

            opcion = input("Opción: ").strip()

            #Registrar nuevo cliente
            if opcion == "1":
                print("\n==== Nuevo cliente ====")
                nombre = input("Nombre: ").strip()
                apellido = input("Apellido: ").strip()
                rut = input("RUT: ").strip()
                telefono = input("Teléfono: ").strip()
                mail = input("Correo (Opcional (ENTER)): ").strip()

                print("\nSeleccione la región:")
                regiones = listar_regiones()
                for i, r in enumerate(regiones, start=1):
                    print(f"[{i}] {r}")
                try:
                    opcion_region = int(input("Región (número): ").strip())
                    region = regiones[opcion_region - 1]
                except (ValueError, IndexError):
                    print("Región no válida.")
                    continue

                print(f"\nSeleccione la comuna de la {region}:")
                comunas = listar_comunas_por_region(region)
                for i, c in enumerate(comunas, start=1):
                    print(f"[{i}] {c}")
                try:
                    opcion_comuna = int(input("Comuna (número): ").strip())
                    comuna = obtener_comuna(region, opcion_comuna)
                except (ValueError, IndexError):
                    print("Comuna no válida.")
                    continue

                calle = input("Calle: ").strip()
                departamento = input("Departamento (Opcional (ENTER)): ").strip() or None
                numero_d = input("Número: ").strip()

                crear_cliente(nombre, apellido, rut, telefono, mail, comuna, calle, departamento, numero_d)

            # Crear cuenta bancaria
            elif opcion == "2":
                print("\n==== Nueva cuenta bancaria ====")
                id_cliente_str = input("ID del cliente: ").strip()
                if not id_cliente_str.isdigit():
                    print("El ID del cliente debe ser un número válido.")
                    continue
                id_cliente = int(id_cliente_str)

                numero_c = input("Número de cuenta (formato 001-0001-000001): ").strip()
                if not re.match(r'^\d{3}-\d{4}-\d{6}$', numero_c):
                    print("Formato inválido. Ejemplo: 001-0001-000001")
                    continue

                saldo_str = input("Saldo inicial: ").strip()
                try:
                    saldo = int(saldo_str)
                except ValueError:
                    print("El saldo inicial debe ser un número válido.")
                    continue

                tipo = input("Tipo de cuenta (corriente / ahorro / vista): ").strip().lower()
                if tipo not in ["corriente", "ahorro", "vista"]:
                    print("Tipo inválido.")
                    continue

                crear_cuenta(id_cliente, numero_c, saldo, tipo)

            # Modificar cliente
            elif opcion == "3":
                try:
                    id_cliente = int(input("ID del cliente a modificar: ").strip())
                    modificar_cliente(id_cliente)
                except ValueError:
                    print("El ID debe ser un número entero válido.")

            # Submenú de estado (clientes / cuentas)
            elif opcion == "4":
                menu_estado()

            # Submenú de listados
            elif opcion == "5":
                menu_listados()

            # Salir
            elif opcion == "0":
                print("\nVolviendo al menú principal...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario. Regresando al menú principal...\n")
    except Exception as e:
        print(f"\nError inesperado en el menú del administrador: {e}")
#def menu_admin()