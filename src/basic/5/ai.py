# 5.  **Validación de Palíndromos:**
#     Escribe una función que determine si una frase es un 
#     palíndromo (se lee igual de atrás hacia adelante), 
#     ignorando espacios, tildes y signos de puntuación.

import string

def es_palindromo_pythonic(frase: str) -> bool:
    # 1. Creamos la tabla de traducción
    # Mapeamos tildes a normales y eliminamos puntuación/espacios
    acentos = "áéíóúü"
    sin_acentos = "aeiouu"
    
    # maketrans(de, a, eliminar)
    tabla = str.maketrans(acentos, sin_acentos, string.punctuation + " ")
    
    # 2. Limpiamos en un solo paso
    frase_limpia = frase.lower().translate(tabla)
    
    # 3. Comparamos
    return frase_limpia == frase_limpia[::-1]

print(es_palindromo_pythonic("¿Anitá lava la tina?")) # True