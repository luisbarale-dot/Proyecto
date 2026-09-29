class Students():
    def __init__(self, user_id, name, ci, course, grade, gender, bday, city, address, phone, email, educational_center, specialization, reference_center):
        self.user_id = user_id
        self.name = name
        self.__ci = ci
        self.__course = course
        self.__grade = grade
        self.__gender= gender
        self.__bday = bday
        self.__city = city
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__educational_center = educational_center
        self.__specialization = specialization
        self.__reference_center = reference_center

#Getters para acceder a atributos privados:
    @property
    def ci(self):
        return self.__ci
    @property
    def course(self):
        return self.__course
    @property
    def grade(self):
        return self.__grade
    @property
    def gender(self):
        return self.__gender
    @property
    def bday(self):
        return self.__bday
    @property
    def city(self):
        return self.__city
    @property
    def address(self):
        return self.__address
    @property
    def phone(self):
        return self.__phone
    @property
    def email(self):
        return self.__email
    @property
    def educational_center(self):
        return self.__educational_center
    @property
    def specialization(self):
        return self.__specialization
    @property
    def reference_center(self):
        return self.__reference_center