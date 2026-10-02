# registro_menu.py
from src.utils.logs import success, error
from src.controllers.User_controller import UserController
from src.controllers.Students_controller import StudentsController
from src.controllers.Professors__controller import ProfessorsController

controller = UserController()
estudiantes_controller = StudentsController()
profesores_controller = ProfessorsController()


def registro():
    print("\n===== REGISTRO DE USUARIO =====")

    tipo_usuario = ""
    while tipo_usuario not in ("estudiante", "adscriptor", "tutor"):
        tipo_usuario = input("¿Es estudiante, adscriptor o tutor?: ").strip().lower()

    username = input("Ingrese un nombre de usuario: ").strip()
    if controller.user_existe(username):
        error("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        input("\nPresione ENTER para continuar...")
        return

    password = input("Ingrese una contraseña: ").strip()
    cedula = input("Cedula: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()

    exito = False
    if tipo_usuario == "estudiante":
        especialidad = input("Especialidad: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
        direccion = input("Direccion: ").strip()
        celular = input("Celular: ").strip()
        anio = input("Año que cursa: ").strip()
        exito = estudiantes_controller.alta_estudiante(
            nombre, apellido, cedula, username, password,
            especialidad, fecha_nacimiento, direccion, celular, anio,
        )
    elif tipo_usuario == "adscriptor":
        centro = input("Centro educativo donde trabaja: ").strip()
        exito = profesores_controller.alta_adscriptor(nombre, apellido, cedula, username, password, centro)
    else:  # tutor
        materia = input("Materia que dicta: ").strip()
        exito = profesores_controller.alta_tutor(nombre, apellido, cedula, username, password, materia)

    if exito:
        success(f"Usuario {username} registrado exitosamente como {tipo_usuario}.")
    else:
        error("No se pudo completar el registro (dato duplicado).")

    input("\nPresione ENTER para continuar...")
