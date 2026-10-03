from src.controllers.Admin_controller import AdminController
from src.controllers.User_controller import UserController

controller = AdminController() #Instanciamos el módulo AdminController
UserCon = UserController()


def menu_admin():
    while True:
        print("""
        ==========================
                MENÚ ADMIN
        ==========================

        1. Registrar Profesor
        2. Registrar Adscriptor
        3. Registrar Alumno
        4. Cerrar sesión""")
    
        opcion = input("Seleccione una opción: ") #Se agregan los datos.
        if opcion == "1":
            print("Registrar Profesor: ")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            if UserCon.user_existe(username): #Comprobamos si el usuario ya existe.
                print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
                return
            ci = input("Cédula: ")
            name = input("Nombre/s y Apellido/s: ")
            course = input("Materia/Especialidad: ")
            professor_data = {  "ci": ci,
                                "name": name,
                                "course": course}
            return controller.register_Professor(username, password, professor_data)
                      #Se usa el método register_Professor, instanciado con los datos ingresados.
        
        elif opcion == "2":
            print("Registrar Adscriptor: ")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            if UserCon.user_existe(username): #Comprobamos si el usuario ya existe.
                print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
                return
            ci = input("Cédula: ")
            name = input("Nombre/s y Apellido/s: ")
            course = input("Materia/Especialidad: ")
            adscriptor_data = { "ci": ci,
                                "name": name,
                                "course": course}
            return controller.register_Adscriptor(username, password, adscriptor_data)
        
        elif opcion == "3":
            print("Registrar Alumno: ")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            if UserCon.user_existe(username): #Comprobamos si el usuario ya existe.
                print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
                return
            ci = input("Cédula: ")
            name = input("Nombre/s y Apellido/s: ")
            course = input("Materia: ")
            grade = input("Año/Grado en que cursa: ")
            gender = input("Género: ")
            bday = input("Fecha de Nacimiento: ")
            city = input("Ciudad: ")
            address = input("Dirección: ")
            phone = input("Teléfono/Celular: ")
            email = input("email: ")
            educational_center = input("Centro Educativo: ")
            specialization = input("Especialidad: ")
            reference_center = input("Centro de Referencia: ")
            student_data = {
                "name": name,
                "ci": ci,
                "course": course,
                "grade": grade,
                "gender": gender,
                "bday": bday,
                "city": city,
                "address": address,
                "phone": phone,
                "email": email,
                "educational_center": educational_center,
                "specialization": specialization,
                "reference_center": reference_center
                }
            return controller.register_Student(username, password, student_data)
        
        elif opcion == "4":
            print("Cerrando sesión...")
            return
        else:
            print("Incorrecto")