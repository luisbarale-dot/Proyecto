class Usuario:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, cedula, especialidad, fecha_de_nacimiento, direccion,centro_educativo_asiste, celular, anio):
        super().__init__(nombre, apellido, cedula)
        self.anio = anio
        self.especialidad = especialidad
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion
        self.centro_educativo_asiste = centro_educativo_asiste
        self.celular = celular
        
        self.asistencia = 0 #luego se usará para contar asistencia
        self.calificaciones = [] #idem (Entiendo que debería ser una lista, ya que según la consigna dice que tiene que registar el historial de las visitas y..hay que calcular promedio? para saber si cumple las que son necesarias
        self.visitas = [] #Para registrar el historial de visitas del estudiante

class Adscriptor(Usuario):

    def __init__(self, nombre, apellido, cedula):
        super().__init__(nombre, apellido, cedula)
        
        # Acá podría ir un método que registre las visitas del estudiante para saber que cumpla el mínimo de visitas necesarias

        self.__disponible = True #Para corroborar la disponibilidad.

    def esta_disponible(self):
        return self.__disponible

    def cambiar_disponibilidad(self, estado): #Cambiar el estado del prof adscriptor 
        self.__disponible = estado


class Tutor(Usuario): #Se entiende por "Tutor" el docente de didáctica.
    def __init__(self, nombre, apellido, cedula, anio, materia_que_dicta):
        super().__init__(nombre, apellido, cedula)
        self.anio = anio
        self.materia_que_dicta = materia_que_dicta


class CentroEducativo:
    def __init__(self, nombre, localidad, tipo, lista_de_adscriptores):
        self.nombre = nombre
        self.localidad = localidad
        self.tipo = tipo
        self.lista_de_adscriptores= lista_de_adscriptores
        self.grupos=[] #Lista de grupos que tiene el centro educativo con estudiantes de práctica

class Grupo:
    def __init__(self, nombre, turno):
        self.nombre=nombre
        self.turno=turno

class Visita:
    def __init__(self, estudiante, adscriptor,materia, fecha, nota, observaciones):
        self.estudiante = estudiante
        self.adscriptor = adscriptor
        self.materia = materia
        self.fecha = fecha
        self.nota = nota
        self.observaciones = observaciones

class Asignacion:
    def __init__(self, estudiante, centro_educativo, adscriptor, grupo, tutor, fecha):
        self.estudiante=estudiante
        self.centro_educativo=centro_educativo
        self.adscriptor=adscriptor
        self.grupo=grupo
        self.tutor=tutor
        self.fecha=fecha