import json
import src.utils.queue as QueueUtil

class JsonUtil:
    def __init__(self,path:str):
        self.filepath=path
        self.queue=QueueUtil.Queue()

<<<<<<< HEAD
    def read(self)->dict:
=======
    def read(self)-> dict:
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        try:
            with open(self.filepath,"r",encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("error archivo no encontrado")
            return {"Usuarios": []}
        except json.JSONDecodeError:
            print("error el archivo no es json")
            return {"Usuarios": []}
        
<<<<<<< HEAD
    def __write(self,data:dict)->None:
        if data ==None:
=======
    def __write(self,data:dict)-> None: 
        if data == None:
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            print("no se puede escribir sin datos")
            return
        with open(self.filepath, "w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

<<<<<<< HEAD
    def __aply(self)->None:
=======
    def __aply(self)-> None:
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
        data=self.read()
        if not self.queue.is_empty():
            key, value = self.queue.dequeue()
            data[key]=value
            self.__write(data)

    def add_to_json_queue(self, key:str, value):
<<<<<<< HEAD
        if key==None or value==None:
=======
        if key == None or value == None:
>>>>>>> 8dff9e8 (Correcciones de errores en controllers y autenticación: módulos de controllers)
            print("no se pueden añadir sin parametros")
            return
        self.queue.enqueue((key,value))
        self.__aply()
    