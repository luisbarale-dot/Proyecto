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

def registro():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]REGISTRO DE USUARIO[/bold cyan]",
            border_style="cyan"
        )
    )

    tipo_usuario = Prompt.ask(
        "¿Es profesor o alumno?",
        choices=["profesor", "alumno"]
    )
    username = Prompt.ask("Ingrese un nombre de usuario")
    password = Prompt.ask("Ingrese una contraseña", password=True)

    if controller.user_existe(username):
        error("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        console.input("\nPresione ENTER para continuar...")
        return

    # controller.registrar_usuario(username, password)

    success(f"Usuario {username} registrado exitosamente como {tipo_usuario}.")
    console.input("\nPresione ENTER para continuar...")