# 4.  **Generador de Contraseñas Simple:**
#     Crea un script que genere una contraseña aleatoria combinando letras mayúsculas,
#     minúsculas, números y un set específico de caracteres especiales,
#     usando el módulo `random`.

import string
import secrets # Librería diseñada para seguridad criptográfica

def secure_password_gen(length: int = 16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # secrets.choice es mucho más seguro que random.choice para tokens o passwords
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

print(secure_password_gen())