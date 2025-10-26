from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cliente import Cliente
from auxiliares.estandarizar_strings import normalizar_string

def crear_cliente(nombre, apellido, rut, telefono, mail, id_direccion=None):
    clientes = obtener_datos_objetos(Cliente)
    for c in clientes:
        if normalizar_string(c.rut) == normalizar_string(rut):
            print("Ya existe un cliente con ese RUT.")
            return
        if normalizar_string(c.telefono) == normalizar_string(telefono):
            print("Ya existe un cliente con ese teléfono.")
            return

    nuevo = Cliente(
        id_direccion=id_direccion,
        nombre=nombre,
        apellido=apellido,
        rut=rut,
        telefono=telefono,
        mail=mail
    )
    insertar_objeto(nuevo)