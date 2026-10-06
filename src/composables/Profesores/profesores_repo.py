
from pathlib import Path
from src.utils.jsonUtil import JsonUtil

DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO_ADSCRIPTOS = DIR_DATA / "Adcriptos.json"
ARCHIVO_ADSCRIPTOS_LEGACY = DIR_DATA / "Adscriptores.json"
ARCHIVO_TUTORES = DIR_DATA / "Profesores.json"
CLAVE_ADSCRIPTOS = "Adscriptos"
CLAVE_TUTORES = "Profesores"


class ProfesoresRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO_ADSCRIPTOS.exists():
            ARCHIVO_ADSCRIPTOS.write_text('{"Adscriptos": []}', encoding="utf-8")
        if not ARCHIVO_TUTORES.exists():
            ARCHIVO_TUTORES.write_text('{"Profesores": []}', encoding="utf-8")
        self.json_adscriptos = JsonUtil(str(ARCHIVO_ADSCRIPTOS))
        self.json_adscriptos_legacy = (
            JsonUtil(str(ARCHIVO_ADSCRIPTOS_LEGACY))
            if ARCHIVO_ADSCRIPTOS_LEGACY.exists() else None
        )
        self.json_tutores = JsonUtil(str(ARCHIVO_TUTORES))

    def _cargar_adscriptos(self):
        registros = self.json_adscriptos.read().get(CLAVE_ADSCRIPTOS, [])
        if self.json_adscriptos_legacy:
            legacy = self.json_adscriptos_legacy.read().get("Adscriptores", [])
            registros = registros + legacy
        unicos = []
        vistos = set()
        for r in registros:
            r["tipo"] = "adscriptor"
            identidad = r.get("user_id", r.get("id"))
            if identidad is None:
                identidad = r.get("cedula", r.get("ci"))
            identidad = str(identidad)
            if identidad not in vistos:
                vistos.add(identidad)
                unicos.append(r)
        return unicos

    def _cargar_tutores(self):
        registros = self.json_tutores.read().get(CLAVE_TUTORES, [])
        for r in registros:
            r["tipo"] = "tutor"
        return registros

    def cargar_todos(self):
        return self._cargar_adscriptos() + self._cargar_tutores()

    def existe_cedula(self, cedula):
        return any(
            r.get("cedula", r.get("ci", r.get("dni"))) == cedula
            for r in self.cargar_todos()
        )

    def agregar(self, registro):
        if registro["tipo"] == "adscriptor":
            registros = self._cargar_adscriptos()
            registros.append(registro)
            self.json_adscriptos.add_to_json_queue(CLAVE_ADSCRIPTOS, registros)
        else:
            registros = self._cargar_tutores()
            registros.append(registro)
            self.json_tutores.add_to_json_queue(CLAVE_TUTORES, registros)

    def actualizar(self, cedula, registro_nuevo):
        if registro_nuevo["tipo"] == "adscriptor":
            registros = self._cargar_adscriptos()
            clave, json_util = CLAVE_ADSCRIPTOS, self.json_adscriptos
        else:
            registros = self._cargar_tutores()
            clave, json_util = CLAVE_TUTORES, self.json_tutores

        for i, r in enumerate(registros):
            if r.get("cedula", r.get("ci", r.get("dni"))) == cedula:
                registros[i] = registro_nuevo
                json_util.add_to_json_queue(clave, registros)
                return True
        return False
