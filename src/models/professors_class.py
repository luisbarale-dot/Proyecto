class Professors():
<<<<<<< HEAD
    def __init__(self, name, user_id, ci, course):
        self.name = name
        self.user_id = user_id
        self.__ci = ci
        self.__course = course
=======
    def __init__(self, user_id, ci, name, course):
        self.user_id = user_id
        self.__ci = ci
        self.name = name
        self.__course = course

class Adscriptores(Professors):
    def __init__(self, user_id, ci, name, course):
        super().__init__(user_id, ci, name, course)
        
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
