<<<<<<< HEAD
class Users():
=======
class Users(): #Definimos el objeto "Users".
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.__password = password
        self.__role = role

    def get_role(self): #Función para devolver el rol que tiene el usuario.
        return self.__role