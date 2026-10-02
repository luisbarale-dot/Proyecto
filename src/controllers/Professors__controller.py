

from src.models.usuario_class import Adscriptor, Tutor
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.composables.Profesores.profesores_repo import ProfesoresRepo
from src.utils.logs import info, error


class ProfessorsController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.profesores_repo = ProfesoresRepo()

    def _armar_profesor(self, datos_usuario, datos_prof):
        if datos_prof["tipo"] == "adscriptor":
            prof = Adscriptor(
                user_id=datos_usuario["id"], nombre=datos_prof["nombre"],
                apellido=datos_prof["apellido"], cedula=datos_prof["cedula"],
                username=datos_usuario["user"], password=datos_usuario["pass"],
                centro_educativo=datos_prof.get("centro_educativo"),
            )
            prof.cambiar_disponibilidad(bool(datos_prof.get("disponible", True)))
            return prof
        else:  # tutor
            return Tutor(
                user_id=datos_usuario["id"], nombre=datos_prof["nombre"],
                apellido=datos_prof["apellido"], cedula=datos_prof["cedula"],
                username=datos_usuario["user"], password=datos_usuario["pass"],
                materia=datos_prof.get("materia"),
            )

    def listar(self, tipo=None):
        resultado = []
        for datos_prof in self.profesores_repo.cargar_todos():
            if tipo and datos_prof["tipo"] != tipo:
                continue
            datos_user = self.usuarios_repo.obtener_por_cedula(datos_prof["cedula"])
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

    def alta_adscriptor(self, nombre, apellido, cedula, username, password, centro_educativo=""):
        if self.profesores_repo.existe_cedula(cedula) or self.usuarios_repo.existe_username(username):
            error("Ya existe un profesor con esa cedula o usuario")
            return False
        self.usuarios_repo.agregar(username, password, "adscriptor", cedula)
        self.profesores_repo.agregar({
            "cedula": cedula, "nombre": nombre, "apellido": apellido,
            "tipo": "adscriptor", "centro_educativo": centro_educativo, "disponible": True,
        })
        info(f"Adscriptor {nombre} {apellido} dado de alta")
        return True

    def alta_tutor(self, nombre, apellido, cedula, username, password, materia):
        if self.profesores_repo.existe_cedula(cedula) or self.usuarios_repo.existe_username(username):
            error("Ya existe un profesor con esa cedula o usuario")
            return False
        self.usuarios_repo.agregar(username, password, "tutor", cedula)
        self.profesores_repo.agregar({
            "cedula": cedula, "nombre": nombre, "apellido": apellido,
            "tipo": "tutor", "materia": materia,
        })
        info(f"Tutor {nombre} {apellido} dado de alta")
        return True

    def cambiar_disponibilidad_adscriptor(self, cedula, disponible: bool):
        prof = None
        for r in self.profesores_repo.cargar_todos():
            if r["cedula"] == cedula and r["tipo"] == "adscriptor":
                prof = r
                break
        if not prof:
            return False
        prof["disponible"] = disponible
        return self.profesores_repo.actualizar(cedula, prof)
