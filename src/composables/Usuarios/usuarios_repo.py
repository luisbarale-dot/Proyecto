
from pathlib import Path
from src.utils.jsonUtil import JsonUtil

DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO = DIR_DATA / "Usuarios.json"
CLAVE = "Usuarios"


class UsuariosRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO.exists():
            ARCHIVO.write_text('{"Usuarios": []}', encoding="utf-8")
        self.json_util = JsonUtil(str(ARCHIVO))

    def cargar_todos(self):
        return self.json_util.read().get(CLAVE, [])

    def guardar_todos(self, usuarios):
        self.json_util.add_to_json_queue(CLAVE, usuarios)

    def existe_username(self, username):
        return any(u.get("user") == username for u in self.cargar_todos())

    def obtener_por_username(self, username):
        for u in self.cargar_todos():
            if u.get("user") == username:
                return u
        return None

    def obtener_por_id(self, user_id):
        for usuario in self.cargar_todos():
            current_id = usuario.get("id", usuario.get("user_id"))
            if current_id is not None and str(current_id) == str(user_id):
                return usuario
        return None

    def existe_cedula(self, cedula):
        return any(usuario.get("cedula") == cedula for usuario in self.cargar_todos())

    def siguiente_id(self):
        usuarios = self.cargar_todos()
        ids = []
        for usuario in usuarios:
            value = usuario.get("id", usuario.get("user_id", 0))
            try:
                ids.append(int(value))
            except (TypeError, ValueError):
                continue
        return max(ids, default=0) + 1

    def agregar(self, username, password, rol, cedula):
        usuarios = self.cargar_todos()
        nuevo = {
            "id": self.siguiente_id(),
            "user": username,
            "pass": password,
            "rol": rol,
            "cedula": cedula,
        }
        usuarios.append(nuevo)
        self.guardar_todos(usuarios)
        return nuevo

    def actualizar_password(self, username, password_nueva):
        usuarios = self.cargar_todos()
        for u in usuarios:
            if u.get("user") == username:
                u["pass"] = password_nueva
                self.guardar_todos(usuarios)
                return True
        return False

    def eliminar_por_id(self, user_id):
        if user_id is None:
            return False
        usuarios = self.cargar_todos()
        restantes = [
            usuario for usuario in usuarios
            if str(usuario.get("id", usuario.get("user_id"))) != str(user_id)
        ]
        if len(restantes) == len(usuarios):
            return False
        self.guardar_todos(restantes)
        return True
