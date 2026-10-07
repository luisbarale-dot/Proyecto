from pathlib import Path

from src.utils.jsonUtil import JsonUtil


DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO = DIR_DATA / "Instituciones.json"
CLAVE = "Instituciones"


class InstitucionesRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO.exists():
            ARCHIVO.write_text('{"Instituciones": []}', encoding="utf-8")
        self.json_util = JsonUtil(str(ARCHIVO))

    def cargar_todos(self):
        return self.json_util.read().get(CLAVE, [])

    def obtener_por_id(self, institucion_id):
        for institucion in self.cargar_todos():
            if str(institucion.get("id")) == str(institucion_id):
                return institucion
        return None

    def crear(self, nombre, cupos_segundo_tercero=0, cupos_cuarto=0):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre de la institución es obligatorio")
        if any(i["nombre"].casefold() == nombre.casefold() for i in self.cargar_todos()):
            raise ValueError("Ya existe una institución con ese nombre")
        cupos = {
            "segundo_tercero": self._validar_cupos(cupos_segundo_tercero),
            "cuarto": self._validar_cupos(cupos_cuarto),
        }
        instituciones = self.cargar_todos()
        nuevo_id = max((int(i.get("id", 0)) for i in instituciones), default=0) + 1
        institucion = {"id": nuevo_id, "nombre": nombre, "cupos": cupos}
        instituciones.append(institucion)
        self.json_util.add_to_json_queue(CLAVE, instituciones)
        return institucion

    def actualizar_cupos(self, institucion_id, cupos_segundo_tercero, cupos_cuarto):
        instituciones = self.cargar_todos()
        for institucion in instituciones:
            if str(institucion.get("id")) == str(institucion_id):
                institucion["cupos"] = {
                    "segundo_tercero": self._validar_cupos(cupos_segundo_tercero),
                    "cuarto": self._validar_cupos(cupos_cuarto),
                }
                self.json_util.add_to_json_queue(CLAVE, instituciones)
                return True
        return False

    @staticmethod
    def _validar_cupos(valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError("Los cupos deben ser números enteros")
        if valor < 0:
            raise ValueError("Los cupos no pueden ser negativos")
        return valor
