# User_controller.py
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.utils.logs import error


class UserController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.current_user = None  # dict: id, user, pass, rol, cedula

    # ---------- Autenticacion ----------
    def user_existe(self, username: str) -> bool:
        try:
            return self.usuarios_repo.existe_username(username)
        except Exception:
            error("Error al leer Usuarios.json")
            return False

    def login(self, username: str, password: str) -> bool:
        try:
            usuario = self.usuarios_repo.obtener_por_username(username)
        except Exception:
            error("Error al leer Usuarios.json")
            return False

        if usuario and usuario["pass"] == password:
            self.current_user = usuario
            return True
        return False

    def registrar_usuario(self, username: str, password: str, rol: str, cedula: str):
        if self.user_existe(username):
            return None
        return self.usuarios_repo.agregar(username, password, rol, cedula)

    # ---------- Sesion ----------
    def get_current_user(self):
        return self.current_user

    def logout(self):
        self.current_user = None
