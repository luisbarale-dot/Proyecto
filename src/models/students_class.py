class Students:
    def __init__(self, user_id, ci, name, second_name=None, last_name, second_last_name,
                 course, grade, gender, bday, city, address, phone, email,
                 educational_center, civic_credential, specialization,
                 reference_center):

        # Atributos privados
        self.__user_id = user_id
        self.__ci = ci
        self.__name = name
        self.__second_name = second_name
        self.__last_name = last_name
        self.__second_last_name = second_last_name
        self.__course = course
        self.__grade = grade
        self.__gender = gender
        self.__bday = bday
        self.__city = city
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__educational_center = educational_center
        self.__civic_credential = civic_credential
        self.__specialization = specialization
        self.__reference_center = reference_center


    # GETTERS

    def get_user_id(self):
        return self.__user_id

    def get_ci(self):
        return self.__ci

    def get_name(self):
        return self.__name

    def get_second_name(self):
        return self.__second_name

    def get_last_name(self):
        return self.__last_name

    def get_second_last_name(self):
        return self.__second_last_name

    def get_course(self):
        return self.__course

    def get_grade(self):
        return self.__grade

    def get_gender(self):
        return self.__gender

    def get_bday(self):
        return self.__bday

    def get_city(self):
        return self.__city

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_educational_center(self):
        return self.__educational_center

    def get_civic_credential(self):
        return self.__civic_credential

    def get_specialization(self):
        return self.__specialization

    def get_reference_center(self):
        return self.__reference_center


    # SETTERS - Datos que puede modificar el estudiante (Tal vez verificar el criterio)

    def set_ci(self, ci):
        self.__ci = ci

    def set_name(self, name):
        self.__name = name

    def set_second_name(self, second_name):
        self.__second_name = second_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_second_last_name(self, second_last_name):
        self.__second_last_name = second_last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_bday(self, bday):
        self.__bday = bday

    def set_city(self, city):
        self.__city = city

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def set_civic_credential(self, civic_credential):
        self.__civic_credential = civic_credential

    def set_specialization(self, specialization):
        self.__specialization = specialization


    # SETTERS- Datos que deben ser modificados administrativamente (Administrativo, secreatario, DOE)

    def set_course(self, course):
        self.__course = course

    def set_grade(self, grade):
        self.__grade = grade

    def set_educational_center(self, educational_center):
        self.__educational_center = educational_center

    def set_reference_center(self, reference_center):
        self.__reference_center = reference_center
