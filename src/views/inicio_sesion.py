from src.controllers.User_controller import UserController
from src.utils.logs import error, success


controller = UserController()


def login():
    print("\n===== INICIO DE SESIÓN =====")
    username = input("Usuario: ").strip()

    if not controller.user_existe(username):
        error("El usuario ingresado no existe o no se pudo leer el archivo de usuarios.")
        input("Presione ENTER para continuar...")
        return None

    for intento in range(1, 4):
        password = input("Contraseña: ")
        if controller.login(username, password):
            usuario = controller.get_current_user()
            success(f"Inicio de sesión exitoso. Bienvenido {usuario.get('user', username)}.")
            input("Presione ENTER para continuar...")
            return usuario
        error(f"Usuario o contraseña incorrectos. Intento {intento} de 3.")

    input("Se agotaron los intentos. Presione ENTER para continuar...")
    return None
