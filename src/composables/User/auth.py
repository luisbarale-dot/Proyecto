from pathlib import Path
from src.utils.logs import error
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
        error("Error al leer usuarios.json")
        return False

    return any(usuario.get("user") == username for usuario in usuarios)

def iniciar_sesion(username, password):
    #Verifica credenciales de usuario usando JsonUtils
    try:
        datos = json_utils.read()
        usuarios = datos.get("Usuarios", [])
    except Exception:
        error("Error al leer usuarios.json")
        return None
    for usuario in usuarios:
        if usuario.get("user") == username and usuario.get("pass") == password:
            return usuario
    return None

def registrar_usuario(username, password, role = "alumno"): #Por defecto, es "alumno".
    try:
        datos = json_utils.read() #Variable para buscar el json.
        usuarios = datos.get("Usuarios", []) #Leo la lista de usuarios con la variable.
        nuevo_usuario = {
            "id": len(usuarios)+1, #Se genera el id de forma automática.
            "user": username,
            "pass": password,
            "rol": role
        }
        usuarios.append(nuevo_usuario) #Añadimos el usuario a la lista.
        json_utils.add_to_json_queue("Usuarios", usuarios) #Se guarda en el json, usando la cola.
        return True
    except Exception:
        error("Error al registrar el usuario.")
        return False