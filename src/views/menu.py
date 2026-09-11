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

# Función para mostrar el menú principal del sistema
def mostrar_menu():
    # Limpia la consola antes de mostrar el menú
    console.clear()
    # Muestra un panel con el nombre del sistema y un borde de color cyan
    console.print(
        Panel("[bold cyan]SISTEMA DE ACCESO[/bold cyan]", border_style="cyan")
    )

    # Opciones del menú
    console.print("\n[1] Iniciar sesión")
    console.print("[2] Salir\n")

    # Solicita al usuario que seleccione una opción del menú
    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2"])

    # Condicional para determinar qué función ejecutar
    if opcion == "1":
        login()
    elif opcion == "2":
        console.print("[yellow]Saliendo...[/yellow]")

# Función para manejar el inicio de sesión del usuario
def login():
    # Limpia la consola antes de mostrar el panel de login
    console.clear()
    console.print(
        Panel("[bold cyan]INICIO DE SESIÓN[/bold cyan]", border_style="cyan")
    )

    # Solicita al usuario que ingrese su nombre de usuario y contraseña
    username = Prompt.ask("Usuario")
    password = Prompt.ask("Contraseña",password=True)

    # Llama al método login del UserController para verificar credenciales
    if controller.login(username, password):
        # Si el login es exitoso, muestra mensaje de éxito y el nombre del usuario actual
        success(f"Inicio de sesión exitoso. Bienvenido {controller.get_current_user().username}")
    else:
        # Si falla, muestra mensaje de error
        error("Usuario o contraseña incorrectos.")

    # Pausa para que el usuario pueda leer el resultado antes de volver al menú
    console.input("\nPresione ENTER para continuar...")
