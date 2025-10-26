from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cuenta import Cuenta

def crear_cuenta(id_cliente, numero_c, saldo_inicial, tipo_cuenta, estado=True):
    cuentas = obtener_datos_objetos(Cuenta)
    for c in cuentas:
        if c.numero_c == numero_c:
            print("Ya existe una cuenta con ese número.")
            return

    nueva = Cuenta(
        id_cliente=id_cliente,
        numero_c=numero_c,
        saldo=saldo_inicial,
        tipo_cuenta=tipo_cuenta,
        estado_cuenta=estado
    )
    insertar_objeto(nueva)