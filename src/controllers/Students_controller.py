from src.models.students_class import Students
from src.composables.Usuarios.usuarios_repo import UsuariosRepo
from src.composables.Estudiantes.estudiantes_repo import EstudiantesRepo
from src.utils.logs import info, error


class StudentsController:
    def __init__(self):
        self.usuarios_repo = UsuariosRepo()
        self.estudiantes_repo = EstudiantesRepo()

    @staticmethod
    def _valor(registro, actual, legado=None):
        if actual in registro:
            return registro[actual]
        return registro.get(legado, "") if legado else ""

    def _armar_estudiante(self, datos_usuario, datos_estudiante):
        valor = self._valor
        estudiante = Students(
            user_id=datos_usuario.get("id", datos_usuario.get("user_id")),
            cedula=valor(datos_estudiante, "cedula", "ci"),
            nombre=valor(datos_estudiante, "nombre", "name"),
            apellido=valor(datos_estudiante, "apellido", "last_name"),
            segundo_apellido=valor(datos_estudiante, "segundo_apellido", "second_last_name"),
            curso=valor(datos_estudiante, "curso", "course"),
            grado=valor(datos_estudiante, "grado", "grade") or valor(datos_estudiante, "anio"),
            genero=valor(datos_estudiante, "genero", "gender"),
            fecha_nacimiento=valor(datos_estudiante, "fecha_nacimiento", "bday"),
            ciudad=valor(datos_estudiante, "ciudad", "city"),
            direccion=valor(datos_estudiante, "direccion", "address"),
            celular=valor(datos_estudiante, "celular", "phone"),
            email=valor(datos_estudiante, "email"),
            centro_educativo=valor(datos_estudiante, "centro_educativo", "educational_center"),
            credencial_civica=valor(datos_estudiante, "credencial_civica", "civic_credential"),
            especialidad=valor(datos_estudiante, "especialidad", "specialization"),
            centro_referencia=valor(datos_estudiante, "centro_referencia", "reference_center"),
            segundo_nombre=valor(datos_estudiante, "segundo_nombre", "second_name"),
        )
        estudiante.cambiar_estado(datos_estudiante.get("estado", "Habilitado"))
        return estudiante

    def listar_estudiantes(self):
        estudiantes = []
        for datos_estudiante in self.estudiantes_repo.cargar_todos():
            cedula = self._valor(datos_estudiante, "cedula", "ci")
            datos_usuario = (
                self.usuarios_repo.obtener_por_cedula(cedula)
                or self.usuarios_repo.obtener_por_id(datos_estudiante.get("user_id"))
            )
            if datos_usuario:
                estudiantes.append(self._armar_estudiante(datos_usuario, datos_estudiante))
        return estudiantes

    def buscar_por_cedula(self, cedula):
        for estudiante in self.listar_estudiantes():
            if estudiante.cedula == cedula:
                return estudiante
        return None

    def buscar_por_user_id(self, user_id):
        for estudiante in self.listar_estudiantes():
            if str(estudiante.get_user_id()) == str(user_id):
                return estudiante
        return None

    def alta_estudiante(
        self, nombre, apellido, cedula, username, password,
        especialidad, fecha_nacimiento, direccion, celular, anio="",
        *, segundo_nombre="", segundo_apellido="", curso="", grado="",
        genero="", ciudad="", email="", centro_educativo="",
        credencial_civica="", centro_referencia="",
    ):
        if not all((nombre, apellido, cedula, username, password)):
            error("Nombre, apellido, cédula, usuario y contraseña son obligatorios")
            return False
        if self.estudiantes_repo.existe_cedula(cedula) or self.usuarios_repo.existe_cedula(cedula):
            error(f"Ya existe una persona con cedula {cedula}")
            return False
        if self.usuarios_repo.existe_username(username):
            error(f"El usuario {username} ya existe")
            return False

        usuario = self.usuarios_repo.agregar(username, password, "estudiante", cedula)
        try:
            self.estudiantes_repo.agregar({
                "user_id": usuario["id"],
                "cedula": cedula,
                "nombre": nombre,
                "segundo_nombre": segundo_nombre,
                "apellido": apellido,
                "segundo_apellido": segundo_apellido,
                "curso": curso,
                "grado": grado or anio,
                "genero": genero,
                "fecha_nacimiento": fecha_nacimiento,
                "ciudad": ciudad,
                "direccion": direccion,
                "celular": celular,
                "email": email,
                "centro_educativo": centro_educativo,
                "credencial_civica": credencial_civica,
                "especialidad": especialidad,
                "centro_referencia": centro_referencia,
                "estado": "Habilitado",
            })
        except Exception:
            self.usuarios_repo.eliminar_por_cedula(cedula)
            raise
        info(f"Estudiante {nombre} {apellido} (CI {cedula}) dado de alta")
        return True

    def baja_estudiante(self, cedula):
        if not self.estudiantes_repo.existe_cedula(cedula):
            return False
        perfil = next(
            registro for registro in self.estudiantes_repo.cargar_todos()
            if registro.get("cedula", registro.get("ci")) == cedula
        )
        self.estudiantes_repo.eliminar(cedula)
        self.usuarios_repo.eliminar_por_cedula(cedula)
        self.usuarios_repo.eliminar_por_id(perfil.get("user_id"))
        info(f"Estudiante CI {cedula} dado de baja")
        return True

    def modificar_estudiante(self, cedula, **cambios):
        registros = self.estudiantes_repo.cargar_todos()
        for registro in registros:
            if registro.get("cedula", registro.get("ci")) == cedula:
                registro.update(cambios)
                self.estudiantes_repo.guardar_todos(registros)
                return True
        return False

    def cambiar_estado(self, cedula, nuevo_estado):
        if nuevo_estado not in Students.ESTADOS_VALIDOS:
            return False
        return self.modificar_estudiante(cedula, estado=nuevo_estado)
