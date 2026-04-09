# Usamos List Comprehension para crear la lista en un solo paso.
# Estructura: [expresión_resultado for elemento in iterable if condición]
solucion_pythonica = [n**2 for n in range(1, 51) if n % 3 == 0]

# Explicación:
# 1. 'for n in range(1, 51)': Itera del 1 al 50.
# 2. 'if n % 3 == 0': Filtra solo los números que son múltiplos de 3 (3, 6, 9...).
# 3. 'n**2': Eleva al cuadrado solo los números que pasaron el filtro.

print(solucion_pythonica)