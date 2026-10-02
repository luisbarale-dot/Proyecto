# menu_profesor.py
from src.controllers.Professors__controller import ProfessorsController
from src.utils.logs import success

profesores_controller = ProfessorsController()


def menu(usuario):
    if usuario["rol"] == "tutor":
        _menu_tutor(usuario)
    else:
        _menu_adscriptor(usuario)


def _menu_tutor(usuario):
    while True:
        print(f"\n===== MENU TUTOR ({usuario['user']}) =====")
        print("[1] Ver mis datos")
        print("[2] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            prof = profesores_controller.buscar_por_cedula(usuario["cedula"])
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
            prof = profesores_controller.buscar_por_cedula(usuario["cedula"])
            print("\n" + (prof.mostrar_info() if prof else "No se encontraron datos."))
        elif opcion == "2":
            nueva = input("¿Disponible? (s/n): ").strip().lower() == "s"
            profesores_controller.cambiar_disponibilidad_adscriptor(usuario["cedula"], nueva)
            success("Disponibilidad actualizada.")
        elif opcion == "3":
            return
        else:
            print("Opcion invalida.")
