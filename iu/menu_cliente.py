from iu.iu_consultas import datos_consulta_saldo, datos_consulta_movimientos
from iu.iu_transacciones import datos_deposito, datos_retiro, datos_transferencia
from negocio.negocio_transacciones import realizar_deposito, realizar_retiro, realizar_transferencia
from negocio.negocio_consultas import consultar_saldo, listar_movimientos

def menu_cliente():
    while True:
        print("\n==== Menú del Cliente ====")
        print("[1] Consultar saldo")
        print("[2] Ver movimientos")
        print("[3] Depositar dinero")
        print("[4] Retirar dinero")
        print("[5] Transferir dinero")
        print("[0] Volver al menú anterior")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            cuenta = datos_consulta_saldo()
            consultar_saldo(cuenta)
        elif opcion == "2":
            cuenta = datos_consulta_movimientos()
            listar_movimientos(cuenta)
        elif opcion == "3":
            datos = datos_deposito()
            realizar_deposito(*datos)
        elif opcion == "4":
            datos = datos_retiro()
            realizar_retiro(*datos)
        elif opcion == "5":
            datos = datos_transferencia()
            realizar_transferencia(*datos)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
#def menu_cliente()