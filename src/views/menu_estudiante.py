
from src.controllers.Students_controller import StudentsController
from src.controllers.Practicas_controller import PracticasController
from src.utils.logs import error, success

students_controller = StudentsController()
practicas_controller = PracticasController()


def menu(usuario):
    while True:
        print(f"\n===== MENÚ DEL ESTUDIANTE ({usuario['user']}) =====")
        print("[1] Ver mis datos")
        print("[2] Gestionar mis prácticas")
        print("[3] Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            estudiante = students_controller.buscar_por_user_id(
                usuario.get("id", usuario.get("user_id")),
            )
            print("\n" + estudiante.mostrar_info() if estudiante else "No se encontraron datos del estudiante.")
        elif opcion == "2":
            _menu_practicas(usuario)
        elif opcion == "3":
            return
        else:
            print("Opción no válida.")


def _menu_practicas(usuario):
    user_id = usuario.get("id", usuario.get("user_id"))
    while True:
        print("\n--- Mis prácticas ---")
        print("[1] Inscribirme a una práctica")
        print("[2] Ver mis solicitudes")
        print("[3] Cancelar una solicitud pendiente")
        print("[4] Ver estado de mis prácticas")
        print("[5] Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            estudiante = students_controller.buscar_por_user_id(user_id)
            categoria = practicas_controller._categoria_grado(
                estudiante.get_grado() if estudiante else None,
            )
            if not categoria:
                error("El año del estudiante no corresponde a las prácticas disponibles.")
                continue
            print(f"Tipo de práctica correspondiente: {practicas_controller.TIPOS_PRACTICA[categoria]}")
            instituciones = practicas_controller.instituciones_con_cupo(categoria)
            if not instituciones:
                print("No hay instituciones con cupos disponibles para esta práctica.")
                continue
            for institucion in instituciones:
                print(f"[{institucion['id']}] {institucion['nombre']} | cupos disponibles: {institucion['disponibles']}")
            institucion_id = input("ID de la institución: ").strip()
            ok, mensaje = practicas_controller.inscribir(user_id, institucion_id, categoria)
            (success if ok else error)(mensaje)
        elif opcion == "2":
            solicitudes = practicas_controller.solicitudes_del_estudiante(user_id)
            if not solicitudes:
                print("No hay solicitudes de prácticas.")
            for solicitud in solicitudes:
                print(
                    f"[{solicitud['id']}] {solicitud['institucion']} | "
                    f"{solicitud['tipo_descripcion']} | estado: {solicitud['estado']}"
                )
        elif opcion == "3":
            solicitud_id = input("ID de la solicitud pendiente: ").strip()
            ok, mensaje = practicas_controller.cancelar_solicitud(user_id, solicitud_id)
            (success if ok else error)(mensaje)
        elif opcion == "4":
            seguimientos = practicas_controller.seguimientos_del_estudiante(user_id)
            if not seguimientos:
                print("No hay prácticas aceptadas con seguimiento.")
            for item in seguimientos:
                print(
                    f"[{item['solicitud_id']}] {item['institucion']} | {item['tipo_descripcion']} | "
                    f"faltas: {item['faltas']} | nota: {item['nota_final'] if item['nota_final'] is not None else 'Pendiente'} | "
                    f"estado: {item['estado']}"
                )
                if item.get("debe_recursar"):
                    print("  Debe recursar el año.")
        elif opcion == "5":
            return
        else:
            print("Opción no válida.")
