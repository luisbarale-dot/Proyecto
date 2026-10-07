

from src.models.usuario_class import Adscriptor, Profesor
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.composables.Profesores.profesores_repo import ProfesoresRepo
from src.composables.Instituciones.instituciones_repo import InstitucionesRepo
from src.composables.Practicas.practicas_repo import PracticasRepo
from src.utils.logs import info, error
from src.utils.arbol_binario_busqueda import ArbolBinarioBusqueda


class ProfessorsController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.profesores_repo = ProfesoresRepo()
        self.instituciones_repo = InstitucionesRepo()
        self.profesores_repo.migrar_user_ids(self.usuarios_repo)
        self.profesores_repo.migrar_instituciones(self.instituciones_repo)

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
                institucion_id=datos_prof.get("institucion_id"),
                max_alumnos=datos_prof.get("max_alumnos", 0),
                segundo_nombre=segundo_nombre,
                segundo_apellido=segundo_apellido,
            )
            prof.cambiar_disponibilidad(bool(datos_prof.get("disponible", True)))
            return prof
        else:
            return Profesor(
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
            datos_user = self.usuarios_repo.obtener_por_id(datos_prof.get("user_id"))
            if datos_user and str(datos_user.get("rol", "")).lower() == datos_prof["tipo"]:
                resultado.append(self._armar_profesor(datos_user, datos_prof))
        return resultado

    def listar_adscriptores(self):
        return self.listar(tipo="adscriptor")

    def listar_profesores(self):
        return self.listar(tipo="profesor")

    def buscar_por_cedula(self, cedula):
        return self._indice_profesores("cedula").buscar(str(cedula))

    def buscar_por_user_id(self, user_id):
        return self._indice_profesores("user_id").buscar(str(user_id))

    def _indice_profesores(self, atributo, tipo=None):
        indice = ArbolBinarioBusqueda()
        for profesor in self.listar(tipo=tipo):
            clave = getattr(profesor, atributo)
            if clave is not None:
                indice.insertar(str(clave), profesor)
        return indice

    def alta_adscriptor(
        self, nombre, apellido, cedula, username, password, centro_educativo="",
        segundo_nombre="", segundo_apellido="", institucion_id=None,
    ):
        if not all((nombre, apellido, cedula, username, password)):
            error("El nombre, el apellido, la cédula, el usuario y la contraseña son obligatorios.")
            return False
        institucion = InstitucionesRepo().obtener_por_id(institucion_id)
        if not institucion:
            error("Seleccione una institución válida para el adscriptor.")
            return False
        if (self.profesores_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_username(username)):
            error("Ya existe una persona con esa cédula o ese nombre de usuario.")
            return False
        usuario = self.usuarios_repo.agregar(username, password, "adscriptor", cedula)
        try:
            self.profesores_repo.agregar({
                "user_id": usuario["id"],
                "cedula": cedula, "nombre": nombre, "apellido": apellido,
                "segundo_nombre": segundo_nombre, "segundo_apellido": segundo_apellido,
                "tipo": "adscriptor", "centro_educativo": institucion["nombre"],
                "institucion_id": institucion["id"], "max_alumnos": 0,
                "disponible": True,
            })
        except Exception:
            self.usuarios_repo.eliminar_por_id(usuario["id"])
            raise
        info(f"Adscriptor {nombre} {apellido} registrado.")
        return True

    def alta_profesor(
        self, nombre, apellido, cedula, username, password, materia,
        segundo_nombre="", segundo_apellido="",
    ):
        if not all((nombre, apellido, cedula, username, password)):
            error("El nombre, el apellido, la cédula, el usuario y la contraseña son obligatorios.")
            return False
        if (self.profesores_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_cedula(cedula)
                or self.usuarios_repo.existe_username(username)):
            error("Ya existe una persona con esa cédula o ese nombre de usuario.")
            return False
        usuario = self.usuarios_repo.agregar(username, password, "profesor", cedula)
        try:
            self.profesores_repo.agregar({
                "user_id": usuario["id"],
                "cedula": cedula, "nombre": nombre, "apellido": apellido,
                "segundo_nombre": segundo_nombre, "segundo_apellido": segundo_apellido,
                "tipo": "profesor", "course": materia,
            })
        except Exception:
            self.usuarios_repo.eliminar_por_id(usuario["id"])
            raise
        info(f"Profesor {nombre} {apellido} registrado.")
        return True

    def configurar_max_alumnos(self, user_id, max_alumnos):
        try:
            max_alumnos = int(max_alumnos)
        except (TypeError, ValueError):
            return False
        perfil = self.profesores_repo.obtener_adscriptor(user_id)
        if max_alumnos < 0 or not perfil:
            return False
        solicitudes = PracticasRepo().cargar_todos()
        asignados = sum(
            1 for solicitud in solicitudes
            if str(solicitud.get("adscriptor_user_id")) == str(user_id)
            and solicitud.get("estado") == "aceptada"
        )
        if max_alumnos < asignados:
            return False
        return self.profesores_repo.actualizar_adscriptor(
            user_id, {"max_alumnos": max_alumnos},
        )

    def cambiar_disponibilidad_adscriptor(self, user_id, disponible: bool):
        if not self.profesores_repo.obtener_adscriptor(user_id):
            return False
        return self.profesores_repo.actualizar_adscriptor(
            user_id, {"disponible": bool(disponible)},
        )
