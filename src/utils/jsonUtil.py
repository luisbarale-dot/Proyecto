import json
import src.utils.queue as QueueUtil

class JsonUtil:
    def __init__(self,path:str):
        self.filepath=path
        self.queue=QueueUtil.Queue()
    def read(self)->dict:
        try:
            with open(self.filepath,"r",encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("error archivo no encontrado")
            return {"Usuarios": []}
        except json.JSONDecodeError:
            print("error el archivo no es json")
            return {"Usuarios": []}
    def __write(self,data:dict)->None:
        if data ==None:
            print("no se puede escribir sin datos")
            return
        with open(self.filepath, "w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    def __aply(self)->None:
        data=self.read()
        if not self.queue.is_empty():
            key, value = self.queue.dequeue()
            data[key]=value
            self.__write(data)

    def add_to_json_queue(self, key:str, value):
        if key==None or value==None:
            print("no se pueden a;adir sin parametros")
            return
        self.queue.enqueue((key,value))
        self.__aply()
    