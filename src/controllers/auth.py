# importa las librerias necesarias para el funcionamiento del modulo auth, como json para manejar archivos de formato JSON y Path para manejar rutas de archivos mas facilmente
import json
from pathlib import Path
# Importa la funcion de error del modulo de logs para mostrar mensajes de error en la consola
from src.utils.logs import error
# Define la ruta del archivo usuarios.json, que contiene los datos de los usuarios del sistema
DIR = Path(__file__).resolve().parent.parent

ARCHIVO_USERS = DIR / "data" / "JSON" / "usuarios.json"
# Funcion para cargar los usuarios desde el archivo usuarios.json, devuelve una lista de diccionarios con los datos de los usuarios
def cargar_usuarios():
    try:
        with open(ARCHIVO_USERS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos["Usuarios"]
    # Manejo de errores en caso de que el archivo no exista o tenga un formato incorrecto, mostrando un mensaje de error en la consola
    except FileNotFoundError: # Error por si no encuentra el archivo
        error("No se encontró el archivo usuarios.json")
        return []

    except json.JSONDecodeError: # Error por si el archivo tiene un formato incorrecto
        error("El archivo usuarios.json tiene un formato incorrecto")
        return []

# Funcion para iniciar session, recibe el nombre de usuario y la contraseña como parametros
def iniciar_sesion(username, password):
    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if (
            usuario["user"] == username
            and usuario["pass"] == password
        ):
            return usuario

    return None