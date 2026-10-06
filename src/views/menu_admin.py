
from src.controllers.Admin_controller import AdminController
from src.utils.logs import success, error

admin = AdminController()


def menu():
    while True:
        print("\n===== MENU ADMINISTRACION =====")
        print("[1] Registrar Profesor/Tutor")
        print("[2] Registrar Adscriptor")
        print("[3] Registrar Estudiante")
        print("[4] Gestionar Estudiantes")
        print("[5] Gestionar Profesores (Adscriptores/Tutores)")
        print("[6] Cerrar sesión")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            _registrar_profesor()
        elif opcion == "2":
            _registrar_adscriptor()
        elif opcion == "3":
            _registrar_estudiante()
        elif opcion == "4":
            _menu_estudiantes()
        elif opcion == "5":
            _menu_profesores()
        elif opcion == "6":
            return
        else:
            print("Opcion invalida.")


def _registrar_profesor():
    print("\n--- Registrar profesor/tutor ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    segundo_nombre = input("Segundo nombre (opcional): ").strip()
    apellido = input("Apellido: ").strip()
    segundo_apellido = input("Segundo apellido (opcional): ").strip()
    materia = input("Materia/especialidad: ").strip()
    _ejecutar_alta(
        "profesor/tutor",
        lambda: admin.registrar_profesor(
            nombre, apellido, cedula, username, password, materia,
            segundo_nombre, segundo_apellido,
        ),
    )


def _registrar_adscriptor():
    print("\n--- Registrar adscriptor ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    segundo_nombre = input("Segundo nombre (opcional): ").strip()
    apellido = input("Apellido: ").strip()
    segundo_apellido = input("Segundo apellido (opcional): ").strip()
    centro = input("Centro educativo: ").strip()
    _ejecutar_alta(
        "adscriptor",
        lambda: admin.registrar_adscriptor(
            nombre, apellido, cedula, username, password, centro,
            segundo_nombre, segundo_apellido,
        ),
    )


def _registrar_estudiante():
    print("\n--- Registrar estudiante ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    segundo_nombre = input("Segundo nombre (opcional): ").strip()
    apellido = input("Apellido: ").strip()
    segundo_apellido = input("Segundo apellido (opcional): ").strip()
    curso = input("Curso/materia: ").strip()
    grado = input("Año/grado que cursa: ").strip()
    genero = input("Género: ").strip()
    especialidad = input("Especialidad: ").strip()
    fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
    ciudad = input("Ciudad: ").strip()
    direccion = input("Dirección: ").strip()
    celular = input("Teléfono/celular: ").strip()
    email = input("Correo electrónico: ").strip()
    centro_educativo = input("Centro educativo: ").strip()
    credencial_civica = input("Credencial cívica (opcional): ").strip()
    centro_referencia = input("Centro de referencia: ").strip()
    _ejecutar_alta(
        "estudiante",
        lambda: admin.registrar_estudiante(
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
        ),
    )


def _ejecutar_alta(tipo, accion):
    try:
        if accion():
            success(f"Registro de {tipo} completado.")
        else:
            error(f"No se pudo registrar el {tipo}; revise usuarios y cédulas duplicados.")
    except (OSError, ValueError):
        error(f"No se pudo guardar el registro de {tipo}. Revise los archivos JSON.")


def _menu_estudiantes():
    while True:
        print("\n--- Estudiantes ---")
        print("[1] Listar estudiantes")
        print("[2] Cambiar estado (Habilitado/Suspenso)")
        print("[3] Dar de baja estudiante del sistema")
        print("[4] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            estudiantes = admin.estudiantes.listar_estudiantes()
            if not estudiantes:
                print("No hay estudiantes cargados.")
            for est in estudiantes:
                print(f" - {est}")

        elif opcion == "2":
            cedula = input("Cedula: ").strip()
            nuevo_estado = input("Nuevo estado (Habilitado/Suspenso): ").strip()
            if admin.estudiantes.cambiar_estado(cedula, nuevo_estado):
                success("Estado actualizado.")
            else:
                error("No se pudo actualizar (cedula o estado invalido).")

        elif opcion == "3":
            cedula = input("Cedula: ").strip()
            success("Estudiante eliminado.") if admin.estudiantes.baja_estudiante(cedula) else error("No existe.")

        elif opcion == "4":
            return
        else:
            print("Opcion invalida.")


def _menu_profesores():
    while True:
        print("\n--- Profesores ---")
        print("[1] Listar adscriptores")
        print("[2] Listar tutores")
        print("[3] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            adscriptores = admin.profesores.listar_adscriptores()
            if not adscriptores:
                print("No hay adscriptores cargados.")
            for a in adscriptores:
                print(f" - {a}")

        elif opcion == "2":
            tutores = admin.profesores.listar_tutores()
            if not tutores:
                print("No hay tutores cargados.")
            for t in tutores:
                print(f" - {t}")

        elif opcion == "3":
            return
        else:
            print("Opcion invalida.")
