class Users(): #Definimos el objeto "Users".
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.__password = password
        self.__role = role

#Getters:
    def get_role(self): #Función para devolver el rol que tiene el usuario.
        return self.__role
    @property
    def password(self):
        return self.__password