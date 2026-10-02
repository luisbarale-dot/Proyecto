
class Usuario:
    """Clase base de la que heredan todos los roles del sistema."""

    def __init__(self, user_id, nombre, apellido, cedula, username, password, rol):
        self.user_id = user_id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.rol = rol

        # Atributos privados: solo accesibles a traves de metodos publicos
        self.__username = username
        self.__password = password

    # Encapsulamiento: getters/setters publicos para atributos privados ---
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
        # Expone la password solo para que la capa de persistencia la guarde.
        return self.__password

    #Metodo pensado para ser sobreescrito por cada subclase ---
    def mostrar_info(self):
        return f"[{self.rol.upper()}] {self.nombre} {self.apellido} (CI: {self.cedula})"

    def __str__(self):
        return self.mostrar_info()


class Estudiante(Usuario):
    """Estudiante practicante. Controla su estado (Habilitado/Suspenso)."""

    ESTADOS_VALIDOS = ("Habilitado", "Suspenso")

    def __init__(self, user_id, nombre, apellido, cedula, username, password,
                 especialidad, fecha_nacimiento, direccion, celular, anio):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="estudiante")
        self.especialidad = especialidad
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.celular = celular
        self.anio = anio

        self.__estado = "Habilitado"          # Habilitado / Suspenso

    #Encapsulamiento del estado del alumno
    def get_estado(self):
        return self.__estado

    def suspender(self, motivo=""):
        self.__estado = "Suspenso"
        return self.__estado

    def habilitar(self):
        self.__estado = "Habilitado"
        return self.__estado

    # Sobreescritura del metodo de la clase base 
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Estado: {self.__estado} | Especialidad: {self.especialidad} ({self.anio}. año)"


class Adscriptor(Usuario):
    """Profesor adscriptor: recibe practicantes en su centro y controla
    su disponibilidad y asistencia."""

    def __init__(self, user_id, nombre, apellido, cedula, username, password, centro_educativo=None):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="adscriptor")
        self.centro_educativo = centro_educativo
        self.__disponible = True                 # privado: se controla via metodos
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

    #Sobreescritura
    def mostrar_info(self):
        base = super().mostrar_info()
        disponibilidad = "Disponible" if self.__disponible else "No disponible"
        return f"{base} | {disponibilidad} | A cargo de {len(self.__estudiantes_a_cargo)} estudiante(s)"


class Tutor(Usuario):
    """Profesor orientador / de didactica: realiza las visitas de
    inspeccion didactica y registra la calificacion de cada visita."""

    def __init__(self, user_id, nombre, apellido, cedula, username, password, materia):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="tutor")
        self.materia = materia

    # Sobreescritura
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Materia: {self.materia}"


class Admin(Usuario):
    """Administrador del sistema: gestiona centros, grupos y usuarios."""

    def __init__(self, user_id, nombre, apellido, cedula, username, password):
        super().__init__(user_id, nombre, apellido, cedula, username, password, rol="admin")

    #  Sobreescritura 
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Administrador del sistema"
