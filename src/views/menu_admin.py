<<<<<<< HEAD
=======
from src.controllers.Admin_controller import AdminController as AdmCon

ControlAdmin = AdmCon()

>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
def menu_admin():
    while True:
        print("""
        ==========================
                MENÚ ADMIN
        ==========================

        1. Registrar profesor
        2. Registrar alumno
        3. Cerrar sesión""")
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
<<<<<<< HEAD
            print("Registrar Profesor")
=======
            print("Registrar Profesor: ")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        elif opcion == "2":
            print("Registrar Alumno")
        elif opcion == "3":
            print("Cerrando sesión...")
            return
        else:
            print("Incorrecto")