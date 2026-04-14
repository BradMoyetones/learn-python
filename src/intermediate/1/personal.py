# 1.  **Manejo de Errores y Archivos:**
#     Escribe un programa que intente leer un archivo de texto. 
#     Si el archivo no existe, debe capturar la excepción, 
#     crear el archivo con un texto por defecto y luego 
#     imprimir el contenido.

# Bloque try para intentar la operación principal
try:
    # 'with' garantiza el cierre del archivo automáticamente al salir del bloque
    with open("notas.txt", "r") as filetext:
        print(filetext.read())
except FileNotFoundError:
    # Captura específica de error cuando el archivo no existe en la ruta
    print("Archivo no encontrado.")
    print("Creando archivo con texto por defecto...")
    
    # Abrimos en modo 'w' (write), que crea el archivo si no existe
    with open("notas.txt", "w") as filetext:
        filetext.write("Hola mundo...")

    # Re-abrimos en modo lectura para mostrar el contenido recién creado
    with open("notas.txt", "r") as filetext:
        print(filetext.read())
except Exception as e:
    # Captura genérica. Es buena práctica asignar el error a una variable 'e'
    # para saber exactamente qué falló si no es un FileNotFoundError.
    print(f"Ocurrio un error inesperado: {e}")