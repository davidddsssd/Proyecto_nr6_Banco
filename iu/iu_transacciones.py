def datos_deposito():
    """
    Solicita los datos necesarios para realizar un depósito.
    Retorna:
        tuple: (número de cuenta, monto, descripción)
    """
    print("\n*** Depósito ***")
    numero_cuenta = input("N° de cuenta donde desea depositar: ").strip()
    monto = input("Monto a depositar: ").strip()
    descripcion = input("Descripción (opcional): ").strip()
    return (numero_cuenta, monto, descripcion)
#def datos_deposito()


def datos_retiro():
    """
    Solicita los datos necesarios para realizar un retiro.
    Retorna:
        tuple: (número de cuenta, monto, descripción)
    """
    print("\n*** Retiro ***")
    numero_cuenta = input("N° de cuenta desde donde desea retirar: ").strip()
    monto = input("Monto a retirar: ").strip()
    descripcion = input("Descripción (opcional): ").strip()
    return (numero_cuenta, monto, descripcion)
#def datos_retiro()


def datos_transferencia():
    """
    Solicita los datos necesarios para realizar una transferencia.
    Retorna:
        tuple: (cuenta_origen, cuenta_destino, monto, descripción)
    """
    print("\n*** Transferencia ***")
    cuenta_origen = input("Número de cuenta origen: ").strip()
    cuenta_destino = input("Número de cuenta destino: ").strip()
    monto = input("Monto a transferir: ").strip()
    descripcion = input("Motivo o descripción (opcional): ").strip()
    return (cuenta_origen, cuenta_destino, monto, descripcion)
#def datos_transferencia()