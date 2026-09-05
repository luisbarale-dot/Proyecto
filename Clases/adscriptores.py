from clase_usuario import Adscriptor

def es_disponible(self):
    return self.__disponible   #Debe consultarse la disponibilidad del adscriptor

def asistencia_practicante(self):
    pass #debe registrarse el control de asistencia del estudiante.

def habilitar(self):
    if self.__disponible == False:
        pass #solicitar_adscriptor próximamente