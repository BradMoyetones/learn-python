# Nivel basico

# Ejercicio 1:

miLista = range(1, 51)
# print(list(miLista))
# print((2 % 2))
def cuadrados_en_lista(lista):
    newList = []
    for e in lista:
        cuadrado = (e * e)
        ope = cuadrado % 3
        if(ope == 0):
            newList.append(cuadrado)
    return newList

newList = cuadrados_en_lista(miLista)

print(newList)