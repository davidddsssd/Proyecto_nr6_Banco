def datos_consulta_saldo():
    """
    Solicita al usuario el número de cuenta para realizar una consulta de saldo.
    Retorna:
        str: número de cuenta ingresado por el usuario.
    """
    print("\n*** Consulta de saldo ***")
    numero_cuenta = input("Número de cuenta: ").strip()
    return numero_cuenta
#def datos_consulta_saldo()

def datos_consulta_movimientos():
    """
    Solicita al usuario el número de cuenta para listar sus movimientos.
    Retorna:
        str: número de cuenta ingresado por el usuario.
    """
    print("\n*** Consulta de movimientos ***")
    numero_cuenta = input("Número de cuenta: ").strip()
    return numero_cuenta
#def datos_consulta_movimientos()