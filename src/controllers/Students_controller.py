

from src.models.usuario_class import Estudiante
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.composables.Estudiantes.estudiantes_repo import EstudiantesRepo
from src.utils.logs import info, error


class StudentsController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.estudiantes_repo = EstudiantesRepo()

    # ---------- ensamblado de objetos ----------
    def _armar_estudiante(self, datos_usuario, datos_estudiante):
        est = Estudiante(
            user_id=datos_usuario["id"],
            nombre=datos_estudiante["nombre"],
            apellido=datos_estudiante["apellido"],
            cedula=datos_estudiante["cedula"],
            username=datos_usuario["user"],
            password=datos_usuario["pass"],
            especialidad=datos_estudiante["especialidad"],
            fecha_nacimiento=datos_estudiante["fecha_nacimiento"],
            direccion=datos_estudiante["direccion"],
            celular=datos_estudiante["celular"],
            anio=datos_estudiante["anio"],
        )
        if datos_estudiante.get("estado") == "Suspenso":
            est.suspender()
        return est

    def listar_estudiantes(self):
        estudiantes = []
        for datos_est in self.estudiantes_repo.cargar_todos():
            datos_user = self.usuarios_repo.obtener_por_cedula(datos_est["cedula"])
            if datos_user:
                estudiantes.append(self._armar_estudiante(datos_user, datos_est))
        return estudiantes

    def buscar_por_cedula(self, cedula):
        for est in self.listar_estudiantes():
            if est.cedula == cedula:
                return est
        return None

    # ---------- alta ----------
    def alta_estudiante(self, nombre, apellido, cedula, username, password,
                         especialidad, fecha_nacimiento, direccion, celular, anio):
        if self.estudiantes_repo.existe_cedula(cedula):
            error(f"Ya existe un estudiante con cedula {cedula}")
            return False
        if self.usuarios_repo.existe_username(username):
            error(f"El usuario {username} ya existe")
            return False

        self.usuarios_repo.agregar(username, password, "estudiante", cedula)
        self.estudiantes_repo.agregar({
            "cedula": cedula, "nombre": nombre, "apellido": apellido,
            "especialidad": especialidad, "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion, "celular": celular, "anio": anio,
            "estado": "Habilitado",
        })
        info(f"Estudiante {nombre} {apellido} (CI {cedula}) dado de alta")
        return True

    # ---------- baja ----------
    def baja_estudiante(self, cedula):
        if not self.estudiantes_repo.existe_cedula(cedula):
            return False
        self.estudiantes_repo.eliminar(cedula)
        self.usuarios_repo.eliminar_por_cedula(cedula)
        info(f"Estudiante CI {cedula} dado de baja")
        return True

    # ---------- modificacion ----------
    def modificar_estudiante(self, cedula, **cambios):
        registros = self.estudiantes_repo.cargar_todos()
        for r in registros:
            if r.get("cedula") == cedula:
                r.update(cambios)
                self.estudiantes_repo.guardar_todos(registros)
                return True
        return False

    def cambiar_estado(self, cedula, nuevo_estado):
        if nuevo_estado not in Estudiante.ESTADOS_VALIDOS:
            return False
        return self.modificar_estudiante(cedula, estado=nuevo_estado)
