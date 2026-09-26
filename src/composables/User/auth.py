from pathlib import Path
<<<<<<< HEAD
from src.utils.logs import error
=======
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
from src.utils.jsonUtil import JsonUtil
# Importamos nuestra utilidad

# Definimos la ruta del archivo usuarios.json
DIR = Path(__file__).resolve().parent.parent.parent
ARCHIVO_USERS = DIR / "data" / "JSON" / "Usuarios.json"

json_utils = JsonUtil(str(ARCHIVO_USERS)) #Instancia global de la utilidad.

def usuario_existe(username):
    try:
        datos = json_utils.read()
        usuarios = datos.get("Usuarios", [])
    except Exception:
<<<<<<< HEAD
        error("Error al leer usuarios.json")
=======
        print("Error al leer usuarios.json")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        return False

    return any(usuario.get("user") == username for usuario in usuarios)

def iniciar_sesion(username, password):
<<<<<<< HEAD
    #Verifica credenciales de usuario usando JsonUtils
=======
    #Verifica credenciales de usuario usando JsonUtils.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
    try:
        datos = json_utils.read()
        usuarios = datos.get("Usuarios", [])
    except Exception:
<<<<<<< HEAD
        error("Error al leer usuarios.json")
=======
        print("Error al leer usuarios.json")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        return None
    for usuario in usuarios:
        if usuario.get("user") == username and usuario.get("pass") == password:
            return usuario
    return None

def registrar_usuario(username, password, role = "alumno"): #Por defecto, es "alumno".
    try:
        datos = json_utils.read() #Variable para buscar el json.
        usuarios = datos.get("Usuarios", []) #Leo la lista de usuarios con la variable.
<<<<<<< HEAD
        nuevo_usuario = {
            "id": len(usuarios)+1, #Se genera el id de forma automática.
=======
        nuevo_id = len(usuarios) + 1 #Contador de nuevos usuarios.
        nuevo_usuario = {
            "id": nuevo_id, #Se genera el id de forma automática.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            "user": username,
            "pass": password,
            "rol": role
        }
        usuarios.append(nuevo_usuario) #Añadimos el usuario a la lista.
        json_utils.add_to_json_queue("Usuarios", usuarios) #Se guarda en el json, usando la cola.
<<<<<<< HEAD
        return True
    except Exception:
        error("Error al registrar el usuario.")
=======
        return nuevo_id #Retorno el nuevo id para usarlo en otros módulos.
    except Exception as e:
        print("Error al registrar el usuario.")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        return False