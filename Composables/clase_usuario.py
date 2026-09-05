class Usuario:
    def __init__(self, nombre, apellido, cedula, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.especialidad = especialidad

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad, año):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.año = año

class Adscriptor(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.__disponible = True    #Para corroborar la disponibilidad.

    def es_disponible(self):
        return self.__disponible   #Debe consultarse la disponibilidad del adscriptor

    def asistencia_practicante(self):
        pass #debe registrarse el control de asistencia del estudiante.

class Tutor(Usuario):   #Se entiende por "Tutor" el docente de didáctica.
    def __init__(self, nombre, apellido, cedula, especialidad):
        super().__init__(nombre, apellido, cedula, especialidad, anno)
        self.anno = anno 

    def visita_practica(self):
        pass