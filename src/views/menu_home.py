# menu_home.py
from src.views import inicio_sesion, registro_menu, menu_estudiante, menu_admin, menu_profesor


def menu_home():
    while True:
        print("\n===== SISTEMA DE GESTION DE PRACTICAS DOCENTES Y EXTENSION =====")
        print("[1] Iniciar sesion")
        print("[2] Registrarte")
        print("[3] Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            usuario = inicio_sesion.login()
            if usuario:
                _enrutar_por_rol(usuario)
        elif opcion == "2":
            registro_menu.registro()
        elif opcion == "3":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opcion invalida.")


def _enrutar_por_rol(usuario):
    rol = usuario["rol"]
    if rol == "estudiante":
        menu_estudiante.menu(usuario)
    elif rol == "admin":
        menu_admin.menu()
    elif rol in ("adscriptor", "tutor"):
        menu_profesor.menu(usuario)
