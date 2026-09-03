class User:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Estudiante(user):
    def __init__(self, nombre, apellido, calificaciones, asistencia = True):
        super().__init__(nombre, apellido)
        self.calificaciones = calificaciones
        self.asistencia = asistencia

class Tutor(user):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.registro_asistencia = True

    def Asistencia(self):
        if super().asistencia == True:
            return self.registro_asistencia
        else:
            return self.registro_asistencia = False

