# Imports necesarios para la funcionalidad del menú
from src.utils.logs import success, error
from src.controllers.User_controller import UserController  # Usamos el controller

# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()

def registro():
    print("""\n======================================
                        REGISTRO DE ALUMNO           
               ======================================""")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    if controller.user_existe(username): #Comprobamos si el usuario ya existe.
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        return
    
    if controller.register(username, password): #Registramos al usuario.
        print("\nUsuario registrado correctamente.")
    else:
        print("\nNo se pudo registrar el usuario.") #Se ejecuta si sucede algún error.
        return