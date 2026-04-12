# 5.  **Validación de Palíndromos:**
#     Escribe una función que determine si una frase es un 
#     palíndromo (se lee igual de atrás hacia adelante), 
#     ignorando espacios, tildes y signos de puntuación.
import string

def palindromes_detect(frase: str = ""):
    # Definición de tu "mapa" de limpieza
    replacements = (
        (" ", ""), ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
    )
    
    # Conviertes a lista para poder mutarla (añadir la puntuación)
    temp_list = list(replacements)

    # Añades dinámicamente cada signo de puntuación al mapa de limpieza
    for char in string.punctuation:
        temp_list.append((char, ""))

    replacements = tuple(temp_list)

    # LIMPIEZA: Aplicas cada reemplazo uno por uno
    # Ojo: Mueves el .lower() fuera del bucle para ganar eficiencia
    frase = frase.lower() 
    for c, v in replacements:
        frase = frase.replace(c, v)

    # Lógica central: Slicing invertido para comparar
    return frase[::-1] == frase

print(palindromes_detect("Anitá lava la tina")) # True