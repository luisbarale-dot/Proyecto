
from src.controllers.Professors__controller import ProfessorsController
from src.utils.logs import success

profesores_controller = ProfessorsController()


def menu(usuario):
    if usuario.get("rol", "").lower() in ("tutor", "profesor"):
        _menu_tutor(usuario)
    else:
        _menu_adscriptor(usuario)


def _buscar_profesor(usuario):
    cedula = usuario.get("cedula")
    if cedula:
        profesor = profesores_controller.buscar_por_cedula(cedula)
        if profesor:
            return profesor
    user_id = usuario.get("id", usuario.get("user_id"))
    return profesores_controller.buscar_por_user_id(user_id)


def _menu_tutor(usuario):
    while True:
        print(f"\n===== MENU TUTOR ({usuario['user']}) =====")
        print("[1] Ver mis datos")
        print("[2] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            prof = _buscar_profesor(usuario)
            print("\n" + (prof.mostrar_info() if prof else "No se encontraron datos."))
        elif opcion == "2":
            return
        else:
            print("Opcion invalida.")


def _menu_adscriptor(usuario):
    while True:
        print(f"\n===== MENU ADSCRIPTOR ({usuario['user']}) =====")
        print("[1] Ver mi disponibilidad")
        print("[2] Cambiar mi disponibilidad")
        print("[3] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            prof = _buscar_profesor(usuario)
            print("\n" + (prof.mostrar_info() if prof else "No se encontraron datos."))
        elif opcion == "2":
            prof = _buscar_profesor(usuario)
            if not prof:
                print("No se encontraron datos del adscriptor.")
                continue
            nueva = input("¿Disponible? (s/n): ").strip().lower() == "s"
            if profesores_controller.cambiar_disponibilidad_adscriptor(prof.cedula, nueva):
                success("Disponibilidad actualizada.")
            else:
                print("No se pudo actualizar la disponibilidad.")
        elif opcion == "3":
            return
        else:
            print("Opcion invalida.")
