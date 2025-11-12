import unicodedata

def normalizar_cadena(cadena: str) -> str:
    """
    Normaliza una cadena quitando tildes, espacios extra y pasando a minúsculas.
    Ejemplo:
        'José Pérez ' -> 'jose perez'
    """
    if not cadena:
        return ''
    
    # Esto es para normalizar a forma NFD y para separar letras de acentos
    s_decomposed = unicodedata.normalize('NFD', cadena)
    
    # Filtra los caracteres (como las tildes)
    s_filtered = ''.join(c for c in s_decomposed if unicodedata.category(c) != 'Mn')
    
    # Quita los espacios al inicio y final, y pasa todo a minúsculas
    return s_filtered.strip().lower()
#def normalizar_cadena()