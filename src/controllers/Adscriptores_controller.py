from pathlib import Path #Importo librería de Path.
from src.models.professors_class import Adscriptores  #Importo la clase Adscriptores.
from src.utils.logs import error #Importo el método "error" desde logs.
from src.utils.jsonUtil import JsonUtil #Importo el módulo ya definido para usar json.

ADSCRIPTO_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ADSCRIPTOR = ADSCRIPTO_DIR / "data" / "JSON" / "Adscriptores.json" #Accedo al json de adscriptos.
json_utils = JsonUtil(str(ARCHIVO_ADSCRIPTOR))

class Adscriptores_controller():
    def __init__(self):
        self.current_adscriptor = None

    def __adscriptor_exists(self, user_id) -> bool: #Compruebo la existencia del profesor.
        try:
            datos = json_utils.read()     #Accedo y leo el json.
            adscriptores = datos.get("Adscriptores", []) #Leo la lista. Si está vacía, se devuelve vacía.
            for adscriptor in adscriptores:    #Si el id coincide, retorna verdadero.
                if adscriptor.get("user_id") == user_id:
                    return True
            return False    #Si no coincide, retorna falso.
        except Exception as e:   #Ante cualquier otro error, 
            print(f"Error al buscar al Adscriptor: {str(e)}")
            return False

    def register_Adscriptor(self, adscriptor_data: dict) -> bool: #Hay que registrar al adscriptor.
        try:                     #Se solicita un diccionario para el registro.
            user_id = adscriptor_data.get("user_id") #Guardo el id para analizarlo.
            #Hay que comprobar si ya está registrado.
            if self.__adscriptor_exists(user_id):  #Analizo la variable con el id del objeto.
                print(f"El Adscriptor con el ID {user_id} ya está registrado.")
                return False            
            adscriptor = Adscriptores( #Se instancia el objeto con los datos recibidos del diccionario.
                adscriptor_data.get("user_id"),
                adscriptor_data.get("ci"),
                adscriptor_data.get("name"),
                adscriptor_data.get("course"))
            datos = json_utils.read() #Leo el contenido actual del json.
            adscriptores = datos.get("Adscriptores", []) #Lista actual de adscriptores.
            new_adscriptor = { #Creo un diccionario con los datos del adscriptor.
                "user_id": adscriptor.user_id,
                "ci": adscriptor.ci,
                "name": adscriptor.name,
                "course": adscriptor.course
            }
            adscriptores.append(new_adscriptor) #Añado a la lista el nuevo adscriptor.
            json_utils.add_to_json_queue("Adscriptores", adscriptores) #Guarda en la cola "Adscriptores".
            return True #Aviso de que funcionó el registro.
        except Exception as e:
            print(f"No se pudo registrar al Adscriptor: {str(e)}")
            return False #Ante cualquier otro error, se emite este mensaje.