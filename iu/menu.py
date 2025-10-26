from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version
from iu.iu_transacciones import datos_deposito, datos_retiro, datos_transferencia
from iu.iu_consultas import datos_consulta_saldo, datos_consulta_movimientos

def menu():
    print(f"\n{nombre_aplicacion} v{numero_version}")
    print("=" * 40)

    while True:
        print("\nBienvenido al sistema bancario")
        print("Seleccione una opción:")
        print("[1] Consultar saldo")
        print("[2] Ver movimientos")
        print("[3] Realizar depósito")
        print("[4] Realizar retiro")
        print("[5] Transferir dinero")
        print("[0] Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            numero_cuenta = datos_consulta_saldo()
            print(f"\n(Consulta de saldo para la cuenta {numero_cuenta})")
        elif opcion == "2":
            numero_cuenta = datos_consulta_movimientos()
            print(f"\n(Consulta de movimientos para la cuenta {numero_cuenta})")
        elif opcion == "3":
            datos = datos_deposito()
            print("\nDatos del depósito ingresados:", datos)
        elif opcion == "4":
            datos = datos_retiro()
            print("\nDatos del retiro ingresados:", datos)
        elif opcion == "5":
            datos = datos_transferencia()
            print("\nDatos de la transferencia ingresados:", datos)
        elif opcion == "0":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")