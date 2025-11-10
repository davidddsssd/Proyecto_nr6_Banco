import re

def validar_telefono(telefono: str) -> bool:
    """
    Valida que el teléfono tenga exactamente 9 dígitos numéricos.
    """
    if not telefono:
        return False

    telefono = telefono.strip()
    return telefono.isdigit() and len(telefono) == 9

def validar_correo(correo):
    """
    Valida el formato general de un correo electrónico.
    Ejemplo válido: ejemplo@dominio.com
    """
    if not correo:
        return False

    correo = correo.strip()
    patron = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(patron.match(correo))

def formatear_nombre(nombre):
    """
    Convierte un nombre o apellido a formato: 
    primera letra mayúscula, resto minúsculas.
    También elimina espacios extra.
    Ejemplo: 'aNA  ' -> 'Ana'
    """
    if not nombre:
        return ""

    # Divide el nombre en palabras (para nombres compuestos)
    partes = nombre.strip().split()
    partes_formateadas = [p.capitalize() for p in partes]
    return " ".join(partes_formateadas)

def validar_rut_chileno(rut):
    """
    Envuelve el validador rut_chile.is_valid_rut()
    en un try/except para evitar errores de formato.
    Retorna True si el RUT es válido, False en caso contrario.
    """
    try:
        from rut_chile import rut_chile
        rut = rut.strip()
        return rut_chile.is_valid_rut(rut)
    except Exception:
        return False