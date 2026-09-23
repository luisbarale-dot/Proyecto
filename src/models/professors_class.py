class Professors():
    def __init__(self, name, user_id, ci, course):
        self.name = name
        self.user_id = user_id
        self.__ci = ci
        self.__course = course