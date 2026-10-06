class Students:
    ESTADOS_VALIDOS = ("Habilitado", "Suspenso")

    def __init__(self, user_id, cedula, nombre, apellido, segundo_apellido,
                 curso, grado, genero, fecha_nacimiento, ciudad, direccion,
                 celular, email, centro_educativo, credencial_civica,
                 especialidad, centro_referencia, segundo_nombre=None):


        self.__user_id = user_id
        self.__cedula = cedula
        self.__nombre = nombre
        self.__segundo_nombre = segundo_nombre
        self.__apellido = apellido
        self.__segundo_apellido = segundo_apellido
        self.__curso = curso
        self.__grado = grado
        self.__genero = genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__celular = celular
        self.__email = email
        self.__centro_educativo = centro_educativo
        self.__credencial_civica = credencial_civica
        self.__especialidad = especialidad
        self.__centro_referencia = centro_referencia
        self.__estado = "Habilitado"




    def get_user_id(self):
        return self.__user_id

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_segundo_nombre(self):
        return self.__segundo_nombre

    def get_apellido(self):
        return self.__apellido

    def get_segundo_apellido(self):
        return self.__segundo_apellido

    def get_curso(self):
        return self.__curso

    def get_grado(self):
        return self.__grado

    def get_genero(self):
        return self.__genero

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_ciudad(self):
        return self.__ciudad

    def get_direccion(self):
        return self.__direccion

    def get_celular(self):
        return self.__celular

    def get_email(self):
        return self.__email

    def get_centro_educativo(self):
        return self.__centro_educativo

    def get_credencial_civica(self):
        return self.__credencial_civica

    def get_especialidad(self):
        return self.__especialidad

    def get_centro_referencia(self):
        return self.__centro_referencia

    @property
    def cedula(self):
        return self.__cedula

    @property
    def nombre(self):
        return self.__nombre

    def get_estado(self):
        return self.__estado

    def cambiar_estado(self, estado):
        if estado not in self.ESTADOS_VALIDOS:
            return False
        self.__estado = estado
        return True

    def mostrar_info(self):
        nombre_completo = " ".join(
            parte for parte in (
                self.__nombre, self.__segundo_nombre, self.__apellido,
                self.__segundo_apellido,
            ) if parte
        )
        return (
            f"{nombre_completo} (CI: {self.__cedula}) | "
            f"Curso: {self.__curso} | Grado: {self.__grado} | "
            f"Estado: {self.__estado}"
        )

    def __str__(self):
        return self.mostrar_info()




    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_segundo_nombre(self, segundo_nombre):
        self.__segundo_nombre = segundo_nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_segundo_apellido(self, segundo_apellido):
        self.__segundo_apellido = segundo_apellido

    def set_genero(self, genero):
        self.__genero = genero

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_celular(self, celular):
        self.__celular = celular

    def set_email(self, email):
        self.__email = email

    def set_credencial_civica(self, credencial_civica):
        self.__credencial_civica = credencial_civica

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad




    def set_curso(self, curso):
        self.__curso = curso

    def set_grado(self, grado):
        self.__grado = grado

    def set_centro_educativo(self, centro_educativo):
        self.__centro_educativo = centro_educativo

    def set_centro_referencia(self, centro_referencia):
        self.__centro_referencia = centro_referencia
