
from src.controllers.Admin_controller import AdminController
from src.utils.logs import success, error

admin = AdminController()


def menu(usuario=None):
    while True:
        print("\n===== MENU ADMINISTRACION =====")
        print("[1] Registrar Profesor")
        print("[2] Registrar Adscriptor")
        print("[3] Registrar Estudiante")
        print("[4] Gestionar Estudiantes")
        print("[5] Gestionar Profesores y Adscriptores")
        print("[6] Buscar personas")
        print("[7] Gestionar instituciones y cupos")
        print("[8] Configurar máximo de alumnos por adscriptor")
        print("[9] Gestionar seguimiento de prácticas")
        print("[10] Cerrar sesión")

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
            _buscar_personas()
        elif opcion == "7":
            _menu_instituciones()
        elif opcion == "8":
            _configurar_limite_adscriptor()
        elif opcion == "9":
            _menu_seguimiento(usuario)
        elif opcion == "10":
            return
        else:
            print("Opcion invalida.")


def _buscar_personas():
    print("\n--- Buscar personas ---")
    print("[1] Estudiante")
    print("[2] Profesor")
    print("[3] Adscriptor")
    tipo = input("Tipo de persona: ").strip()
    if tipo not in ("1", "2", "3"):
        error("Tipo de persona no válido.")
        return

    print("[1] Buscar por cédula")
    print("[2] Buscar por ID de usuario")
    criterio = input("Criterio de búsqueda: ").strip()
    if criterio not in ("1", "2"):
        error("Criterio de búsqueda no válido.")
        return
    termino = input("Cédula o ID de usuario: ").strip()
    if not termino:
        error("Ingrese un valor para realizar la búsqueda.")
        return

    controlador = admin.estudiantes if tipo == "1" else admin.profesores
    persona = (
        controlador.buscar_por_cedula(termino)
        if criterio == "1"
        else controlador.buscar_por_user_id(termino)
    )
    roles_esperados = {"1": "estudiante", "2": "profesor", "3": "adscriptor"}
    rol_persona = getattr(persona, "rol", "estudiante" if tipo == "1" else None)
    if persona and rol_persona != roles_esperados[tipo]:
        persona = None
    if persona:
        print(f"Resultado: {persona}")
    else:
        print("No se encontró ninguna persona con esos datos.")


