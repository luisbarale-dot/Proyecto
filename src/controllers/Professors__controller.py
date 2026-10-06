

from src.models.usuario_class import Adscriptor, Tutor
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.composables.Profesores.profesores_repo import ProfesoresRepo
from src.utils.logs import info, error


class ProfessorsController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.profesores_repo = ProfesoresRepo()

    def _armar_profesor(self, datos_usuario, datos_prof):
        cedula = datos_prof.get("cedula", datos_prof.get("ci", datos_prof.get("dni", "")))
        nombre = datos_prof.get("nombre", datos_prof.get("name", ""))
        apellido = datos_prof.get("apellido", datos_prof.get("last_name", ""))
        segundo_nombre = datos_prof.get("segundo_nombre", datos_prof.get("second_name", ""))
        segundo_apellido = datos_prof.get(
            "segundo_apellido", datos_prof.get("second_last_name", ""),
        )
        user_id = datos_usuario.get("id", datos_usuario.get("user_id"))
        if datos_prof["tipo"] == "adscriptor":
            prof = Adscriptor(
                user_id=user_id, nombre=nombre,
                apellido=apellido, cedula=cedula,
                username=datos_usuario["user"], password=datos_usuario["pass"],
                centro_educativo=datos_prof.get("centro_educativo"),
                segundo_nombre=segundo_nombre,
                segundo_apellido=segundo_apellido,
            )
            prof.cambiar_disponibilidad(bool(datos_prof.get("disponible", True)))
            return prof
        else:
            return Tutor(
                user_id=user_id, nombre=nombre,
                apellido=apellido, cedula=cedula,
                username=datos_usuario["user"], password=datos_usuario["pass"],
                materia=datos_prof.get("materia", datos_prof.get("course", "")),
                segundo_nombre=segundo_nombre,
                segundo_apellido=segundo_apellido,
            )

    def listar(self, tipo=None):
        resultado = []
        for datos_prof in self.profesores_repo.cargar_todos():
            if tipo and datos_prof["tipo"] != tipo:
                continue
            cedula = datos_prof.get("cedula", datos_prof.get("ci", datos_prof.get("dni")))
            datos_user = (
                self.usuarios_repo.obtener_por_cedula(cedula)
                or self.usuarios_repo.obtener_por_id(datos_prof.get("user_id"))
            )
            if datos_user:
                resultado.append(self._armar_profesor(datos_user, datos_prof))
        return resultado

    def listar_adscriptores(self):
        return self.listar(tipo="adscriptor")

    def listar_tutores(self):
        return self.listar(tipo="tutor")

    def buscar_por_cedula(self, cedula):
        for prof in self.listar():
            if prof.cedula == cedula:
                return prof
        return None

    def buscar_por_user_id(self, user_id):
        for prof in self.listar():
            if str(prof.user_id) == str(user_id):
                return prof
        return None

    def alta_adscriptor(
        self, nombre, apellido, cedula, username, password, centro_educativo="",
        segundo_nombre="", segundo_apellido="",
    ):
        if not all((nombre, apellido, cedula, username, password)):
            error("Nombre, apellido, cédula, usuario y contraseña son obligatorios")
            return False
        if (self.profesores_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_username(username)):
            error("Ya existe un profesor con esa cedula o usuario")
            return False
        self.usuarios_repo.agregar(username, password, "adscriptor", cedula)
        try:
            self.profesores_repo.agregar({
                "cedula": cedula, "nombre": nombre, "apellido": apellido,
                "segundo_nombre": segundo_nombre, "segundo_apellido": segundo_apellido,
                "tipo": "adscriptor", "centro_educativo": centro_educativo, "disponible": True,
            })
        except Exception:
            self.usuarios_repo.eliminar_por_cedula(cedula)
            raise
        info(f"Adscriptor {nombre} {apellido} dado de alta")
        return True

    def alta_tutor(
        self, nombre, apellido, cedula, username, password, materia,
        segundo_nombre="", segundo_apellido="",
    ):
        if not all((nombre, apellido, cedula, username, password)):
            error("Nombre, apellido, cédula, usuario y contraseña son obligatorios")
            return False
        if (self.profesores_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_username(username)):
            error("Ya existe un profesor con esa cedula o usuario")
            return False
        self.usuarios_repo.agregar(username, password, "tutor", cedula)
        try:
            self.profesores_repo.agregar({
                "cedula": cedula, "nombre": nombre, "apellido": apellido,
                "segundo_nombre": segundo_nombre, "segundo_apellido": segundo_apellido,
                "tipo": "tutor", "course": materia,
            })
        except Exception:
            self.usuarios_repo.eliminar_por_cedula(cedula)
            raise
        info(f"Tutor {nombre} {apellido} dado de alta")
        return True

    def cambiar_disponibilidad_adscriptor(self, cedula, disponible: bool):
        prof = None
        for r in self.profesores_repo.cargar_todos():
            if r.get("cedula", r.get("ci", r.get("dni"))) == cedula and r["tipo"] == "adscriptor":
                prof = r
                break
        if not prof:
            return False
        prof["disponible"] = disponible
        return self.profesores_repo.actualizar(cedula, prof)
