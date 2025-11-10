from iu.menu_cliente import menu_cliente
from iu.menu_admin import menu_admin

def menu_inicio():
    while True:
        print("\n*** Bienvenido al Sistema de Gestión Bancaria ***")
        print("[1] Ingresar como Cliente")
        print("[2] Ingresar como Administrador")
        print("[0] Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_admin()
        elif opcion == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
#def menu_inicio()