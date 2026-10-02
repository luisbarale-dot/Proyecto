

from src.controllers.Students_controller import StudentsController
from src.controllers.Professors__controller import ProfessorsController


class AdminController:
    def __init__(self):
        self.estudiantes = StudentsController()
        self.profesores = ProfessorsController()
