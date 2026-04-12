# 5.  **Validación de Palíndromos:**
#     Escribe una función que determine si una frase es un 
#     palíndromo (se lee igual de atrás hacia adelante), 
#     ignorando espacios, tildes y signos de puntuación.
import unicodedata

def es_palindromo_pro(frase: str) -> bool:
    # Normalización NFD: separa la 'á' en 'a' + '´' (tilde combinada)
    frase = frase.lower()
    frase = unicodedata.normalize('NFD', frase)
    
    # Filtramos: solo dejamos caracteres que sean letras (L) y convertimos a minúsculas
    # El Regex [^a-z] elimina todo lo que NO sea una letra
    frase_limpia = "".join(c for c in frase if unicodedata.category(c) == 'Ll')
    
    return frase_limpia == frase_limpia[::-1]

print(es_palindromo_pro("¡Anita, lava la tina!")) # True