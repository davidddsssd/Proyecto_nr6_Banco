from negocio.negocio_cliente import crear_cliente
from negocio.negocio_cuentas import crear_cuenta

def menu_admin():
    while True:
        print("\n*** Menú del Administrador ***")
        print("[1] Registrar nuevo cliente")
        print("[2] Crear cuenta bancaria")
        print("[0] Volver al menú anterior")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            print("\n--- Nuevo cliente ---")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            rut = input("RUT: ").strip()
            telefono = input("Teléfono: ").strip()
            mail = input("Correo (opcional): ").strip()

            crear_cliente(nombre, apellido, rut, telefono, mail)

        elif opcion == "2":
            print("\n--- Nueva cuenta ---")
            id_cliente = input("ID del cliente: ").strip()
            numero_c = input("Número de cuenta: ").strip()
            saldo = float(input("Saldo inicial: ").strip())
            tipo = input("Tipo de cuenta (corriente/ahorro/vista): ").strip()
            crear_cuenta(id_cliente, numero_c, saldo, tipo)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
#def menu_admin()