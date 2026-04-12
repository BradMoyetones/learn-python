# 4.  **Generador de Contraseñas Simple:**
#     Crea un script que genere una contraseña aleatoria combinando letras mayúsculas,
#     minúsculas, números y un set específico de caracteres especiales,
#     usando el módulo `random`.

import string
import random

def generator_pro(length: int = 12):
    # Combinamos todo en una sola constante. 
    # string.punctuation incluye: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # random.choices(poblacion, k=numero) devuelve una lista de k elementos
    password_list = random.choices(caracteres, k=length)
    
    return "".join(password_list)

print(generator_pro(15))