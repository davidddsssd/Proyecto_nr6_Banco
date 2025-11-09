from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cliente import Cliente
from auxiliares import normalizar_cadena

def crear_cliente(nombre, apellido, rut, telefono, mail=None, id_direccion=None):
    # Validar campos obligatorios
    if not nombre or not apellido or not rut or not telefono:
        print("Faltan datos obligatorios.")
        return

    # Verificar si el cliente ya existe
    clientes = obtener_datos_objetos(Cliente)
    for c in clientes:
        if normalizar_cadena(c.rut) == normalizar_cadena(rut):
            print("Ya existe un cliente con ese RUT.")
            return
        if normalizar_cadena(c.telefono) == normalizar_cadena(telefono):
            print("Ya existe un cliente con ese teléfono.")
            return

    # Crear objeto Cliente
    nuevo = Cliente(
        id_direccion=id_direccion,
        nombre=nombre,
        apellido=apellido,
        rut=rut,
        telefono=telefono,
        mail=mail
    )

    # Insertar en la base de datos
    insertar_objeto(nuevo)
    print("Cliente registrado correctamente.")
#def crear_cliente()