
from pathlib import Path
from src.utils.jsonUtil import JsonUtil

DIR_DATA = Path(__file__).resolve().parent.parent.parent / "data" / "JSON"
ARCHIVO_ADSCRIPTOS = DIR_DATA / "Adcriptos.json"
ARCHIVO_ADSCRIPTOS_LEGACY = DIR_DATA / "Adscriptores.json"
ARCHIVO_PROFESORES = DIR_DATA / "Profesores.json"
CLAVE_ADSCRIPTOS = "Adscriptos"
CLAVE_PROFESORES = "Profesores"


class ProfesoresRepo:
    def __init__(self):
        DIR_DATA.mkdir(parents=True, exist_ok=True)
        if not ARCHIVO_ADSCRIPTOS.exists():
            ARCHIVO_ADSCRIPTOS.write_text('{"Adscriptos": []}', encoding="utf-8")
        if not ARCHIVO_PROFESORES.exists():
            ARCHIVO_PROFESORES.write_text('{"Profesores": []}', encoding="utf-8")
        self.json_adscriptos = JsonUtil(str(ARCHIVO_ADSCRIPTOS))
        self.json_adscriptos_legacy = (
            JsonUtil(str(ARCHIVO_ADSCRIPTOS_LEGACY))
            if ARCHIVO_ADSCRIPTOS_LEGACY.exists() else None
        )
        self.json_profesores = JsonUtil(str(ARCHIVO_PROFESORES))

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

    def _cargar_profesores(self):
        registros = self.json_profesores.read().get(CLAVE_PROFESORES, [])
        for r in registros:
            r["tipo"] = "profesor"
        return registros

    def cargar_todos(self):
        return self._cargar_adscriptos() + self._cargar_profesores()

    def migrar_user_ids(self, usuarios_repo):
        fuentes = [
            (self.json_adscriptos, CLAVE_ADSCRIPTOS),
            (self.json_profesores, CLAVE_PROFESORES),
        ]
        if self.json_adscriptos_legacy:
            fuentes.append((self.json_adscriptos_legacy, "Adscriptores"))

        registros_por_fuente = [
            (json_util, clave, json_util.read().get(clave, []))
            for json_util, clave in fuentes
        ]
        todos = [registro for _, _, registros in registros_por_fuente for registro in registros]
        perfiles_por_cedula = {}
        for registro in todos:
            cedula = registro.get("cedula", registro.get("ci", registro.get("dni")))
            perfiles_por_cedula[cedula] = perfiles_por_cedula.get(cedula, 0) + 1

        cuentas_vinculadas = {
            str(registro["user_id"])
            for registro in todos
            if registro.get("user_id") is not None
        }
        usuarios = usuarios_repo.cargar_todos()
        fuentes_modificadas = set()
        for indice, (_, clave, registros) in enumerate(registros_por_fuente):
            for registro in registros:
                if registro.get("user_id") is not None:
                    continue
                cedula = registro.get("cedula", registro.get("ci", registro.get("dni")))
                tipo = "adscriptor" if clave in (CLAVE_ADSCRIPTOS, "Adscriptores") else "profesor"
                roles = ("adscriptor",) if tipo == "adscriptor" else ("profesor",)
                coincidencias = [
                    usuario for usuario in usuarios
                    if usuario.get("cedula") == cedula
                    and str(usuario.get("rol", "")).lower() in roles
                ]
                if len(coincidencias) != 1 or perfiles_por_cedula.get(cedula) != 1:
                    continue
                usuario = coincidencias[0]
                user_id = usuario.get("id", usuario.get("user_id"))
                if user_id is None or str(user_id) in cuentas_vinculadas:
                    continue
                registro["user_id"] = user_id
                cuentas_vinculadas.add(str(user_id))
                fuentes_modificadas.add(indice)

        for indice, (json_util, clave, registros) in enumerate(registros_por_fuente):
            if indice in fuentes_modificadas:
                json_util.add_to_json_queue(clave, registros)
        return bool(fuentes_modificadas)

    def migrar_instituciones(self, instituciones_repo):
        instituciones = instituciones_repo.cargar_todos()
        por_nombre = {}
        for institucion in instituciones:
            clave = institucion.get("nombre", "").strip().casefold()
            por_nombre.setdefault(clave, []).append(institucion)

        fuentes = [(self.json_adscriptos, CLAVE_ADSCRIPTOS)]
        if self.json_adscriptos_legacy:
            fuentes.append((self.json_adscriptos_legacy, "Adscriptores"))
        cambios = []
        for json_util, clave in fuentes:
            registros = json_util.read().get(clave, [])
            modificado = False
            for registro in registros:
                if registro.get("institucion_id") is not None:
                    continue
                nombre = str(registro.get("centro_educativo", "")).strip().casefold()
                coincidencias = por_nombre.get(nombre, [])
                if nombre and len(coincidencias) == 1:
                    registro["institucion_id"] = coincidencias[0]["id"]
                    modificado = True
            if modificado:
                cambios.append((json_util, clave, registros))
        for json_util, clave, registros in cambios:
            json_util.add_to_json_queue(clave, registros)
        return bool(cambios)

    def existe_cedula(self, cedula):
        return any(
            r.get("cedula", r.get("ci", r.get("dni"))) == cedula
            for r in self.cargar_todos()
        )

    def obtener_adscriptor(self, user_id):
        for registro in self._cargar_adscriptos():
            if str(registro.get("user_id")) == str(user_id):
                return registro
        return None

    def actualizar_adscriptor(self, user_id, cambios):
        fuentes = [(self.json_adscriptos, CLAVE_ADSCRIPTOS)]
        if self.json_adscriptos_legacy:
            fuentes.append((self.json_adscriptos_legacy, "Adscriptores"))
        for json_util, clave in fuentes:
            registros = json_util.read().get(clave, [])
            for registro in registros:
                if str(registro.get("user_id")) == str(user_id):
                    registro.update(cambios)
                    json_util.add_to_json_queue(clave, registros)
                    return True
        return False

    def agregar(self, registro):
        user_id = registro.get("user_id")
        if user_id is None:
            raise ValueError("El perfil de profesor requiere user_id")
        if any(
            str(r.get("user_id")) == str(user_id)
            for r in self.cargar_todos()
        ):
            raise ValueError(f"Ya existe un perfil para user_id {user_id}")
        if registro["tipo"] == "adscriptor":
            registros = self._cargar_adscriptos()
            registros.append(registro)
            self.json_adscriptos.add_to_json_queue(CLAVE_ADSCRIPTOS, registros)
        else:
            registros = self._cargar_profesores()
            registros.append(registro)
            self.json_profesores.add_to_json_queue(CLAVE_PROFESORES, registros)

    def actualizar(self, cedula, registro_nuevo):
        if registro_nuevo["tipo"] == "adscriptor":
            registros = self._cargar_adscriptos()
            clave, json_util = CLAVE_ADSCRIPTOS, self.json_adscriptos
        else:
            registros = self._cargar_profesores()
            clave, json_util = CLAVE_PROFESORES, self.json_profesores

        for i, r in enumerate(registros):
            if r.get("cedula", r.get("ci", r.get("dni"))) == cedula:
                registros[i] = registro_nuevo
                json_util.add_to_json_queue(clave, registros)
                return True
        return False
