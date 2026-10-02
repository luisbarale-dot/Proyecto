# inicio_sesion.py
from src.utils.logs import success, error
from src.controllers.User_controller import UserController

controller = UserController()


def login():
    print("\n===== INICIO DE SESION =====")

    username = input("Usuario: ").strip()

    if not controller.user_existe(username):
        error("El usuario ingresado no existe. Por favor, registrese primero")
        input("\nPresione ENTER para continuar...")
        return None

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        password = input("Contraseña: ").strip()

        if controller.login(username, password):
            usuario = controller.get_current_user()
            success(f"Inicio de sesion exitoso. Bienvenido {usuario['user']} ({usuario['rol']})")
            input("\nPresione ENTER para continuar...")
            return usuario  # Bug corregido: se corta el flujo apenas el login es exitoso

        intentos += 1
        error(f"Usuario o contraseña incorrectos. Intento {intentos} de {max_intentos}.")

    error("Se agotaron los intentos de inicio de sesion.")
    input("\nPresione ENTER para continuar...")
    return None
