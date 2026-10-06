from src.utils.logs import error
from src.views import inicio_sesion, registro_menu, menu_estudiante, menu_admin, menu_profesor


def menu_home():
    while True:
        print("\n===== GESTOR DE PRACTICAS DOCENTES =====")
        print("[1] Iniciar sesión")
        print("[2] Registrarse")
        print("[3] Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario = inicio_sesion.login()
            if usuario:
                _enrutar_por_rol(usuario)
        elif opcion == "2":
            registro_menu.registro()
        elif opcion == "3":
            print("\nSaliendo del sistema...")
            return
        else:
            print("Opción inválida.")


def _enrutar_por_rol(usuario):
    rol = str(usuario.get("rol", "")).strip().lower()
    if rol in ("estudiante", "alumno"):
        menu_estudiante.menu(usuario)
    elif rol == "admin":
        menu_admin.menu()
    elif rol in ("adscriptor", "profesor"):
        menu_profesor.menu(usuario)
    else:
        error(f"El rol '{usuario.get('rol', '')}' no tiene un menú asignado.")
