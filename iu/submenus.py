from negocio.negocio_cliente import (desactivar_cliente, reactivar_cliente)
from negocio.negocio_cuentas import (desactivar_cuenta, reactivar_cuenta)
from negocio.negocio_listados import (listar_clientes, listar_cuentas, listar_direcciones)

def menu_estado():
    """
    Submenú para activar o desactivar clientes y cuentas bancarias.
    """
    while True:
        print("\n==== Desactivar / Reactivar ====")
        print("[1] Desactivar cliente")
        print("[2] Reactivar cliente")
        print("[3] Desactivar cuenta bancaria")
        print("[4] Reactivar cuenta bancaria")
        print("[0] Volver")

        opcion = input("Opción: ").strip()

        #Desactivar cliente
        if opcion == "1":
            try:
                id_cliente = int(input("ID del cliente a desactivar: ").strip())
                desactivar_cliente(id_cliente)
            except ValueError:
                print("El ID debe ser un número entero válido.")

        #Reactivar cliente
        elif opcion == "2":
            try:
                id_cliente = int(input("ID del cliente a reactivar: ").strip())
                reactivar_cliente(id_cliente)
            except ValueError:
                print("El ID debe ser un número entero válido.")

        #Desactivar cuenta
        elif opcion == "3":
            try:
                id_cuenta = int(input("ID de la cuenta a desactivar: ").strip())
                desactivar_cuenta(id_cuenta)
            except ValueError:
                print("El ID debe ser un número entero válido.")

        #Reactivar cuenta
        elif opcion == "4":
            try:
                id_cuenta = int(input("ID de la cuenta a reactivar: ").strip())
                reactivar_cuenta(id_cuenta)
            except ValueError:
                print("El ID debe ser un número entero válido.")

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")
#def menu_estado()


def menu_listados():
    """
    Submenú para listar información del sistema.
    """
    while True:
        print("\n==== Submenú de Listados ====")
        print("[1] Listar clientes")
        print("[2] Listar cuentas bancarias")
        print("[3] Listar direcciones de clientes")
        print("[0] Volver")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            listar_cuentas()
        elif opcion == "3":
            listar_direcciones()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
#def menu_listados()