def _registrar_profesor():
    print("\n--- Registrar profesor ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    segundo_nombre = input("Segundo nombre (opcional): ").strip()
    apellido = input("Apellido: ").strip()
    segundo_apellido = input("Segundo apellido (opcional): ").strip()
    materia = input("Materia/especialidad: ").strip()
    _ejecutar_alta(
        "profesor",
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
    instituciones = admin.practicas.instituciones_repo.cargar_todos()
    if not instituciones:
        error("Primero registre una institución y configure sus cupos.")
        return
    print("Instituciones disponibles:")
    for institucion in instituciones:
        print(f"[{institucion['id']}] {institucion['nombre']}")
    institucion_id = input("ID de la institución: ").strip()
    _ejecutar_alta(
        "adscriptor",
        lambda: admin.registrar_adscriptor(
            nombre, apellido, cedula, username, password, "",
            segundo_nombre, segundo_apellido, institucion_id,
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
        print("[2] Listar profesores")
        print("[3] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            adscriptores = admin.profesores.listar_adscriptores()
            if not adscriptores:
                print("No hay adscriptores cargados.")
            for a in adscriptores:
                print(f" - {a}")

        elif opcion == "2":
            profesores = admin.profesores.listar_profesores()
            if not profesores:
                print("No hay profesores cargados.")
            for profesor in profesores:
                print(f" - {profesor}")

        elif opcion == "3":
            return
        else:
            print("Opcion invalida.")


def _menu_instituciones():
    while True:
        print("\n--- Instituciones y cupos ---")
        print("[1] Registrar institución")
        print("[2] Cambiar cupos de una institución")
        print("[3] Listar instituciones")
        print("[4] Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la institución: ").strip()
            try:
                segundo_tercero = int(input("Cupos para segundo y tercero: ").strip())
                cuarto = int(input("Cupos para cuarto año: ").strip())
                institucion = admin.practicas.crear_institucion(nombre, segundo_tercero, cuarto)
                success(f"Institución {institucion['nombre']} registrada.")
            except ValueError as exc:
                error(str(exc))
        elif opcion == "2":
            instituciones = admin.practicas.instituciones_repo.cargar_todos()
            for institucion in instituciones:
                cupos = institucion.get("cupos", {})
                print(
                    f"[{institucion['id']}] {institucion['nombre']} | "
                    f"2.º/3.º: {cupos.get('segundo_tercero', 0)} | "
                    f"4.º: {cupos.get('cuarto', 0)}"
                )
            institucion_id = input("ID de la institución: ").strip()
            try:
                segundo_tercero = int(input("Nuevos cupos para segundo y tercero: ").strip())
                cuarto = int(input("Nuevos cupos para cuarto año: ").strip())
                ok, mensaje = admin.practicas.actualizar_cupos(
                    institucion_id, segundo_tercero, cuarto,
                )
                (success if ok else error)(mensaje)
            except ValueError as exc:
                error(str(exc))
        elif opcion == "3":
            instituciones = admin.practicas.instituciones_repo.cargar_todos()
            if not instituciones:
                print("No hay instituciones registradas.")
            for institucion in instituciones:
                cupos = institucion.get("cupos", {})
                ocupados_23 = admin.practicas.cupos_ocupados(institucion["id"], "segundo_tercero")
                ocupados_4 = admin.practicas.cupos_ocupados(institucion["id"], "cuarto")
                print(
                    f"[{institucion['id']}] {institucion['nombre']} | "
                    f"2.º/3.º: {ocupados_23}/{cupos.get('segundo_tercero', 0)} | "
                    f"4.º: {ocupados_4}/{cupos.get('cuarto', 0)}"
                )
        elif opcion == "4":
            return
        else:
            print("Opción inválida.")


def _configurar_limite_adscriptor():
    adscriptores = admin.profesores.listar_adscriptores()
    if not adscriptores:
        print("No hay adscriptores registrados.")
        return
    print("\n--- Máximo de alumnos por adscriptor ---")
    for adscriptor in adscriptores:
        perfil = admin.profesores.profesores_repo.obtener_adscriptor(adscriptor.user_id)
        institucion = perfil.get("centro_educativo", "Sin institución") if perfil else "Sin institución"
        limite = perfil.get("max_alumnos", 0) if perfil else 0
        print(f"ID {adscriptor.user_id} | {adscriptor.nombre} {adscriptor.apellido} | {institucion} | máximo: {limite}")
    user_id = input("ID de usuario del adscriptor: ").strip()
    limite = input("Nuevo máximo de alumnos: ").strip()
    if not limite.isdigit():
        error("El máximo debe ser un entero igual o mayor que cero.")
        return
    if admin.profesores.configurar_max_alumnos(user_id, int(limite)):
        success("Máximo de alumnos actualizado.")
    else:
        error("No se pudo actualizar, verifique el ID y el máximo.")


def _menu_seguimiento(usuario):
    actor_user_id = usuario.get("id", usuario.get("user_id")) if usuario else None
    if actor_user_id is None:
        error("No se pudo identificar la sesión del administrador.")
        return
    seguimientos = admin.practicas.seguimientos_administracion()
    if not seguimientos:
        print("No hay prácticas aceptadas para mostrar.")
        return
    for item in seguimientos:
        print(
            f"[{item['solicitud_id']}] {item['estudiante']} | {item['institucion']} | "
            f"{item['tipo_descripcion']} | faltas: {item['faltas']} | "
            f"nota: {item['nota_final']} | estado: {item['estado']}"
        )
    solicitud_id = input("ID de la práctica a actualizar (Enter para volver): ").strip()
    if not solicitud_id:
        return
    faltas = input("Total de faltas (Enter para mantener): ").strip()
    nota = input("Nota final de 0 a 12 (Enter para mantener): ").strip()
    ok, mensaje = admin.practicas.actualizar_seguimiento(
        actor_user_id, solicitud_id,
        faltas=faltas if faltas else None,
        nota_final=nota if nota else None,
    )
    (success if ok else error)(mensaje)
