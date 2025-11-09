from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cliente import Cliente
from modelos.direccion import Direccion
from auxiliares import normalizar_cadena
from datos.conexion import Session
from rut_chile import rut_chile

def crear_cliente(nombre, apellido, rut, telefono, mail=None, id_direccion=None):
    # Validar campos obligatorios
    if not nombre or not apellido or not rut or not telefono:
        print("Faltan datos obligatorios (nombre, apellido, RUT o teléfono).")
        return

    # Validar formato de RUT
    if not rut_chile.is_valid_rut(rut):
        print("El RUT ingresado no es válido. Ejemplo correcto: 12.345.678-9")
        return

    # Conexión a la base de datos
    sesion = Session()

    try:
        # Verificar si el cliente ya existe (por RUT o teléfono)
        clientes = sesion.query(Cliente).all()
        for c in clientes:
            if normalizar_cadena(c.rut) == normalizar_cadena(rut):
                print("Ya existe un cliente con ese RUT.")
                return
            if normalizar_cadena(c.telefono) == normalizar_cadena(telefono):
                print("Ya existe un cliente con ese teléfono.")
                return

        # Seleccionar o confirmar dirección válida
        if id_direccion is None:
            print("\nDebe indicar una dirección existente (ID de 1 a 20).")
            direcciones = sesion.query(Direccion).all()
            print("Direcciones disponibles:")
            for d in direcciones:
                print(f"  [{d.id_direccion}] {d.calle}, {d.comuna}")
            try:
                id_direccion = int(input("\nIngrese el ID de la dirección: "))
            except:
                print("ID inválido.")
                return

        # Confirmar que la dirección exista
        direccion = sesion.query(Direccion).filter_by(id_direccion=id_direccion).first()
        if not direccion:
            print("El ID de dirección no existe en la base de datos.")
            return

        # Crear el nuevo cliente
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

    except Exception as e:
        print("Error al registrar cliente:", e)

    finally:
        sesion.close()
#def crear_cliente()