import os

base_dir = "./src/"

def ejercicio(number: int, level: str):
    directorio = os.path.join(base_dir, level, str(number))
    
    files = {
        "personal": os.path.join(directorio, "personal.py"),
        "ai": os.path.join(directorio, "ai.py"),
        "lib": os.path.join(directorio, "lib.py")
    }

    if os.path.exists(directorio):
        return f"Error: El directorio '{directorio}' ya existe."
    
    try:
        os.makedirs(directorio, exist_ok=True)
        
        for file_path in files.values():
            with open(file_path, "w") as _f:
                pass
                
        return f"Ejercicio {number} ({level}) creado exitosamente en {directorio}"
    
    except PermissionError:
        return "Error: Acceso denegado. Intenta ejecutar con sudo o revisa los permisos de ./src/"
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

print(ejercicio(3, "basic"))