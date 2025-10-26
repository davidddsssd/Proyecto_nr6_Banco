import unicodedata

def normalizar_string(cadena: str) -> str:
    """
    Normaliza una cadena quitando tildes, espacios extra y pasando a minúsculas.
    Ejemplo:
        'José Pérez ' -> 'jose perez'
    """
    if not cadena:
        return ''
    
    # Normaliza a forma NFD para separar letras de acentos
    s_decomposed = unicodedata.normalize('NFD', cadena)
    
    # Filtra caracteres no base (como tildes)
    s_filtered = ''.join(c for c in s_decomposed if unicodedata.category(c) != 'Mn')
    return s_filtered.strip().lower()