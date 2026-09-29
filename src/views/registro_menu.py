# Imports necesarios para la funcionalidad del menú
from src.controllers.User_controller import UserController  # Usamos el controller
from src.controllers.Students_controller import StudentController as StudCon

# Instancia del controlador de usuarios, que maneja login/logout y estado de sesión
controller = UserController()
studcon = StudCon()

def registro():
    print("""\n======================================
                        REGISTRO DE ALUMNO           
               ======================================""")
    username = input("Nombre de Usuario: ")
    password = input("Contraseña: ")
    if controller.user_existe(username): #Comprobamos si el usuario ya existe.
            print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
            return
    if controller.register(username, password): #Registramos al usuario.
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
        return studcon.ceate_student(username, password, name, ci, course, grade, gender, bday, city, address, phone, email, educational_center, specialization, reference_center)

    else:
        print("\nNo se pudo registrar el usuario.") #Se ejecuta si sucede algún error.
        return