

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

    def migrar_user_ids(self, usuarios_repo):
        registros = self.cargar_todos()
        usuarios = usuarios_repo.cargar_todos()
        perfiles_por_cedula = {}
        for registro in registros:
            cedula = registro.get("cedula", registro.get("ci"))
            perfiles_por_cedula[cedula] = perfiles_por_cedula.get(cedula, 0) + 1

        cuentas_vinculadas = {
            str(registro["user_id"])
            for registro in registros
            if registro.get("user_id") is not None
        }
        cambios = False
        for registro in registros:
            if registro.get("user_id") is not None:
                continue
            cedula = registro.get("cedula", registro.get("ci"))
            coincidencias = [
                usuario for usuario in usuarios
                if usuario.get("cedula") == cedula
                and str(usuario.get("rol", "")).lower() in ("estudiante", "alumno")
            ]
            if len(coincidencias) != 1 or perfiles_por_cedula.get(cedula) != 1:
                continue
            usuario = coincidencias[0]
            user_id = usuario.get("id", usuario.get("user_id"))
            if user_id is None or str(user_id) in cuentas_vinculadas:
                continue
            registro["user_id"] = user_id
            cuentas_vinculadas.add(str(user_id))
            cambios = True

        if cambios:
            self.guardar_todos(registros)
        return cambios

    def guardar_todos(self, registros):
        self.json_util.add_to_json_queue(CLAVE, registros)

    def existe_cedula(self, cedula):
        return any(r.get("cedula", r.get("ci")) == cedula for r in self.cargar_todos())

    def agregar(self, registro):
        user_id = registro.get("user_id")
        if user_id is None:
            raise ValueError("El perfil de estudiante requiere user_id")
        if any(str(r.get("user_id")) == str(user_id) for r in self.cargar_todos()):
            raise ValueError(f"Ya existe un perfil para user_id {user_id}")
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
