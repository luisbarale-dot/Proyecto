from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Imports necesarios para la funcionalidad del menú
from src.utils.logs import success, error
from src.controllers.User_controller import UserController  # Usamos el controller
from src.views import inicio_sesion, registro_menu  # Importamos los módulos de inicio de sesión
# Instancia de la clase Console para mostrar mensajes en la consola
console = Console()
# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()


# Función para mostrar el menú principal del sistema
def menu_home():
    # Limpia la consola antes de mostrar el menú
    console.clear()
    # Muestra un panel con el nombre del sistema y un borde de color cyan
    console.print(
        Panel("[bold cyan]SISTEMA DE ACCESO[/bold cyan]", border_style="cyan")
    )

    # Opciones del menú
    console.print("\n[1] Iniciar sesion")
    console.print("[2] Registrarte\n")
    console.print("[3] Salir\n")

    # Solicita al usuario que seleccione una opción del menú
    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

    # Condicional para determinar qué función ejecutar
    if opcion == "1":
        inicio_sesion.login()
    elif opcion == "2":
        registro_menu.registro()
    elif opcion == "3":
        console.print("\n[bold red]Saliendo del sistema...[/bold red]")
        exit()
