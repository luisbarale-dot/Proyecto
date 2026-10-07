from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.utils.logs import error


class UserController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.current_user = None

    def user_existe(self, username: str) -> bool:
        try:
            return self.usuarios_repo.existe_username(username)
        except (OSError, ValueError):
            error("No se pudo leer el archivo de usuarios.")
            return False

    def login(self, username: str, password: str) -> bool:
        try:
            usuario = self.usuarios_repo.obtener_por_username(username)
        except (OSError, ValueError):
            error("No se pudo leer el archivo de usuarios.")
            return False

        if usuario and usuario.get("pass") == password:
            self.current_user = {
                key: value for key, value in usuario.items() if key != "pass"
            }
            return True
        return False

    def registrar_usuario(self, username: str, password: str, rol: str, cedula: str):
        if not username or not password or self.user_existe(username):
            return None
        return self.usuarios_repo.agregar(username, password, rol, cedula)

    def get_current_user(self):
        return self.current_user

    def logout(self):
        self.current_user = None
