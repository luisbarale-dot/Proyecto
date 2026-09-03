from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.utils.logs import success, error
from src.models.auth import iniciar_sesion


console = Console()


def mostrar_menu():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]SISTEMA DE ACCESO[/bold cyan]",
            border_style="cyan"
        )
    )

    console.print("\n[1] Iniciar sesión")
    console.print("[2] Salir\n")

    opcion = Prompt.ask(
        "Seleccione una opción",
        choices=["1", "2"]
    )

    if opcion == "1":
        login()

    elif opcion == "2":
        console.print("[yellow]Saliendo...[/yellow]")


def login():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]INICIO DE SESIÓN[/bold cyan]",
            border_style="cyan"
        )
    )

    username = Prompt.ask("Usuario")
    password = Prompt.ask("Contraseña", password=True)

    if iniciar_sesion(username, password):
        success("Inicio de sesión exitoso.")
    else:
        error("Usuario o contraseña incorrectos.")


    console.input("\nPresione ENTER para continuar...")