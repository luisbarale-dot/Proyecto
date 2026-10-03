# Imports necesarios para la funcionalidad del menú
from src.controllers.User_controller import UserController
from src.views.registro_menu import registro  #Usaremos la función registro.
from src.views.menu_admin import menu_admin

controller = UserController() #Utilizamos el módulo "user_controller",
                    #que instancia el objeto "Users()" para
                    #manejar login/logout y estado de sesión.

#Función para manejar el inicio de sesión del usuario (cualquiera sea su rol).
def login():
    print("""
    ==================================
               INICIAR SESION
    ==================================""")
    username = input("Usuario: ")

    if not controller.user_existe(username): #Usamos la función del módulo "UserController".
        user_no_exists = input("""El usuario ingresado no existe.
                            ¿Desea registrarse? [s/n]: """).lower() #Valida "s/n" y "S/N".
        if user_no_exists == "s":
            registro() #Llamamos a la funcion de registro del "UserController".
            return
        input("\nPresione ENTER para regresar al Menú...") #Se ejecuta cuando el usuario selecciona "n".
        return # Este return evita que el codigo continue, si el usuario no existe y no quiere registrarse.

    """Si el usuario existe, se ejecuta lo siguiente:"""
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos: #Se ejecuta con un máximo de 3 intentos.
        password = input("Contraseña: ") #Ingreso manual de contraseña.

        if controller.login(username, password): #Se comprueba user y pass correctos.
            usuario = controller.get_current_user() #Se verifica si ya inició sesión, con get del "UserController".
            print(f"""\nInicio de sesión exitoso. 
                    Bienvenido {usuario.username}""") #Se usa su nombre de usuario para el mensaje.
            if usuario.get_role() == "admin":
                menu_admin() #Si es admin, accede a ese menú.
            input("\nPresione ENTER para continuar...")
            return  #Termina el ciclo.
        else:
            intentos += 1
            print(f"""\nUsuario o contraseña incorrectos. 
              Intento {intentos} de {max_intentos}.""") #Se ejecuta nuevamente.

    #Llego aca porque fallo 3 veces.
    print("\nSe alcanzó el máximo de intentos.")
    cambiar = input("¿Desea cambiar su contraseña? [s/n]: ") #Se elije una de las opciones.
    if cambiar == "s":
        # Aca posteriormente llamaremos a la funcion para cambiar contraseña
        print("Cambio de contraseña (por realizarse).")
    else:   #Si no desea cambiarla, puede regresar al menú.
        input("\nPresione ENTER para regresar al Menú...")
        return