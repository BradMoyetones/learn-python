# Definición del rango: el límite superior (51) es exclusivo, por eso llega a 50.
miLista = range(1, 51)
# print(list(miLista))
# print((2 % 2))
def cuadrados_en_lista(lista):
    # Inicialización de una lista vacía para almacenar resultados.
    newList = [] 
    
    # Bucle 'for in' para iterar sobre cada elemento del objeto range.
    for e in lista:
        # Operación de potencia (también se puede usar e**2).
        cuadrado = (e * e)
        
        # Uso del operador módulo para verificar divisibilidad.
        ope = cuadrado % 3
        
        # Estructura condicional: si el residuo es 0, es divisible.
        if(ope == 0):
            # Método append para agregar el elemento al final de la lista.
            newList.append(cuadrado)
            
    # Retorno de la lista poblada.
    return newList

# Llamada a la función y asignación del resultado.
newList = cuadrados_en_lista(miLista)

# Salida por consola del array final.
print(newList)