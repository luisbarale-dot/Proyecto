from pathlib import Path

from src.utils.jsonUtil import JsonUtil


DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO = DIR_DATA / "SolicitudesPracticas.json"
CLAVE = "Solicitudes"


class PracticasRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO.exists():
            ARCHIVO.write_text('{"Solicitudes": []}', encoding="utf-8")
        self.json_util = JsonUtil(str(ARCHIVO))

    def cargar_todos(self):
        return self.json_util.read().get(CLAVE, [])

    def crear_solicitud(self, student_user_id, institucion_id, tipo_practica):
        solicitudes = self.cargar_todos()
        nuevo_id = max((int(s.get("id", 0)) for s in solicitudes), default=0) + 1
        solicitud = {
            "id": nuevo_id,
            "student_user_id": student_user_id,
            "institucion_id": institucion_id,
            "tipo_practica": tipo_practica,
            "estado": "pendiente",
            "adscriptor_user_id": None,
        }
        solicitudes.append(solicitud)
        self.json_util.add_to_json_queue(CLAVE, solicitudes)
        return solicitud

    def actualizar(self, solicitud_id, cambios):
        solicitudes = self.cargar_todos()
        for solicitud in solicitudes:
            if str(solicitud.get("id")) == str(solicitud_id):
                solicitud.update(cambios)
                self.json_util.add_to_json_queue(CLAVE, solicitudes)
                return True
        return False
