
from src.controllers.Professors__controller import ProfessorsController
from src.controllers.Practicas_controller import PracticasController
from src.utils.logs import success, error

profesores_controller = ProfessorsController()
practicas_controller = PracticasController()


def menu(usuario):
    if usuario.get("rol", "").lower() == "profesor":
        _menu_profesor(usuario)
    else:
        _menu_adscriptor(usuario)


def _buscar_profesor(usuario):
    user_id = usuario.get("id", usuario.get("user_id"))
    return profesores_controller.buscar_por_user_id(user_id)


def _menu_profesor(usuario):
    while True:
        print(f"\n===== MENÚ DEL PROFESOR ({usuario['user']}) =====")
        print("[1] Ver mis datos")
        print("[2] Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            prof = _buscar_profesor(usuario)
            print("\n" + (prof.mostrar_info() if prof else "No se encontraron datos."))
        elif opcion == "2":
            return
        else:
            print("Opción no válida.")


def _menu_adscriptor(usuario):
    while True:
        print(f"\n===== MENÚ DEL ADSCRIPTOR ({usuario['user']}) =====")
        print("[1] Ver mi disponibilidad")
        print("[2] Cambiar mi disponibilidad")
        print("[3] Ver solicitudes pendientes")
        print("[4] Aceptar solicitud")
        print("[5] Rechazar solicitud")
        print("[6] Actualizar seguimiento de alumnos")
        print("[7] Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            prof = _buscar_profesor(usuario)
            print("\n" + (prof.mostrar_info() if prof else "No se encontraron datos."))
        elif opcion == "2":
            prof = _buscar_profesor(usuario)
            if not prof:
                print("No se encontraron datos del adscriptor.")
                continue
            nueva = input("¿Disponible? (s/n): ").strip().lower() == "s"
            if profesores_controller.cambiar_disponibilidad_adscriptor(prof.user_id, nueva):
                success("Disponibilidad actualizada.")
            else:
                print("No se pudo actualizar la disponibilidad.")
        elif opcion == "3":
            solicitudes = practicas_controller.solicitudes_pendientes_adscriptor(
                usuario.get("id", usuario.get("user_id")),
            )
            if not solicitudes:
                print("No hay solicitudes pendientes para la institución asignada.")
            for solicitud in solicitudes:
                print(
                    f"[{solicitud['id']}] {solicitud['estudiante']} | "
                    f"{solicitud['tipo_descripcion']} | {solicitud['institucion']}"
                )
        elif opcion in ("4", "5"):
            solicitud_id = input("ID de la solicitud: ").strip()
            ok, mensaje = practicas_controller.resolver_solicitud(
                usuario.get("id", usuario.get("user_id")),
                solicitud_id,
                aceptar=opcion == "4",
            )
            (success if ok else print)(mensaje)
        elif opcion == "6":
            _actualizar_seguimiento_adscriptor(usuario)
        elif opcion == "7":
            return
        else:
            print("Opción no válida.")


def _actualizar_seguimiento_adscriptor(usuario):
    user_id = usuario.get("id", usuario.get("user_id"))
    seguimientos = practicas_controller.seguimientos_de_adscriptor(user_id)
    if not seguimientos:
        print("No hay prácticas aceptadas asignadas a este adscriptor.")
        return
    for item in seguimientos:
        print(
            f"[{item['solicitud_id']}] {item['estudiante']} | {item['institucion']} | "
            f"{item['tipo_descripcion']} | faltas: {item['faltas']} | nota: {item['nota_final']} | {item['estado']}"
        )
    solicitud_id = input("ID de la práctica a actualizar (Enter para volver): ").strip()
    if not solicitud_id:
        return
    faltas = input("Total de faltas (Enter para mantener): ").strip()
    nota = input("Nota final de 0 a 12 (Enter para mantener): ").strip()
    ok, mensaje = practicas_controller.actualizar_seguimiento(
        user_id, solicitud_id,
        faltas=faltas if faltas else None,
        nota_final=nota if nota else None,
    )
    (success if ok else error)(mensaje)
