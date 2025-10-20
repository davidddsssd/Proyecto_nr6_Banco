from datos.obtener_datos import obtener_datos_objetos
from prettytable import PrettyTable
from modelos.direccion import Direccion

def listado_direccion():
    tabla_direcciones = PrettyTable()
    tabla_direcciones.field_names = ['Código dirección', 'Nombre comuna', 'Nombre calle', 'Departamento', 'N° departamento']

    direcciones = obtener_datos_objetos(Direccion)

    if direcciones:
        for direccion in direcciones:
            tabla_direcciones.add_row([
                direccion.id_direccion,
                direccion.comuna,
                direccion.calle,
                direccion.departamento,
                direccion.numero_d
            ])
            print(f"{direccion.id_direccion} {direccion.comuna} {direccion.calle} {direccion.departamento} {direccion.numero_d}")

        print(tabla_direcciones)
    else:
        print("No se encontraron direcciones registradas.")