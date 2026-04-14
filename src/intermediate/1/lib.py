# 1.  **Manejo de Errores y Archivos:**
#     Escribe un programa que intente leer un archivo de texto. 
#     Si el archivo no existe, debe capturar la excepción, 
#     crear el archivo con un texto por defecto y luego 
#     imprimir el contenido.

from pathlib import Path

def manejar_archivo_pro(nombre: str):
    archivo = Path(nombre)

    # Pathlib permite verificar existencia de forma directa y elegante
    if not archivo.exists():
        print(f"El archivo {nombre} no existe. Creándolo...")
        # Escribir texto directamente (abre y cierra el flujo por ti)
        archivo.write_text("Texto por defecto con Pathlib")
    
    # Leer texto directamente
    contenido = archivo.read_text()
    print(f"Contenido del archivo:\n{contenido}")

# manejar_archivo_pro("notas.txt")