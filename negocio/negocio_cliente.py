from modelos.cliente import Cliente
from modelos.direccion import Direccion
from auxiliares import normalizar_cadena
from auxiliares.validaciones import (validar_telefono, validar_correo, formatear_nombre, validar_rut_chileno)
from auxiliares.direcciones_base import listar_regiones, listar_comunas_por_region, obtener_comuna
from datos.conexion import Session


def crear_cliente(nombre, apellido, rut, telefono, mail=None, comuna=None, calle=None, departamento=None, numero_d=None):
    """
    Crea un nuevo cliente junto con su dirección asociada,
    usando una única sesión para evitar conflictos entre objetos.
    """

    if not nombre or not apellido or not rut or not telefono or not comuna or not calle or not numero_d:
        print("Faltan datos obligatorios (nombre, apellido, rut, teléfono o dirección).")
        return

    # Normalización de texto
    nombre = formatear_nombre(nombre.strip())
    apellido = formatear_nombre(apellido.strip())
    rut = rut.strip()
    telefono = telefono.strip()
    if mail:
        mail = mail.strip()

    # Validaciones
    if not validar_rut_chileno(rut):
        print("El RUT ingresado no es válido. Ejemplo: 12345678-9")
        return

    if not validar_telefono(telefono):
        print("El teléfono ingresado no es válido. Ejemplo: 912345678")
        return

    if mail and not validar_correo(mail):
        print("El correo ingresado no es válido. Ejemplo: ejemplo@dominio.com")
        return

    sesion = Session()
    try:
        # Verificar duplicados
        clientes = sesion.query(Cliente).all()
        for c in clientes:
            if normalizar_cadena(c.rut) == normalizar_cadena(rut):
                print("Ya existe un cliente con ese RUT.")
                sesion.close()
                return
            if normalizar_cadena(c.telefono) == normalizar_cadena(telefono):
                print("Ya existe un cliente con ese teléfono.")
                sesion.close()
                return

        # Crear dirección y cliente dentro de la misma sesión
        nueva_direccion = Direccion(
            comuna=comuna.strip(),
            calle=calle.strip(),
            departamento=departamento,
            numero_d=str(numero_d).strip()
        )
        sesion.add(nueva_direccion)
        sesion.flush()

        nuevo_cliente = Cliente(
            id_direccion=nueva_direccion.id_direccion,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            telefono=telefono,
            mail=mail
        )
        sesion.add(nuevo_cliente)
        sesion.commit()

        print(f"\nCliente '{nombre} {apellido}' registrado correctamente.")
        print(f"Dirección guardada: {calle} #{numero_d}, {comuna}")

    except Exception as e:
        sesion.rollback()
        print("Error al registrar cliente:", e)
    finally:
        sesion.close()
#def crear_cliente()


