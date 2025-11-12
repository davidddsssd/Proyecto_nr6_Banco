import re

def validar_telefono(telefono: str) -> bool:
    """
    Valida que el teléfono cumpla con el formato correcto
    Ejemplo válido: '912345678'
    """
    if not telefono:
        return False

    telefono = telefono.strip()

    # Permite el formato estándar (con o sin +569)
    if telefono.startswith("+569"):
        telefono = telefono[4:]
    elif telefono.startswith("569"):
        telefono = telefono[3:]

    return telefono.isdigit() and len(telefono) == 9
#def validar_telefono()

def validar_correo(correo: str) -> bool:
    """
    Valida el formato general de un correo electrónico
    Ejemplo válido: ejemplo@dominio.com
    """
    if not correo:
        return False

    correo = correo.strip()
    patron = re.compile(r'^[\w\.\+\-ñÑ]+@[\w\.\-]+\.[A-Za-z]{2,}$')
    return bool(patron.match(correo))
#def validar_correo()

def formatear_nombre(nombre: str) -> str:
    """
    Convierte un nombre o apellido a formato:
    -Primera letra mayúscula, resto minúsculas
    -También elimina espacios extra
    Ejemplo: 'aNA  ' -> 'Ana'
    """
    if not nombre:
        return ""

    # Divide el nombre en palabras (para nombres los compuestos)
    partes = nombre.strip().split()
    partes_formateadas = [p.capitalize() for p in partes]
    return " ".join(partes_formateadas)
#def formatear_nombre()

def validar_rut_chileno(rut: str) -> bool:
    """
    Se encarga de que el RUT cumpla con el formato de nuestro pais
    Retorna True si el RUT es válido, False en caso contrario
    """
    try:
        from rut_chile import rut_chile
        rut = rut.strip()
        return rut_chile.is_valid_rut(rut)
    except Exception:
        return False
#def validar_rut_chileno()