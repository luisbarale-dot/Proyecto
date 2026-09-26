
# Imports necesarios para la funcionalidad del menú
from src.utils.logs import success, error
from src.controllers.User_controller import UserController  # Usamos el controller
from src.views import inicio_sesion, registro_menu  # Importamos los módulos de inicio de sesión

# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()

# Función para mostrar el menú principal del sistema
def menu_home():
    while True:
        print("""
        \n=================================
          SISTEMA DE GESTIÓN DE PRÁCTICAS
        ===================================
        1. Iniciar Sesión
        2. Registrarse
        3. Salir""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
<<<<<<< HEAD
            inicio_sesion.login()
        elif opcion == "2":
            registro_menu.registro()
        elif opcion == "3":
            print("Saliendo del sistema...")
=======
            inicio_sesion.login() #Lleva al módulo "inicio_sesion".
        elif opcion == "2": 
            registro_menu.registro() #Lleva al módulo "registro_menu".
        elif opcion == "3":
            print("Saliendo del sistema...") #Termina el programa.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")