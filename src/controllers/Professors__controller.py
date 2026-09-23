from pathlib import Path #Importo librería de Path.
from src.models.professors_class import Professors  #Importo la clase Profesores.
from src.utils.logs import error #Importo el método "error" desde logs.
from src.utils.jsonUtil import JsonUtil #Importo el módulo ya definido para usar json.

PROFESSOR_DIR = Path(__file__).resolve().parent.parent #Accedo al directorio de archivos json.
ARCHIVO_PROFESSOR = PROFESSOR_DIR / "data" / "JSON" / "Profesores.json" #Accedo al json de profesores.

ADSCRIPTO_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ADSCRIPTO = ADSCRIPTO_DIR / "data" / "JSON" / "Adscriptos.json" #Accedo al json de adscriptos.

class Professor_Controller(): #Establezco un controller para habilitar nuevo docente.
    def __init__(self): 
        self.current_professor = None #Inicialmente no hay lista de docentes.

    def professor_exists(self, user_id) -> bool: #Compruebo la existencia del profesor.
        try:
            datos = JsonUtil.read()     #Accedo y leo el json.
            professors = datos.get("Profesores", []) #Leo la lista. Si está vacía, se devuelve vacía.
            for professor in professors:    #Si el id coincide, retorna verdadero.
                if professor.get("user_id") == user_id:
                    return True
                return False    #Si no coincide, retorna falso.
        except Exception:   #Ante cualquier otro error, 
            error(f"Error al buscar al Docente: {str(Exception)}")
            return False

    def register_Professor(self, professor_data: dict) -> bool: #Hay que registrar al docente.
        try:                                    #Se solicita un diccionario para el registro.
            user_id = professor_data.get("user_id") #Guardo el id para analizarlo.
            #Hay que comprobar si ya está registrado.
            if self.professor_exists(user_id):  #Analizo la variable con el id del objeto.
                error(f"El Docente con el ID {user_id} ya está registrado.")
                return False
        except:
            professor = Professors( #Se instancia el objeto con los datos recibidos del diccionario.
                professor_data.get("user_id"),
                professor_data.get("ci"),
                professor_data.get("name"),
                professor_data.get("course"))
            datos = JsonUtil.read() #Leo el contenido actual del json.
            professors = datos.get("Profesores", []) #Lista actual de alumnos.
            new_professor = { #Creo un diccionario con los datos del docente.
                "Número de id": professor.user_id,
                "ci": professor.ci,
                "Primer Nombre": professor.name,
                "Materia/Curso": professor.course
            }
            professors.append(new_professor) #Añado a la lista el nuevo docente.