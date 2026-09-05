class Usuario:
    def __init__(self, nombre, apellido, cedula, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.especialidad = especialidad
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad, anio):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.año = anio
        self.asistencia = 0 #luego se usará para contar asistencia
        self.calificaciones = [] #idem (Entiendo que debería ser una lista, ya que según la consigna dice que tiene que registar el historial de las visitas 
class Adscriptor(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.__disponible = True    #Para corroborar la disponibilidad.
class Tutor(Usuario):   #Se entiende por "Tutor" el docente de didáctica.
    def __init__(self, nombre, apellido, cedula, especialidad, anio):
        super().__init__(nombre, apellido, cedula, especialidad)
        self.anno = anio
