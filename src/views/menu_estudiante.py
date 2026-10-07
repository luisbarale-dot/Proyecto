
from src.controllers.Students_controller import StudentsController

students_controller = StudentsController()


def menu(usuario):
    while True:
        print(f"\n===== MENU ESTUDIANTE ({usuario['user']}) =====")
        print("[1] Ver mis datos")
        print("[2] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            estudiante = students_controller.buscar_por_user_id(
                usuario.get("id", usuario.get("user_id")),
            )
            print("\n" + estudiante.mostrar_info() if estudiante else "No se encontraron datos del estudiante.")
        elif opcion == "2":
            return
        else:
            print("Opcion invalida.")
