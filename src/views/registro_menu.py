from src.controllers.Students_controller import StudentsController
from src.controllers.Professors__controller import ProfessorsController
from src.controllers.User_controller import UserController
from src.utils.logs import error, success


user_controller = UserController()
students_controller = StudentsController()
professors_controller = ProfessorsController()


def registro():
    print("\n===== REGISTRO DE USUARIO =====")
    tipo_usuario = input("Tipo de usuario (estudiante/adscriptor/tutor): ").strip().lower()
    if tipo_usuario not in ("estudiante", "adscriptor", "tutor"):
        error("Tipo de usuario inválido.")
        return

    username = input("Nombre de usuario: ").strip()
    if not username:
        error("El nombre de usuario no puede quedar vacío.")
        return
    if user_controller.user_existe(username):
        error("El usuario ya existe. Elija otro nombre de usuario.")
        return

    password = input("Contraseña: ")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    if not all((password, cedula, nombre, apellido)):
        error("Todos los datos son obligatorios.")
        return

    try:
        if tipo_usuario == "estudiante":
            especialidad = input("Especialidad: ").strip()
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            segundo_nombre = input("Segundo nombre (opcional): ").strip()
            segundo_apellido = input("Segundo apellido (opcional): ").strip()
            curso = input("Curso/materia: ").strip()
            grado = input("Año/grado que cursa: ").strip()
            genero = input("Género: ").strip()
            ciudad = input("Ciudad: ").strip()
            direccion = input("Dirección: ").strip()
            celular = input("Celular: ").strip()
            email = input("Correo electrónico: ").strip()
            centro_educativo = input("Centro educativo: ").strip()
            credencial_civica = input("Credencial cívica (opcional): ").strip()
            centro_referencia = input("Centro de referencia: ").strip()
            creado = students_controller.alta_estudiante(
                nombre, apellido, cedula, username, password,
                especialidad, fecha_nacimiento, direccion, celular,
                segundo_nombre=segundo_nombre,
                segundo_apellido=segundo_apellido,
                curso=curso,
                grado=grado,
                genero=genero,
                ciudad=ciudad,
                email=email,
                centro_educativo=centro_educativo,
                credencial_civica=credencial_civica,
                centro_referencia=centro_referencia,
            )
        elif tipo_usuario == "adscriptor":
            segundo_nombre = input("Segundo nombre (opcional): ").strip()
            segundo_apellido = input("Segundo apellido (opcional): ").strip()
            centro = input("Centro educativo donde trabaja: ").strip()
            creado = professors_controller.alta_adscriptor(
                nombre, apellido, cedula, username, password, centro,
                segundo_nombre, segundo_apellido,
            )
        else:
            segundo_nombre = input("Segundo nombre (opcional): ").strip()
            segundo_apellido = input("Segundo apellido (opcional): ").strip()
            materia = input("Materia que dicta: ").strip()
            creado = professors_controller.alta_tutor(
                nombre, apellido, cedula, username, password, materia,
                segundo_nombre, segundo_apellido,
            )
    except (OSError, ValueError):
        error("No se pudo guardar el registro. Revise los archivos JSON y vuelva a intentar.")
        return

    if creado:
        success(f"Usuario {username} registrado como {tipo_usuario}.")
    else:
        error("No se pudo completar el registro; la cédula o el usuario podrían estar duplicados.")
