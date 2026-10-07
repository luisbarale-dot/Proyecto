from pathlib import Path

from src.utils.jsonUtil import JsonUtil


DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO = DIR_DATA / "SeguimientoPracticas.json"
CLAVE = "Seguimientos"


class SeguimientoRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO.exists():
            ARCHIVO.write_text('{"Seguimientos": []}', encoding="utf-8")
        self.json_util = JsonUtil(str(ARCHIVO))

    def cargar_todos(self):
        return self.json_util.read().get(CLAVE, [])

    def obtener_por_solicitud(self, solicitud_id):
        for seguimiento in self.cargar_todos():
            if str(seguimiento.get("solicitud_id")) == str(solicitud_id):
                return seguimiento
        return None

    def crear_si_no_existe(self, solicitud):
        existente = self.obtener_por_solicitud(solicitud["id"])
        if existente:
            return existente
        seguimiento = {
            "solicitud_id": solicitud["id"],
            "student_user_id": solicitud["student_user_id"],
            "faltas": 0,
            "nota_final": None,
            "estado": "En curso",
            "debe_recursar": False,
        }
        seguimientos = self.cargar_todos()
        seguimientos.append(seguimiento)
        self.json_util.add_to_json_queue(CLAVE, seguimientos)
        return seguimiento

    def actualizar(self, solicitud_id, cambios):
        seguimientos = self.cargar_todos()
        for seguimiento in seguimientos:
            if str(seguimiento.get("solicitud_id")) == str(solicitud_id):
                seguimiento.update(cambios)
                self.json_util.add_to_json_queue(CLAVE, seguimientos)
                return True
        return False
