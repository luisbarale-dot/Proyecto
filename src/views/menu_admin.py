def menu_admin():
    while True:
        print("""
        ==========================
                MENÚ ADMIN
        ==========================

        1. Registrar profesor
        2. Registrar alumno
        3. Cerrar sesión""")
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Registrar Profesor")
        elif opcion == "2":
            print("Registrar Alumno")
        elif opcion == "3":
            print("Cerrando sesión...")
            return
        else:
            print("Incorrecto")