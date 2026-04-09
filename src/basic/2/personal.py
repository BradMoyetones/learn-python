# 2.  **Frecuencia de Caracteres:**
# Escribe una función que reciba un string y 
# devuelva un diccionario donde las llaves sean los caracteres y 
# los valores sean la cantidad de veces que aparecen. (Ignora espacios y mayúsculas).

# Función para contar apariciones: Recorre la cadena cada vez que se llama.
def count(caracter, cadena):
    conteo = 0
    for c in cadena:
        if(caracter == c):
            conteo += 1
    return conteo

# Función principal
def diccionario(cadena: str):
    # Inicialización usando el constructor dict()
    dicc = dict()

    for letra in cadena:
        # Aquí es donde ocurre la magia: asignas el valor a la llave.
        # Si la llave no existe, Python la crea. Si existe, la sobreescribe.
        # El problema es que llamas a 'count' en cada iteración.
        dicc[letra] = count(letra, cadena)

    return dicc

print(diccionario("hHooo olas"))