def modificar_cliente(id_cliente):
    """
    Permite modificar los datos de un cliente existente mediante un menú de opciones.
    Incluye validaciones y un submenú para editar la dirección.
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID.")
            return

        direccion = sesion.query(Direccion).filter_by(id_direccion=cliente.id_direccion).first()

        while True:
            print("\n==== Modificar Cliente ====")
            print(f"Cliente actual: {cliente.nombre} {cliente.apellido} (RUT: {cliente.rut})")
            print(f"Teléfono: {cliente.telefono}")
            print(f"Correo: {cliente.mail if cliente.mail else 'No registrado'}")
            print(f"Dirección: {direccion.calle} #{direccion.numero_d}, {direccion.comuna}")
            if direccion.departamento:
                print(f"Departamento: {direccion.departamento}")

            print("\nSeleccione el dato que desea modificar:")
            print("[1] Nombre")
            print("[2] Apellido")
            print("[3] RUT")
            print("[4] Teléfono")
            print("[5] Correo")
            print("[6] Dirección")
            print("[0] Volver")

            opcion = input("Opción: ").strip()

            #Nombre
            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    cliente.nombre = formatear_nombre(nuevo_nombre)
                    sesion.commit()
                    print("Nombre actualizado correctamente.")
                else:
                    print("No se ingresó ningún nombre.")

            #Apellido
            elif opcion == "2":
                nuevo_apellido = input("Nuevo apellido: ").strip()
                if nuevo_apellido:
                    cliente.apellido = formatear_nombre(nuevo_apellido)
                    sesion.commit()
                    print("Apellido actualizado correctamente.")
                else:
                    print("No se ingresó ningún apellido.")

            #RUT
            elif opcion == "3":
                nuevo_rut = input("Nuevo RUT: ").strip()
                if not nuevo_rut:
                    print("No se ingresó ningún RUT.")
                    continue
                if not validar_rut_chileno(nuevo_rut):
                    print("El RUT ingresado no es válido.")
                    continue
                cliente.rut = nuevo_rut
                sesion.commit()
                print("RUT actualizado correctamente.")

            #Teléfono
            elif opcion == "4":
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                if not nuevo_telefono:
                    print("No se ingresó ningún teléfono.")
                    continue
                if not validar_telefono(nuevo_telefono):
                    print("El teléfono ingresado no es válido. Ejemplo: 912345678")
                    continue
                cliente.telefono = nuevo_telefono
                sesion.commit()
                print("Teléfono actualizado correctamente.")

            #Correo
            elif opcion == "5":
                nuevo_mail = input("Nuevo correo (deje vacío para eliminar): ").strip()
                if nuevo_mail:
                    if not validar_correo(nuevo_mail):
                        print("El correo ingresado no es válido. Ejemplo: ejemplo@dominio.com")
                        continue
                    cliente.mail = nuevo_mail
                else:
                    cliente.mail = None
                sesion.commit()
                print("Correo actualizado correctamente.")

            #Dirección completa
            elif opcion == "6":
                print("\n--- Modificar Dirección ---")

                # Región y comuna
                print("\nSeleccione la REGIÓN:")
                regiones = listar_regiones()
                for i, r in enumerate(regiones, start=1):
                    print(f"[{i}] {r}")

                try:
                    opcion_region = int(input("Región (número): ").strip())
                    region = regiones[opcion_region - 1]
                except (ValueError, IndexError):
                    print("Región no válida. Intente nuevamente.")
                    continue

                print(f"\nSeleccione la COMUNA de la {region}:")
                comunas = listar_comunas_por_region(region)
                for i, c in enumerate(comunas, start=1):
                    print(f"[{i}] {c}")

                try:
                    opcion_comuna = int(input("Comuna (número): ").strip())
                    comuna = obtener_comuna(region, opcion_comuna)
                except (ValueError, IndexError):
                    print("Comuna no válida. Intente nuevamente.")
                    continue

                # Calle
                while True:
                    calle = input("\nCalle: ").strip()
                    if not calle.replace(" ", "").isalpha():
                        print("La calle solo puede contener letras y espacios.")
                    elif not calle:
                        print("Debe ingresar un nombre de calle.")
                    else:
                        break

                # Departamento (opcional)
                departamento = input("Departamento (opcional, presione Enter si no aplica): ").strip()
                if departamento == "":
                    departamento = None

                # Número
                while True:
                    numero_d = input("Número de dirección: ").strip()
                    if not numero_d.isdigit():
                        print("El número de dirección solo debe contener números.")
                    else:
                        break

                # Actualizar dirección
                direccion.comuna = comuna
                direccion.calle = calle
                direccion.departamento = departamento
                direccion.numero_d = numero_d

                sesion.commit()
                print("Dirección actualizada correctamente.")

            #Volver
            elif opcion == "0":
                break

            else:
                print("Opción no válida. Intente nuevamente.")

    except Exception as e:
        sesion.rollback()
        print("Error al modificar cliente:", e)
    finally:
        sesion.close()
#def modificar_cliente()


def desactivar_cliente(id_cliente):
    """
    Marca un cliente como inactivo
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID.")
            return

        if not cliente.estado_cliente:
            print("El cliente ya se encuentra desactivado.")
            return

        cliente.estado_cliente = False
        sesion.commit()
        print(f"Cliente {cliente.nombre} {cliente.apellido} (ID {cliente.id_cliente}) desactivado correctamente.")

    except Exception as e:
        sesion.rollback()
        print("Error al desactivar cliente:", e)
    finally:
        sesion.close()
#def desactivar_cliente()


def reactivar_cliente(id_cliente):
    """
    Vuelve a activar un cliente previamente desactivado
    """
    sesion = Session()
    try:
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        if not cliente:
            print("No se encontró un cliente con ese ID.")
            return

        if cliente.estado_cliente:
            print("El cliente ya está activo.")
            return

        cliente.estado_cliente = True
        sesion.commit()
        print(f"Cliente {cliente.nombre} {cliente.apellido} (ID {cliente.id_cliente}) reactivado correctamente.")

    except Exception as e:
        sesion.rollback()
        print("Error al reactivar cliente:", e)
    finally:
        sesion.close()
#def reactivar_cliente()