
# Imports necesarios para la funcionalidad del menú
from src.controllers.User_controller import UserController  # Usamos el controller
from src.views import inicio_sesion, registro_menu  # Importamos los módulos de inicio de sesión

# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()

# Función para mostrar el menú principal del sistema
def menu_home():
    while True:
        print("""
        =================================
          SISTEMA DE GESTIÓN DE PRÁCTICAS
        ===================================
        1. Iniciar Sesión
        2. Registrarse como Estudiante
        3. Salir""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            inicio_sesion.login() #Lleva al módulo "inicio_sesion".
        elif opcion == "2": 
            registro_menu.registro() #Lleva al módulo "registro_menu".
        elif opcion == "3":
            print("Saliendo del sistema...") #Termina el programa.
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")