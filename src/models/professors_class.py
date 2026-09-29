class Professors():
    def __init__(self, user_id, ci, name, course):
        self.user_id = user_id
        self.__ci = ci
        self.name = name
        self.__course = course

#Getters para acceder a los atributos privados:
    @property
    def ci(self):
        return self.__ci
    @property
    def course(self):
        return self.__course

class Adscriptores(Professors):
    def __init__(self, user_id, ci, name, course):
        super().__init__(user_id, ci, name, course)