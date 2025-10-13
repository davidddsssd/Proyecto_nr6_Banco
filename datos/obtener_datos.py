from datos.conexion import Session
from modelos.direccion import Direccion
from modelos.cliente import Cliente
from sqlalchemy import func

sesion = Session()

def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos

def obtener_datos_direccion():
    listado_direccion = sesion.query(Direccion).all()
    if listado_direccion:
        for direccion in listado_direccion:
            print(f'{direccion.id_direccion} {direccion.comuna} {direccion.calle} {direccion.departamente} {direccion.numero_d}')

def obtener_datos_clientes():
    listado_clientes = sesion.query(Cliente).all()
    if listado_clientes:
        for cliente in listado_clientes:
            print(f'{cliente.id_cliente}{cliente.nombre}{cliente.apellido}{cliente.rut}{cliente.telefono}{cliente.mail}')