from pathlib import Path
from src.utils.logs import error
from src.utils.jsonUtil import JsonUtil
# Importamos nuestra utilidad

# Definimos la ruta del archivo usuarios.json
DIR = Path(__file__).resolve().parent.parent.parent
ARCHIVO_USERS = DIR / "data" / "JSON" / "Usuarios.json"
print(ARCHIVO_USERS)       # ruta completa
print(ARCHIVO_USERS.exists())  # debe dar True
# Instancia global de la utilidad
json_utils = JsonUtil(str(ARCHIVO_USERS))

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