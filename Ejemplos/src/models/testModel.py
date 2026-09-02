#la idea es que los modelos tengan la menos cantidad de logia posible.. un get y un set por atributo a lo mucho
class testModel():
    def __init__(self, id):
        self.nombre
        self.id=id
        pass
    def __get_nombre(self):
            return self.nombre
    def __set_nombre(self,nombre):
            self.nombre=nombre