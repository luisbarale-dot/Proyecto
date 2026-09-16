# User_controller.py
import src.composables.User.auth as user_auth
from src.utils.logs import error
from src.models.users_class import Users  # importa tu clase Users

class UserController:
    def __init__(self):
        self.current_user = None

    def user_existe(self, username: str) -> bool:
        return user_auth.usuario_existe(username)

    def login(self, username: str, password: str) -> bool:
        usuario = user_auth.iniciar_sesion(username, password)

        if usuario:
            self.current_user = Users(
                user_id=usuario.get("id"),
                username=usuario.get("user"),
                password=usuario.get("pass"),
                role=usuario.get("rol"),
            )
            return True

        return False

    def get_current_user(self):
        return self.current_user
