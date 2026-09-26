from pathlib import Path #Importo librería de Path.
from src.models.professors_class import Professors  #Importo la clase Profesores.
from src.utils.logs import error #Importo el método "error" desde logs.
from src.utils.jsonUtil import JsonUtil #Importo el módulo ya definido para usar json.

PROFESSOR_DIR = Path(__file__).resolve().parent.parent #Accedo al directorio de archivos json.
ARCHIVO_PROFESSOR = PROFESSOR_DIR / "data" / "JSON" / "Profesores.json" #Accedo al json de profesores.
<<<<<<< HEAD

ADSCRIPTO_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ADSCRIPTO = ADSCRIPTO_DIR / "data" / "JSON" / "Adscriptos.json" #Accedo al json de adscriptos.
=======
json_utils = JsonUtil(str(ARCHIVO_PROFESSOR))
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)

class Professor_Controller(): #Establezco un controller para habilitar nuevo docente.
    def __init__(self): 
        self.current_professor = None #Inicialmente no hay lista de docentes.

<<<<<<< HEAD
    def professor_exists(self, user_id) -> bool: #Compruebo la existencia del profesor.
        try:
            datos = JsonUtil.read()     #Accedo y leo el json.
=======
    def __professor_exists(self, user_id) -> bool: #Compruebo la existencia del profesor.
        try:
            datos = json_utils.read()     #Accedo y leo el json.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            professors = datos.get("Profesores", []) #Leo la lista. Si está vacía, se devuelve vacía.
            for professor in professors:    #Si el id coincide, retorna verdadero.
                if professor.get("user_id") == user_id:
                    return True
<<<<<<< HEAD
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
=======
            return False    #Si no coincide, retorna falso.
        except Exception as e:   #Ante cualquier otro error, 
            print(f"Error al buscar al Docente: {str(e)}")
            return False

    def register_Professor(self, professor_data: dict) -> bool: #Hay que registrar al docente.
        try:                     #Se solicita un diccionario para el registro.
            user_id = professor_data.get("user_id") #Guardo el id para analizarlo.
            #Hay que comprobar si ya está registrado.
            if self.__professor_exists(user_id):  #Analizo la variable con el id del objeto.
                print(f"El Docente con el ID {user_id} ya está registrado.")
                return False #Se interrumpe el programa y se da aviso del no registro.
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            professor = Professors( #Se instancia el objeto con los datos recibidos del diccionario.
                professor_data.get("user_id"),
                professor_data.get("ci"),
                professor_data.get("name"),
                professor_data.get("course"))
<<<<<<< HEAD
            datos = JsonUtil.read() #Leo el contenido actual del json.
            professors = datos.get("Profesores", []) #Lista actual de alumnos.
            new_professor = { #Creo un diccionario con los datos del docente.
                "Número de id": professor.user_id,
                "ci": professor.ci,
                "Primer Nombre": professor.name,
                "Materia/Curso": professor.course
            }
            professors.append(new_professor) #Añado a la lista el nuevo docente.
=======
            datos = json_utils.read() #Leo el contenido actual del json.
            professors = datos.get("Profesores", []) #Lista actual de profesores.
            new_professor = { #Creo un diccionario con los datos del docente.
                "user_id": professor.user_id,
                "ci": professor.ci,
                "name": professor.name,
                "course": professor.course
            }
            professors.append(new_professor) #Añado a la lista el nuevo docente.
            json_utils.add_to_json_queue("Profesores", professors) #Guarda en la cola de "Profesores".
            return True #Se da aviso de que el registro fue satisfactorio.
        except Exception as e:
            print(f"Error al registrar al Docente: {str(e)}") #Se emite el error producido.
            return False
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
