class Students():
    def __init__(self, user_id, name, ci, course, grade, gender, bday, city, address, phone, email, educational_center, registration_card, specialization, reference_center):
        self.name = name
        self.user_id = user_id
        self.__ci = ci
        self.__course = course
        self.__grade = grade
        self.__gender= gender
        self.__bday = bday
        self.__city = city
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__registration_card = registration_card
        self.__educational_center = educational_center
        self.__specialization = specialization
        self.__reference_center = reference_center
