

from src.controllers.Students_controller import StudentsController
from src.controllers.Professors__controller import ProfessorsController


class AdminController:
    def __init__(self):
        self.estudiantes = StudentsController()
        self.profesores = ProfessorsController()

    def registrar_profesor(
        self, nombre, apellido, cedula, username, password, materia,
        segundo_nombre="", segundo_apellido="",
    ):
        return self.profesores.alta_tutor(
            nombre, apellido, cedula, username, password, materia,
            segundo_nombre, segundo_apellido,
        )

    def registrar_adscriptor(
        self, nombre, apellido, cedula, username, password, centro,
        segundo_nombre="", segundo_apellido="",
    ):
        return self.profesores.alta_adscriptor(
            nombre, apellido, cedula, username, password, centro,
            segundo_nombre, segundo_apellido,
        )

    def registrar_estudiante(
        self, nombre, apellido, cedula, username, password,
        especialidad, fecha_nacimiento, direccion, celular, anio="", **datos,
    ):
        return self.estudiantes.alta_estudiante(
            nombre, apellido, cedula, username, password,
            especialidad, fecha_nacimiento, direccion, celular, anio,
            **datos,
        )
