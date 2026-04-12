# 4.  **Generador de Contraseñas Simple:**
#     Crea un script que genere una contraseña aleatoria combinando letras mayúsculas,
#     minúsculas, números y un set específico de caracteres especiales,
#     usando el módulo `random`.

import string
import random

def simple_password_generator(length: int = 8):
    # Definimos los sets de caracteres usando la librería 'string'
    lettersU = string.ascii_uppercase
    lettersL = string.ascii_lowercase
    digits = string.digits
    
    # Concatenamos todos los posibles caracteres en una sola cadena
    shuffles = lettersU + lettersL + digits
    
    # ''.join() toma un iterable y une sus elementos con el separador indicado (en este caso nada)
    # El generador interno ejecuta 'random.choice' la cantidad de veces que diga 'length'
    return ''.join(random.choice(shuffles) for n in range(length))

print(simple_password_generator(10))