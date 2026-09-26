#Importo los controllers necesarios para el Administrador:
from src.controllers.Adscriptores_controller import Adscriptores_controller as AdsCon
from src.controllers.Professors__controller import Professor_Controller as ProfCon
from src.controllers.Students_controller import StudentController as StudCon
from src.controllers.User_controller import UserController as UserCon

class AdminController: #Se define el Admin con los métodos de los demás controllers.
    def __init__(self):
        self.__AdsCon = AdsCon()
        self.__ProfCon = ProfCon()
        self.__StudCon = StudCon()
        self.__UserCon = UserCon()

    def register_Professor(self, username, password, ci, name, course): 
        """Se solicitan atributos que brinda el módulo auth, a través del módulo User_controller."""
        user_id = self.__UserCon.register(username, password, "Profesor") #El método citado retorna el número de id nuevo.
                                         #Se solicita nombre de usuario y contraseña. El rol queda predefinido.
        if user_id: #Si el usuario se registró correctamente y se obtuvo su ID, se continúa con el registro del docente.
            professor_data = {"user_id": user_id, #Se agrega el nuevo número de usuario automático.
                          "ci": ci, #Atributos propios de la clase Profesor.
                          "name": name,
                          "course": course}
            return self.__ProfCon.register_Professor(professor_data) #Se recurre al método de registro del controller de Profesor.
        return False #Si no se pudo registrar el usuario, se interrumpe el registro del docente.
    
    def register_Adscriptor(self, username, password, ci, name, course):
        """Se solicitan atributos que brinda el módulo auth, a través del módulo User_controller."""
        user_id = self.__UserCon.register(username, password, "Adscriptor") #El método citado retorna el número de id nuevo.
                                         #Se solicita nombre de usuario y contraseña. El rol queda predefinido.
        if user_id: #Si existe su ID, se procede con el registro.
            adscriptor_data = {"user_id": user_id, #Se agrega el nuevo número de usuario automático.
                          "ci": ci,
                          "name": name,
                          "course": course}
            return self.__AdsCon.register_Adscriptor(adscriptor_data)
        return False #Si no se pudo registrar, se interrumpe el registro.
    
    def register_Student(self, username, password, name, ci, course, grade, gender, bday, city, address, phone, email, educational_center, specialization, reference_center):
        """Se solicitan atributos que brinda el módulo auth, a través del módulo User_controller."""
        user_id = self.__UserCon.register(username, password, "Alumno") #El método citado retorna el número de id nuevo.
                                         #Se solicita nombre de usuario y contraseña. El rol queda predefinido.
        if user_id: #Si hay id, se procede con el registro.
            student_data = {"user_id": user_id, #Se agrega el nuevo número de usuario automático.
                "ci": ci,
                "name": name,
                "course": course,
                "grade": grade,
                "gender": gender,
                "bday": bday,
                "city": city,
                "address": address,
                "phone": phone,
                "email": email,
                "educational_center": educational_center,
                "specialization": specialization,
                "reference_center": reference_center
                }
            return self.__StudCon.create_student(student_data)
        return False #Si no se pudo registrar, se interrumpe el registro.