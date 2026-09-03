import json
from pathlib import Path

from src.utils.logs import error

DIR = Path(__file__).resolve().parent.parent

ARCHIVO_USERS = DIR / "data" / "usuarios.json"

def cargar_usuarios():
    try:
        with open(ARCHIVO_USERS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos["Usuarios"]

    except FileNotFoundError:
        error("No se encontró el archivo usuarios.json")
        return []

    except json.JSONDecodeError:
        error("El archivo usuarios.json tiene un formato incorrecto")
        return []


def iniciar_sesion(username, password):
    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if (
            usuario["user"] == username
            and usuario["pass"] == password
        ):
            return usuario

    return None