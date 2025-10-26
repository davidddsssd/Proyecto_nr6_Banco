from prettytable import PrettyTable
from datos.obtener_datos import obtener_datos_objetos

from modelos.direccion import Direccion
from modelos.cliente import Cliente
from modelos.cuenta import Cuenta
from modelos.cuenta_destino import CuentaDestino
from modelos.transaccion import Transaccion

def listado_direccion():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Comuna', 'Calle', 'Departamento', 'N°']
    direcciones = obtener_datos_objetos(Direccion)
    if direcciones:
        for d in direcciones:
            tabla.add_row([
                getattr(d, 'id_direccion', getattr(d, 'id', None)),
                getattr(d, 'comuna', getattr(d, 'nombre_comuna', '')),
                getattr(d, 'calle', ''),
                getattr(d, 'departamento', ''),
                getattr(d, 'numero_d', getattr(d, 'numero', ''))])
        print(tabla)
    else:
        print("No se encontraron direcciones.")
#def listado_direccion()

def listado_cliente():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'ID Dirección', 'Nombre', 'Apellido', 'RUT', 'Teléfono', 'Mail']
    clientes = obtener_datos_objetos(Cliente)
    if clientes:
        for c in clientes:
            tabla.add_row([
                getattr(c, 'id_cliente', getattr(c, 'id', None)),
                getattr(c, 'id_direccion', ''),
                getattr(c, 'nombre', getattr(c, 'razon_social', '')),
                getattr(c, 'apellido', ''),
                getattr(c, 'rut', ''),
                getattr(c, 'telefono', ''),
                getattr(c, 'mail', getattr(c, 'correo_contacto', ''))])
        print(tabla)
    else:
        print("No se encontraron clientes.")
#def listado_cliente()

def listado_cuenta():
    tabla = PrettyTable()
    tabla.field_names = ['ID Cuenta', 'ID Cliente', 'Número', 'Saldo', 'Fecha apertura', 'Tipo', 'Estado']
    cuentas = obtener_datos_objetos(Cuenta)
    if cuentas:
        for cu in cuentas:
            tabla.add_row([
                getattr(cu, 'id_cuenta', getattr(cu, 'id', None)),
                getattr(cu, 'id_cliente', ''),
                getattr(cu, 'numero_c', getattr(cu, 'numero', '')),
                getattr(cu, 'saldo', ''),
                getattr(cu, 'fecha_apertura', getattr(cu, 'fecha', '')),
                getattr(cu, 'tipo_cuenta', getattr(cu, 'tipo', '')),
                getattr(cu, 'estado_cuenta', getattr(cu, 'habilitado', ''))])
        print(tabla)
    else:
        print("No se encontraron cuentas.")
#def listado_cuenta()

def listado_cuenta_destino():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Tipo', 'Estado', 'Titular']
    destinos = obtener_datos_objetos(CuentaDestino)
    if destinos:
        for cd in destinos:
            tabla.add_row([
                getattr(cd, 'id_cuenta_destino', getattr(cd, 'id', None)),
                getattr(cd, 'tipo_cuenta_destino', getattr(cd, 'tipo', '')),
                getattr(cd, 'estado_cuenta_destino', getattr(cd, 'estado', '')),
                getattr(cd, 'nombre_titular', '')])
        print(tabla)
    else:
        print("No se encontraron cuentas destino.")
#def listado_cuenta_destino()

def listado_transaccion():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'ID Cuenta', 'ID Destino', 'Tipo', 'Fecha', 'Monto', 'Descripción']
    transacciones = obtener_datos_objetos(Transaccion)
    if transacciones:
        for t in transacciones:
            tabla.add_row([
                getattr(t, 'id_transaccion', getattr(t, 'id', None)),
                getattr(t, 'id_cuenta', getattr(t, 'id_cuenta_origen', '')),
                getattr(t, 'id_cuenta_destino', ''),
                getattr(t, 'tipo_transaccion', getattr(t, 'tipo', '')),
                getattr(t, 'fecha_transaccion', getattr(t, 'fecha', '')),
                getattr(t, 'monto', ''),
                getattr(t, 'descripcion', '')])
        print(tabla)
    else:
        print("No se encontraron transacciones.")
#def listado_transaccion()

def menu_simple():
    while True:
        print("\n*** Menú rápido de pruebas ***")
        print("[1] Listar direcciones")
        print("[2] Listar clientes")
        print("[3] Listar cuentas")
        print("[4] Listar cuentas destino")
        print("[5] Listar transacciones")
        print("[0] Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == '1':
            listado_direccion()
        elif opcion == '2':
            listado_cliente()
        elif opcion == '3':
            listado_cuenta()
        elif opcion == '4':
            listado_cuenta_destino()
        elif opcion == '5':
            listado_transaccion()
        elif opcion == '0':
            print("Saliendo.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_simple()