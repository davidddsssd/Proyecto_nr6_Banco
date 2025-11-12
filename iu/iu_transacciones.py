def datos_deposito():
    """
    Solicita los datos necesarios para realizar un depósito
    """
    print("\n==== Depósito ====")
    numero_cuenta = input("N° de cuenta: ").strip()
    monto = input("Monto a depositar: ").strip()
    descripcion = input("Descripción (Opcional (ENTER)): ").strip()
    return (numero_cuenta, monto, descripcion)
#def datos_deposito()


def datos_retiro():
    """
    Solicita los datos necesarios para realizar un retiro
    """
    print("\n==== Retiro ====")
    numero_cuenta = input("N° de cuenta: ").strip()
    monto = input("Monto a retirar: ").strip()
    descripcion = input("Descripción (Opcional (ENTER)): ").strip()
    return (numero_cuenta, monto, descripcion)
#def datos_retiro()


def datos_transferencia():
    """
    Solicita los datos necesarios para realizar una transferencia
    """
    print("\n==== Transferencia ====")
    cuenta_origen = input("N° de cuenta origen: ").strip()
    cuenta_destino = input("N° de cuenta destino: ").strip()
    monto = input("Monto a transferir: ").strip()
    descripcion = input("Descripción (Opcional (ENTER)): ").strip()
    return (cuenta_origen, cuenta_destino, monto, descripcion)
#def datos_transferencia()