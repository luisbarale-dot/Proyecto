
class Usuario:

    def __init__(
        self, user_id, nombre, apellido, cedula, username, password, rol,
        segundo_nombre="", segundo_apellido="",
    ):
        self.user_id = user_id
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.apellido = apellido
        self.segundo_apellido = segundo_apellido
        self.cedula = cedula
        self.rol = rol


        self.__username = username
        self.__password = password


    def get_username(self):
        return self.__username

    def verificar_password(self, password):
        return self.__password == password

    def cambiar_password(self, password_actual, password_nueva):
        if not self.verificar_password(password_actual):
            return False
        self.__password = password_nueva
        return True

    def get_password_hash(self):

        return self.__password


    def mostrar_info(self):
        nombre_completo = " ".join(
            parte for parte in (
                self.nombre, self.segundo_nombre, self.apellido, self.segundo_apellido,
            ) if parte
        )
        return f"[{self.rol.upper()}] {nombre_completo} (CI: {self.cedula})"

    def __str__(self):
        return self.mostrar_info()


class Estudiante(Usuario):

    ESTADOS_VALIDOS = ("Habilitado", "Suspenso")

    def __init__(self, user_id, nombre, apellido, cedula, username, password,
                 especialidad, fecha_nacimiento, direccion, celular, anio):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="estudiante")
        self.especialidad = especialidad
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.celular = celular
        self.anio = anio

        self.__estado = "Habilitado"


    def get_estado(self):
        return self.__estado

    def suspender(self, motivo=""):
        self.__estado = "Suspenso"
        return self.__estado

    def habilitar(self):
        self.__estado = "Habilitado"
        return self.__estado


    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Estado: {self.__estado} | Especialidad: {self.especialidad} ({self.anio}. año)"


class Adscriptor(Usuario):

    def __init__(
        self, user_id, nombre, apellido, cedula, username, password,
        centro_educativo=None, segundo_nombre="", segundo_apellido="",
        institucion_id=None, max_alumnos=0,
    ):
        super().__init__(
            user_id, nombre, apellido, cedula, username, password,
            rol="adscriptor", segundo_nombre=segundo_nombre,
            segundo_apellido=segundo_apellido,
        )
        self.centro_educativo = centro_educativo
        self.institucion_id = institucion_id
        self.max_alumnos = max_alumnos
        self.__disponible = True
        self.__estudiantes_a_cargo = []

    def esta_disponible(self):
        return self.__disponible

    def cambiar_disponibilidad(self, estado: bool):
        self.__disponible = estado

    def aceptar_estudiante(self, cedula_estudiante):
        if cedula_estudiante not in self.__estudiantes_a_cargo:
            self.__estudiantes_a_cargo.append(cedula_estudiante)

    def echar_estudiante(self, cedula_estudiante):
        if cedula_estudiante in self.__estudiantes_a_cargo:
            self.__estudiantes_a_cargo.remove(cedula_estudiante)

    def get_estudiantes_a_cargo(self):
        return list(self.__estudiantes_a_cargo)


    def mostrar_info(self):
        base = super().mostrar_info()
        disponibilidad = "Disponible" if self.__disponible else "No disponible"
        return f"{base} | {disponibilidad} | A cargo de {len(self.__estudiantes_a_cargo)} estudiante(s)"


class Profesor(Usuario):

    def __init__(
        self, user_id, nombre, apellido, cedula, username, password, materia,
        segundo_nombre="", segundo_apellido="",
    ):
        super().__init__(
            user_id, nombre, apellido, cedula, username, password,
            rol="profesor", segundo_nombre=segundo_nombre,
            segundo_apellido=segundo_apellido,
        )
        self.materia = materia


    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Materia: {self.materia}"


class Admin(Usuario):

    def __init__(self, user_id, nombre, apellido, cedula, username, password):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="admin")


    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Administrador del sistema"
