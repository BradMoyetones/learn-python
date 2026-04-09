# 2.  **Frecuencia de Caracteres:**
# Escribe una función que reciba un string y 
# devuelva un diccionario donde las llaves sean los caracteres y 
# los valores sean la cantidad de veces que aparecen. (Ignora espacios y mayúsculas).


def frecuencia_caracteres(cadena: str) -> dict:
    # 1. Limpieza: Pasamos a minúsculas y eliminamos espacios.
    # Usamos .replace() y .lower()
    limpia = cadena.lower().replace(" ", "")
    
    frecuencia = {}

    for caracter in limpia:
        if caracter in frecuencia:
            # Si el caracter ya es una llave, sumamos 1
            frecuencia[caracter] += 1
        else:
            # Si es la primera vez que lo vemos, lo inicializamos en 1
            frecuencia[caracter] = 1
            
    return frecuencia

# Ejemplo de uso
print(frecuencia_caracteres("Hola Mundo")) 
# Resultado: {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}