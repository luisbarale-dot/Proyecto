from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Imports necesarios para la funcionalidad del menú
from src.utils.logs import success, error
from src.controllers.User_controller import UserController  # Usamos el controller

# Instancia de la clase Console para mostrar mensajes en la consola
console = Console()
# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()


# Función para manejar el inicio de sesión del usuario
def login():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]INICIO DE SESIÓN[/bold cyan]",
            border_style="cyan"
        )
    )

    username = Prompt.ask("Usuario")

    if not controller.user_existe(username):
        error("El usuario ingresado no existe. Por favor, registrese primero")
        user_noexiste = Prompt.ask(
            "¿Desea registrarse ahora?",
            choices=["s", "n"],
            default="n"
        )
        if user_noexiste == "s":
            # Llamamos a la funcion de registro
            console.print("Registro.")

        console.input("\nPresione ENTER para continuar...")
        return # Este return evita que el codigo continue, si el usuario no existe y no quiere registrarse

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:

        password = Prompt.ask("Contraseña", password=True)

        if controller.login(username, password):
            success(
                f"Inicio de sesión exitoso. "
                f"Bienvenido {controller.get_current_user().username}"
            )

            console.input("\nPresione ENTER para continuar...")

        intentos += 1

        error(
            f"Usuario o contraseña incorrectos. "
            f"Intento {intentos} de {max_intentos}."
        )

    # Llego aca porque fallo 3 veces
    cambiar = Prompt.ask(
        "¿Desea cambiar su contraseña?",
        choices=["s", "n"],
        default="n"
    )

    if cambiar == "s":
        # Aca posteriormente llamaremos a la funcion para cambiar contraseña
        console.print("Cambio de contraseña.")

    console.input("\nPresione ENTER para continuar...")