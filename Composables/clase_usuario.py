class Usuario:
    def __init__(self, nombre, apellido, cedula, especialidad):
        self.nombre = nombre -> str
        self.apellido = apellido -> str
        self.cedula = cedula -> int
        self.especialidad = especialidad -> str

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad, año):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.año = año -> int

class Adscriptor(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.__disponible = True -> bool      #Para corroborar la disponibilidad.

    def es_disponible(self):
        return self.__disponible   #Debe consultarse la disponibilidad del adscriptor

    def asistencia_practicante(self):
        pass #debe registrarse el control de asistencia del estudiante.

class Tutor(Usuario):   #Se entiende por "Tutor" el docente de didáctica.
    def __init__(self, nombre, apellido, cedula, especialidad):
        super().__init__(nombre, apellido, cedula, especialidad, anno)
        self.anno = anno -> int

    def visita_practica(self):
        pass