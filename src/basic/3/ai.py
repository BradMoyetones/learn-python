# 3.  **Filtrado de Diccionarios:**
# Tienes un diccionario con nombres de productos como llaves y sus 
# precios como valores. Crea una función que reciba este diccionario 
# y un presupuesto máximo, y devuelva un nuevo diccionario solo con 
# los productos que puedes costear.

diccionario = {
    "Mantequilla": 10.85,
    "Pasta": 5,
    "Pescado": 12,
    "Arroz": 8
}

def can_costear_pythonic(productos: dict, presupuesto: float) -> dict:
    # {llave: valor para cada item si cumple la condicion} (Dictionary Comprehension)
    return {p: v for p, v in productos.items() if v <= presupuesto}

# Una sola línea, clara y directa.
print(can_costear_pythonic(diccionario, 11))