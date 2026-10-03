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
    user_id = controller.register(username, password, "Alumno")
    if user_id: #Registramos al usuario.
        name = input("Nombre/s y Apellido/s: ")
        ci = input("Cédula: ")
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
                "user_id": user_id,
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
        return studcon.create_student(student_data)
    else:
        print("No se pudo registrar el usuario.") #Se ejecuta si sucede algún error.
        return False