# User_controller.py
import src.composables.User.auth as user_auth #Importa el módulo de autenticación.
<<<<<<< HEAD
from src.models.users_class import Users  #importa tu clase Users.
=======
from src.models.users_class import Users  #importa la clase Users.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)

class UserController:
    def __init__(self):
        self.current_user = None #Inicialmente no contiene usuarios.

    def user_existe(self, username: str) -> bool:
        return user_auth.usuario_existe(username) #Comprueba existencia del usuario.

#Función de inicio de sesión:
    def login(self, username: str, password: str) -> bool:
        usuario = user_auth.iniciar_sesion(username, password) #se verifica el usuario.
        if usuario:
            self.current_user = Users(
                user_id=usuario.get("id"),
                username=usuario.get("user"),
                password=usuario.get("pass"),
                role=usuario.get("rol"))
            return True #Si existe, retorna verdadero.
        return False #Si no existe, retorna falso.

#Función para registrar nuevos usuarios, por defecto "alumnos":
<<<<<<< HEAD
    def register(self, username: str, password: str, role: str="alumno") -> bool:
=======
    def register(self, username: str, password: str, role: str="Alumno"):
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        if self.user_existe(username):
            return False
        return user_auth.registrar_usuario(username, password, role)

    def get_current_user(self): #Comprueba el usuario que inició sesión.
        return self.current_user