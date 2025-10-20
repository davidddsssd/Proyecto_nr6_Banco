#Para pedirle datos sobre el cliente
def ingresar_datos_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    rut = input("Ingrese su rut: ")
    telefono = input("Ingrese su teléfono: ")
    mail = input("Ingrese su correo mail: ")
    return nombre, apellido, rut, telefono, mail