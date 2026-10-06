

from pathlib import Path
from src.utils.jsonUtil import JsonUtil

DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO = DIR_DATA / "Alumnos.json"
CLAVE = "Alumnos"


class EstudiantesRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO.exists():
            ARCHIVO.write_text('{"Alumnos": []}', encoding="utf-8")
        self.json_util = JsonUtil(str(ARCHIVO))

    def cargar_todos(self):
        return self.json_util.read().get(CLAVE, [])

    def guardar_todos(self, registros):
        self.json_util.add_to_json_queue(CLAVE, registros)

    def existe_cedula(self, cedula):
        return any(r.get("cedula", r.get("ci")) == cedula for r in self.cargar_todos())

    def agregar(self, registro):
        registros = self.cargar_todos()
        registros.append(registro)
        self.guardar_todos(registros)

    def actualizar(self, cedula, registro_nuevo):
        registros = self.cargar_todos()
        for i, r in enumerate(registros):
            if r.get("cedula", r.get("ci")) == cedula:
                registros[i] = registro_nuevo
                self.guardar_todos(registros)
                return True
        return False

    def eliminar(self, cedula):
        registros = [
            r for r in self.cargar_todos()
            if r.get("cedula", r.get("ci")) != cedula
        ]
        self.guardar_todos(registros)
