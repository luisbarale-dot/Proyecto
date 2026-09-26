from pathlib import Path
from src.utils.logs import error
from src.utils.jsonUtil import JsonUtil
from src.models.students_class import Students

DIR = Path(__file__).resolve().parent.parent
ARCHIVO_STUDENTS = DIR / "data" / "JSON" / "Alumnos.json"
json_utils = JsonUtil(str(ARCHIVO_STUDENTS))


class StudentController:
    def __init__(self): #Guarda el estudiante que se está utilizando actualmente.
        self.current_student = None

    def student_exists(self, user_id) -> bool: #Verificar si existe eun estudiante.
        try:
            datos = json_utils.read()
            # Obtener la lista que está dentro de "Alumnos".
            # Si no existe, utilizar una lista vacía.
            students = datos.get("Alumnos", [])
            for student in students:                
                if student.get("user_id") == user_id:
                    return True
<<<<<<< HEAD
                return False

        except Exception as e:
            error(f"Error al buscar el estudiante: {str(e)}")
=======
            return False
        except Exception as e:
            print(f"Error al buscar el estudiante: {str(e)}")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            return False

    def get_current_student(self):
            return self.current_student

    def create_student(self, student_data: dict) -> bool: #Creamos un estudiante.
        try:            
            user_id = student_data.get("user_id")
            # Antes de crearlo comprobar si ya existe.
            if self.student_exists(user_id):
<<<<<<< HEAD
                error(f"El estudiante con el ID {user_id} ya existe")
=======
                print(f"El estudiante con el ID {user_id} ya existe")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
                return False
            # Crear un objeto Students utilizando los datos recibidos en el 
            # diccionario student_data.
            student = Students(
                student_data.get("user_id"),
<<<<<<< HEAD
                student_data.get("ci"),
                student_data.get("name"),
=======
                student_data.get("name"),
                student_data.get("ci"),
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
                student_data.get("course"),
                student_data.get("grade"),
                student_data.get("gender"),
                student_data.get("bday"),
                student_data.get("city"),
                student_data.get("address"),
                student_data.get("phone"),
                student_data.get("email"),
                student_data.get("educational_center"),
<<<<<<< HEAD
                student_data.get("registration_card"),
=======
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
                student_data.get("specialization"),
                student_data.get("reference_center"))
            
            datos = json_utils.read() #Leer el contenido actual del archivo JSON.
            students = datos.get("Alumnos", []) #Obtener la lista actual de alumnos.
            # Crear un diccionario con los datos del objeto Students.
            # para poder guardarlo en el archivo JSON:
            nuevo_student = {
                "user_id": student.user_id,
<<<<<<< HEAD
                "ci": student.ci,
                "name": student.name,
=======
                "name": student.name,
                "ci": student.ci,
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
                "course": student.course,
                "grade": student.grade,
                "gender": student.gender,
                "bday": student.bday,
                "city": student.city,
                "address": student.address,
                "phone": student.phone,
                "email": student.email,
                "educational_center": student.educational_center,
<<<<<<< HEAD
                "registration_card": student.registration_card,
                "specialization": student.specialization,
                "reference_center": student.reference_center
                }
            
=======
                "specialization": student.specialization,
                "reference_center": student.reference_center
                }
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            students.append(nuevo_student) #Agrega el nuevo estudiante a la lista.
            json_utils.add_to_json_queue("Alumnos", students) #Guarda de nuevo la lista "Alumnos".
            self.current_student = student #Guarda el objeto recién creado como  estudiante actual.
            return True
        except Exception as e:
            error(f"Error al crear el estudiante: {str(e)}")
            return False

    def update_student(self, user_id, new_data: dict) -> bool: #Actualizar un estudiante.
        try:
            datos = json_utils.read() #Leer los datos actuales del JSON.
            students = datos.get("Alumnos", []) #Obtener la lista de alumnos.
            #Recorrer los estudiantes buscando el user_id que queremos modificar:
            for student in students:
                if student.get("user_id") == user_id:
                    student.update(new_data) #update permite actualizar solamente los
                                             #datos recibidos en new_data.
                    json_utils.add_to_json_queue("Alumnos", students) #Guardar de nuevo la 
                                                                      #lista modificada
                    return True
<<<<<<< HEAD
            error(f"El estudiante con el ID {user_id} no existe")
            return False
        except Exception as e:            
            error(f"Error al actualizar el estudiante: {str(e)}")
=======
            print(f"El estudiante con el ID {user_id} no existe")
            return False
        except Exception as e:            
            print(f"Error al actualizar el estudiante: {str(e)}")
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            return False

    def delete_student(self, user_id) -> bool:  # Elimina un estudiante
        try:
            datos = json_utils.read()
            students = datos.get("Alumnos", [])
            for student in students:
                if student.get("user_id") == user_id:
                    students.remove(student)  # Elimina al estudiante de la lista
                    json_utils.add_to_json_queue("Alumnos", students) # Actualiza y guarda
                                                                      # la lista en el JSON.
                    if self.current_student: #Si era el estudiante actual, lo elimina.
                        if self.current_student.user_id == user_id:
                            self.current_student = None
                    return True
<<<<<<< HEAD
            error(f"El estudiante con el ID {user_id} no existe")
            return False
        except Exception as e:
            error(f"Error al eliminar el estudiante: {str(e)}")
            return False
=======
            print(f"El estudiante con el ID {user_id} no existe")
            return False
        except Exception as e:
            print(f"Error al eliminar el estudiante: {str(e)}")
            return False
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
