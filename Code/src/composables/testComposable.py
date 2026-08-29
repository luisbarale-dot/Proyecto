from models.testModel import testModel
#y aca importando solo el modelo hacemos la logica basicamente hacemos una herencia del modelo
class testController(testModel):
    def __init__(self, id):
        super().__init__(id)

    def ingresarNombre(self,nombre):
        #por ejemplo aca verificamos que nombre no sea None porque en el modelo no tiene que haber logica eso va aqui en los composables
        if nombre != None:
            self.__set_nombre(nombre)
        pass