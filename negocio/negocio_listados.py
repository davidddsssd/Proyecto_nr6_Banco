from modelos.cliente import Cliente
from modelos.cuenta import Cuenta
from modelos.direccion import Direccion
from datos.conexion import Session


def listar_clientes():
    """
    Muestra todos los clientes registrados con sus datos principales
    """
    sesion = Session()
    try:
        clientes = sesion.query(Cliente).all()
        if not clientes:
            print("No hay clientes registrados.")
            return

        print("\n==== LISTADO DE CLIENTES ====")
        for c in clientes:
            estado = "Activo" if c.estado_cliente else "Inactivo"
            print(f"\nID: {c.id_cliente}")
            print(f"Nombre: {c.nombre} {c.apellido}")
            print(f"RUT: {c.rut}")
            print(f"Teléfono: {c.telefono}")
            print(f"Correo: {c.mail if c.mail else 'No registrado'}")
            print(f"Estado: {estado}")
            print("-" * 40)

    except Exception as e:
        print("Error al listar clientes:", e)
    finally:
        sesion.close()
#def listar_clientes()


def listar_cuentas():
    """
    Muestra las cuentas junto con los datos del cliente asociado
    """
    sesion = Session()
    try:
        cuentas = sesion.query(Cuenta).all()
        if not cuentas:
            print("No hay cuentas registradas.")
            return

        print("\n==== LISTADO DE CUENTAS BANCARIAS ====")
        for cuenta in cuentas:
            cliente = sesion.query(Cliente).filter_by(id_cliente=cuenta.id_cliente).first()

            if cliente:
                print(f"\nCliente: {cliente.nombre} {cliente.apellido} (RUT: {cliente.rut})")
            else:
                print("\nCliente: No encontrado")

            print(f"N° Cuenta: {cuenta.numero_c}")
            print(f"Tipo: {cuenta.tipo_cuenta}")
            print(f"Fecha de apertura: {cuenta.fecha_apertura}")
            print(f"Saldo: ${cuenta.saldo:,.2f}")
            estado = "Activa" if cuenta.estado_cuenta else "Cerrada"
            print(f"Estado: {estado}")
            print("-" * 50)

    except Exception as e:
        print("Error al listar cuentas:", e)
    finally:
        sesion.close()
#def listar_cuentas()

def listar_direcciones():
    """
    Muestra las direcciones asociadas a los clientes
    """
    sesion = Session()
    try:
        clientes = sesion.query(Cliente).all()
        if not clientes:
            print("No hay clientes registrados.")
            return

        print("\n==== LISTADO DE DIRECCIONES DE CLIENTES ====")
        for c in clientes:
            direccion = sesion.query(Direccion).filter_by(id_direccion=c.id_direccion).first()
            if not direccion:
                print(f"\nCliente: {c.nombre} {c.apellido} (RUT: {c.rut})")
                print("Dirección: No registrada")
                print("-" * 50)
                continue

            print(f"\nCliente: {c.nombre} {c.apellido} (RUT: {c.rut})")
            print(f"Comuna: {direccion.comuna}")
            print(f"Calle: {direccion.calle}")
            print(f"Número: {direccion.numero_d}")
            print(f"Departamento: {direccion.departamento if direccion.departamento else 'No aplica'}")
            print("-" * 50)

    except Exception as e:
        print("Error al listar direcciones:", e)
    finally:
        sesion.close()
#def listar_direcciones()