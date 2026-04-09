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

def can_costear(productos: dict, presupuesto_maximo: int):
    new_dict = dict() 
    
    # .items() desempaqueta el diccionario en tuplas (llave, valor)
    for p, v in productos.items():
        # Verificamos si el valor (precio) entra en el presupuesto
        if(v <= presupuesto_maximo):
            # Insertamos la nueva entrada en el diccionario de retorno
            new_dict[p] = v
            
    return new_dict

print(can_costear(diccionario, 11))