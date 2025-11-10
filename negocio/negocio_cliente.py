from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos
from modelos.cliente import Cliente
from modelos.direccion import Direccion
from auxiliares import normalizar_cadena
from auxiliares.validaciones import (validar_telefono, validar_correo, formatear_nombre, validar_rut_chileno)
from datos.conexion import Session


def crear_cliente(nombre, apellido, rut, telefono, mail=None, id_direccion=None):
    # Validar campos obligatorios
    if not nombre or not apellido or not rut or not telefono:
        print("Faltan datos obligatorios (nombre, apellido, RUT o teléfono).")
        return

    # Limpieza básica
    nombre = nombre.strip()
    apellido = apellido.strip()
    rut = rut.strip()
    telefono = telefono.strip()
    if mail:
        mail = mail.strip()

    # Formatear nombre y apellido (mayúscula inicial)
    nombre = formatear_nombre(nombre)
    apellido = formatear_nombre(apellido)

    # Validar formato de RUT chileno
    if not validar_rut_chileno(rut):
        print("El RUT ingresado no es válido. Ejemplo correcto: 12.345.678-9")
        return

    # Validar formato de teléfono chileno
    if not validar_telefono(telefono):
        print("El teléfono ingresado no es válido. Ejemplo correcto: +56912345678 o 912345678")
        return

    # Validar formato de correo electrónico (si se ingresó)
    if mail and not validar_correo(mail):
        print("El correo ingresado no es válido. Ejemplo: ejemplo@dominio.com")
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
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
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
        print("Cliente registrado correctamente con datos válidos.")

    except Exception as e:
        print("Error al registrar cliente:", e)

    finally:
        sesion.close()
#def crear_cliente()