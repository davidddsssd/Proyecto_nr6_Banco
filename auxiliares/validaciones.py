import re

def validar_telefono(telefono: str) -> bool:
    """
    Valida que el teléfono tenga exactamente 9 dígitos numéricos.
    """
    if not telefono:
        return False

    telefono = telefono.strip()
    return telefono.isdigit() and len(telefono) == 9
#def validar_telefono()

def validar_correo(correo: str) -> bool:
    """
    Valida el formato general de un correo electrónico.
    Ejemplo válido: ejemplo@dominio.com
    """
    if not correo:
        return False

    correo = correo.strip()
    patron = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(patron.match(correo))
#def validar_correo()

def formatear_nombre(nombre: str) -> str:
    """
    Convierte un nombre o apellido a formato:
    primera letra mayúscula, resto minúsculas.
    También elimina espacios extra.
    Ejemplo: 'aNA  ' -> 'Ana'
    """
    if not nombre:
        return ""

    partes = nombre.strip().split()
    partes_formateadas = [p.capitalize() for p in partes]
    return " ".join(partes_formateadas)
#def formatear_nombre()

def validar_rut_chileno(rut: str) -> bool:
    """
    Valida el formato de un RUT en nuestro país.
    Usa el paquete 'rut_chile' y controla errores de formato.
    Retorna True si el RUT es válido, False si no.
    """
    try:
        from rut_chile import rut_chile
        rut = rut.strip()
        return rut_chile.is_valid_rut(rut)
    except Exception:
        return False
#def validar_rut_chileno()