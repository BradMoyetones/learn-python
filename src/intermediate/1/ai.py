# 1.  **Manejo de Errores y Archivos:**
#     Escribe un programa que intente leer un archivo de texto. 
#     Si el archivo no existe, debe capturar la excepción, 
#     crear el archivo con un texto por defecto y luego 
#     imprimir el contenido.

def gestionar_archivo(nombre: str):
    try:
        f = open(nombre, "r")
    except FileNotFoundError:
        print("No existe. Creando...")
        with open(nombre, "w") as f:
            f.write("Contenido base de Pythonic way")
        # Volvemos a intentar leer después de crear
        return gestionar_archivo(nombre)
    else:
        # Esto solo corre si el 'try' fue exitoso (el archivo existía)
        with f: # El archivo ya estaba abierto del try
            print("Contenido leído con éxito:")
            print(f.read())
    finally:
        print("Proceso finalizado.")

# gestionar_archivo("notas.txt")