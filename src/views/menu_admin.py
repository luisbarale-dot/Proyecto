# menu_admin.py
from src.controllers.Admin_controller import AdminController
from src.utils.logs import success, error

admin = AdminController()


def menu():
    while True:
        print("\n===== MENU ADMINISTRACION =====")
        print("[1] Gestionar Estudiantes")
        print("[2] Gestionar Profesores (Adscriptores/Tutores)")
        print("[3] Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            _menu_estudiantes()
        elif opcion == "2":
            _menu_profesores()
        elif opcion == "3":
            return
        else:
            print("Opcion invalida.")


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
