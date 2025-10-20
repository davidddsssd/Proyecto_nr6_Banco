import unicodedata

def normalizar_string(cadena):
    s_decomposed = unicodedata.normalize('NDF', cadena)
    s_filtered = ''.join(
        c for c in s_decomposed 
    )