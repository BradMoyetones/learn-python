import pandas as pd

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

def filtrar_con_pandas(productos: dict, presupuesto: float):
    # Convertimos el diccionario a una Serie o DataFrame
    df = pd.Series(productos)
    
    # Aplicamos un "filtro de máscara" (Boolean Indexing)
    # Esto es extremadamente rápido porque ocurre a nivel de memoria de C
    resultado = df[df <= presupuesto]
    
    # Convertimos de vuelta a diccionario para el ejemplo
    return resultado.to_dict()

print(filtrar_con_pandas(diccionario, 11))