from collections import Counter

def frecuencia_pro(cadena: str):
    # Limpiamos y le pasamos todo el string a Counter
    limpia = cadena.lower().replace(" ", "")
    return dict(Counter(limpia))

print(frecuencia_pro("Hoooolas"))