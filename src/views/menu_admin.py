from src.controllers.Admin_controller import AdminController

controller = AdminController() #Instanciamos el módulo AdminController

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
            ci = input("Cédula: ")
            name = input("Nombre/s y Apellido/s: ")
            course = input("Materia/Especialidad: ")
            return controller.register_Professor(username, password, ci, name, course)
                      #Se usa el método register_Professor, instanciado con los datos ingresados.
        
        elif opcion == "2":
            print("Registrar Adscriptor: ")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            ci = input("Cédula: ")
            name = input("Nombre/s y Apellido/s: ")
            course = input("Materia/Especialidad: ")
            return controller.register_Adscriptor(username, password, ci, name, course)
        
        elif opcion == "3":
            print("Registrar Alumno: ")
            username = input("Usuario: ")
            password = input("Contraseña: ")
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
            return controller.register_Student(username, password, name, ci, course, grade, gender, bday, city, address, phone, email, educational_center, specialization, reference_center)
        
        elif opcion == "4":
            print("Cerrando sesión...")
            return
        else:
            print("Incorrecto")