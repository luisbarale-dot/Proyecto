from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Imports necesarios para la funcionalidad del menu, son necesarios por el sistema de modularizacion que estamos utilizando
from src.utils.logs import success, error
from src.models.auth import iniciar_sesion

# Instancia de la clase Console para mostrar mensajes en la consola
console = Console()

# Funcion para mostrar el menu principal del sistema
def mostrar_menu():
    # Limpia la consola antes de mostrar el menu
    console.clear()
    # Muestra un panel con el nombre del sistema y un borde de color cyan
    console.print(
        Panel(
            "[bold cyan]SISTEMA DE ACCESO[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("\n[1] Iniciar sesión")
    console.print("[2] Salir\n")
    # Solicita al usuario que seleccione una opcion del menu
    opcion = Prompt.ask(
        "Seleccione una opción",
        choices=["1", "2"]
    )
    # Un if basico, para determinar que funcion ejecutar dependiendo de la opcion seleccionada por el usuario
    if opcion == "1":
        login()

    elif opcion == "2":
        console.print("[yellow]Saliendo...[/yellow]")

# Funcion para manejar el inicio de sesion del usuario
def login():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]INICIO DE SESIÓN[/bold cyan]",
            border_style="cyan"
        )
    )
    # Solicita al usuario que ingrese su nombre de usuario y contraseña
    username = Prompt.ask("Usuario")
    password = Prompt.ask("Contraseña", password=True)
    # Llama a la funcion iniciar sesion del modulo auth para verificar las credenciales del usuario
    if iniciar_sesion(username, password):
        success("Inicio de sesión exitoso.")
    else:
        error("Usuario o contraseña incorrectos.")


    console.input("\nPresione ENTER para continuar...")