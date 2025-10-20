from datos.obtener_datos import obtener_datos_objetos
from prettytable import PrettyTable

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
            tabla.add_row([d.id_direccion, d.comuna, d.calle, d.departamento, d.numero_d])
            print(f"{d.id_direccion} {d.comuna} {d.calle} {d.departamento} {d.numero_d}")
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
            tabla.add_row([c.id_cliente, c.id_direccion, c.nombre, c.apellido, c.rut, c.telefono, c.mail])
            print(f"{c.id_cliente} {c.id_direccion} {c.nombre} {c.apellido} {c.rut} {c.telefono} {c.mail}")
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
            tabla.add_row([cu.id_cuenta, cu.id_cliente, cu.numero_c, cu.saldo, cu.fecha_apertura, cu.tipo_cuenta, cu.estado_cuenta])
            print(f"{cu.id_cuenta} {cu.id_cliente} {cu.numero_c} {cu.saldo} {cu.fecha_apertura} {cu.tipo_cuenta} {cu.estado_cuenta}")
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
            tabla.add_row([cd.id_cuenta_destino, cd.tipo_cuenta_destino, cd.estado_cuenta_destino, cd.nombre_titular])
            print(f"{cd.id_cuenta_destino} {cd.tipo_cuenta_destino} {cd.estado_cuenta_destino} {cd.nombre_titular}")
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
            tabla.add_row([t.id_transaccion, t.id_cuenta, t.id_cuenta_destino, t.tipo_transaccion, t.fecha_transaccion, t.monto, t.descripcion])
            print(f"{t.id_transaccion} {t.id_cuenta} {t.id_cuenta_destino} {t.tipo_transaccion} {t.fecha_transaccion} {t.monto} {t.descripcion}")
        print(tabla)
    else:
        print("No se encontraron transacciones.")
#def listado_transaccion()