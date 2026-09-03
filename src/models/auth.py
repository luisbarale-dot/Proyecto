import json
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent

base_Users = DIR / "data" / "usuarios.json"

def cargar_usuarios():
    try:
        with open(base_Users, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos["Usuarios"]

    except FileNotFoundError:
        print("No se encontró el archivo usuarios.json")
        return []

    except json.JSONDecodeError:
        print("El archivo usuarios.json tiene un formato incorrecto")
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