import re
import unicodedata
import math

from src.composables.Instituciones.instituciones_repo import InstitucionesRepo
from src.composables.Practicas.practicas_repo import PracticasRepo
from src.composables.Practicas.seguimiento_repo import SeguimientoRepo
from src.controllers.Professors__controller import ProfessorsController
from src.controllers.Students_controller import StudentsController


TIPOS_PRACTICA = {
    "segundo_tercero": "Segundo y tercero",
    "cuarto": "Cuarto año",
}


class PracticasController:
    TIPOS_PRACTICA = TIPOS_PRACTICA

    def __init__(self):
        self.instituciones_repo = InstitucionesRepo()
        self.solicitudes_repo = PracticasRepo()
        self.seguimiento_repo = SeguimientoRepo()
        self.estudiantes = StudentsController()
        self.profesores = ProfessorsController()

    def crear_institucion(self, nombre, cupos_segundo_tercero=0, cupos_cuarto=0):
        return self.instituciones_repo.crear(
            nombre, cupos_segundo_tercero, cupos_cuarto,
        )

    def instituciones_con_cupo(self, tipo_practica):
        resultado = []
        for institucion in self.instituciones_repo.cargar_todos():
            capacidad = institucion.get("cupos", {}).get(tipo_practica, 0)
            ocupados = self._cupos_ocupados(institucion.get("id"), tipo_practica)
            if capacidad > ocupados:
                item = dict(institucion)
                item["disponibles"] = capacidad - ocupados
                resultado.append(item)
        return resultado

    def cupos_ocupados(self, institucion_id, tipo_practica):
        return self._cupos_ocupados(institucion_id, tipo_practica)

    def actualizar_cupos(self, institucion_id, cupos_segundo_tercero, cupos_cuarto):
        institucion = self.instituciones_repo.obtener_por_id(institucion_id)
        if not institucion:
            return False, "No existe esa institución."
        try:
            cupos_segundo_tercero = int(cupos_segundo_tercero)
            cupos_cuarto = int(cupos_cuarto)
        except (TypeError, ValueError):
            return False, "Los cupos deben ser números enteros."
        solicitudes = self.solicitudes_repo.cargar_todos()
        for tipo, nuevos_cupos in (
            ("segundo_tercero", cupos_segundo_tercero),
            ("cuarto", cupos_cuarto),
        ):
            ocupados = sum(
                1 for solicitud in solicitudes
                if solicitud.get("institucion_id") == institucion.get("id")
                and solicitud.get("tipo_practica") == tipo
                and solicitud.get("estado") == "aceptada"
            )
            if int(nuevos_cupos) < ocupados:
                return False, f"No se puede reducir {TIPOS_PRACTICA[tipo]} por debajo de los {ocupados} cupos ocupados."
        try:
            actualizado = self.instituciones_repo.actualizar_cupos(
                institucion_id, cupos_segundo_tercero, cupos_cuarto,
            )
        except ValueError as exc:
            return False, str(exc)
        return (True, "Cupos actualizados.") if actualizado else (False, "No existe esa institución.")

    def inscribir(self, student_user_id, institucion_id, tipo_practica):
        tipo_practica = str(tipo_practica).strip().lower()
        if tipo_practica not in TIPOS_PRACTICA:
            return False, "Tipo de práctica inválido."
        estudiante = self.estudiantes.buscar_por_user_id(student_user_id)
        if not estudiante:
            return False, "No se encontró el perfil del estudiante."
        if estudiante.get_estado() != "Habilitado":
            return False, "El estudiante no está habilitado para inscribirse."
        categoria = self._categoria_grado(estudiante.get_grado())
        if categoria != tipo_practica:
            return False, "El tipo de práctica no corresponde al año del estudiante."
        institucion = self.instituciones_repo.obtener_por_id(institucion_id)
        if not institucion:
            return False, "No existe esa institución."
        cupos = institucion.get("cupos", {}).get(tipo_practica, 0)
        ocupados = self._cupos_ocupados(institucion_id, tipo_practica)
        if ocupados >= cupos:
            return False, "La institución no tiene cupos disponibles para esta práctica."
        if any(
            str(s.get("student_user_id")) == str(student_user_id)
            and s.get("estado") in ("pendiente", "aceptada")
            for s in self.solicitudes_repo.cargar_todos()
        ):
            return False, "El estudiante ya tiene una solicitud pendiente o una práctica aceptada."
        self.solicitudes_repo.crear_solicitud(
            student_user_id, institucion.get("id"), tipo_practica,
        )
        return True, "Solicitud enviada; queda pendiente de aceptación por un adscriptor."

    def solicitudes_del_estudiante(self, student_user_id):
        instituciones = {
            str(i["id"]): i["nombre"]
            for i in self.instituciones_repo.cargar_todos()
        }
        resultado = []
        for solicitud in self.solicitudes_repo.cargar_todos():
            if str(solicitud.get("student_user_id")) != str(student_user_id):
                continue
            item = dict(solicitud)
            item["institucion"] = instituciones.get(str(item.get("institucion_id")), "Institución desconocida")
            item["tipo_descripcion"] = TIPOS_PRACTICA.get(item.get("tipo_practica"), item.get("tipo_practica"))
            resultado.append(item)
        return resultado

    def cancelar_solicitud(self, student_user_id, solicitud_id):
        solicitud = self._buscar_solicitud(solicitud_id)
        if not solicitud or str(solicitud.get("student_user_id")) != str(student_user_id):
            return False, "No se encontró esa solicitud del estudiante."
        if solicitud.get("estado") != "pendiente":
            return False, "Sólo se pueden cancelar solicitudes pendientes."
        self.solicitudes_repo.actualizar(solicitud_id, {"estado": "cancelada"})
        return True, "Solicitud cancelada."

    def solicitudes_pendientes_adscriptor(self, adscriptor_user_id):
        perfil = self.profesores.profesores_repo.obtener_adscriptor(adscriptor_user_id)
        if not perfil:
            return []
        estudiantes = {
            str(e.get_user_id()): e
            for e in self.estudiantes.listar_estudiantes()
        }
        instituciones = {
            str(i["id"]): i["nombre"]
            for i in self.instituciones_repo.cargar_todos()
        }
        resultado = []
        for solicitud in self.solicitudes_repo.cargar_todos():
            if (
                solicitud.get("estado") != "pendiente"
                or str(solicitud.get("institucion_id")) != str(perfil.get("institucion_id"))
            ):
                continue
            item = dict(solicitud)
            item["institucion"] = instituciones.get(str(item.get("institucion_id")), "Institución desconocida")
            item["tipo_descripcion"] = TIPOS_PRACTICA.get(item.get("tipo_practica"), item.get("tipo_practica"))
            estudiante = estudiantes.get(str(item.get("student_user_id")))
            item["estudiante"] = str(estudiante) if estudiante else "Estudiante sin perfil"
            resultado.append(item)
        return resultado

    def resolver_solicitud(self, adscriptor_user_id, solicitud_id, aceptar):
        perfil = self.profesores.profesores_repo.obtener_adscriptor(adscriptor_user_id)
        if not perfil:
            return False, "No se encontró el perfil del adscriptor."
        solicitud = self._buscar_solicitud(solicitud_id)
        if not solicitud or solicitud.get("estado") != "pendiente":
            return False, "La solicitud no existe o ya fue resuelta."
        if str(solicitud.get("institucion_id")) != str(perfil.get("institucion_id")):
            return False, "Sólo se pueden gestionar solicitudes de la institución asignada."

        cambios = {
            "estado": "aceptada" if aceptar else "rechazada",
            "revisado_por_user_id": adscriptor_user_id,
        }
        if aceptar:
            estudiante = self.estudiantes.buscar_por_user_id(
                solicitud.get("student_user_id"),
            )
            if not estudiante or estudiante.get_estado() != "Habilitado":
                return False, "El estudiante no existe o no está habilitado."
            if self._categoria_grado(estudiante.get_grado()) != solicitud.get("tipo_practica"):
                return False, "El tipo de práctica ya no corresponde al año del estudiante."
            adscriptor = self.profesores.buscar_por_user_id(adscriptor_user_id)
            if not adscriptor or not adscriptor.esta_disponible():
                return False, "El adscriptor no está disponible."
            limite = int(perfil.get("max_alumnos", 0))
            asignados = sum(
                1 for s in self.solicitudes_repo.cargar_todos()
                if str(s.get("adscriptor_user_id")) == str(adscriptor_user_id)
                and s.get("estado") == "aceptada"
            )
            if asignados >= limite:
                return False, "El adscriptor alcanzó el máximo de alumnos configurado por administración."
            tipo = solicitud.get("tipo_practica")
            institucion = self.instituciones_repo.obtener_por_id(solicitud.get("institucion_id"))
            if not institucion:
                return False, "La institución de la solicitud ya no existe."
            cupos = institucion.get("cupos", {}).get(tipo, 0)
            if self._cupos_ocupados(solicitud.get("institucion_id"), tipo) >= cupos:
                return False, "La institución ya completó los cupos para esta práctica."
            cambios["adscriptor_user_id"] = adscriptor_user_id

        self.solicitudes_repo.actualizar(solicitud_id, cambios)
        if aceptar:
            self.seguimiento_repo.crear_si_no_existe(solicitud)
        return True, "Solicitud aceptada." if aceptar else "Solicitud rechazada."

    def seguimientos_del_estudiante(self, student_user_id):
        return self._listar_seguimientos(
            lambda solicitud: str(solicitud.get("student_user_id")) == str(student_user_id),
        )

    def seguimientos_de_adscriptor(self, adscriptor_user_id):
        return self._listar_seguimientos(
            lambda solicitud: solicitud.get("estado") == "aceptada"
            and str(solicitud.get("adscriptor_user_id")) == str(adscriptor_user_id),
        )

    def seguimientos_administracion(self):
        return self._listar_seguimientos(lambda solicitud: solicitud.get("estado") == "aceptada")

    def actualizar_seguimiento(self, actor_user_id, solicitud_id, faltas=None, nota_final=None):
        solicitud = self._buscar_solicitud(solicitud_id)
        if not solicitud or solicitud.get("estado") != "aceptada":
            return False, "No se encontró una práctica aceptada con ese ID."
        usuario = self.estudiantes.usuarios_repo.obtener_por_id(actor_user_id)
        rol = str(usuario.get("rol", "")).strip().lower() if usuario else ""
        if rol == "adscriptor":
            if str(solicitud.get("adscriptor_user_id")) != str(actor_user_id):
                return False, "Sólo puedes modificar el seguimiento de tus alumnos asignados."
        elif rol != "admin":
            return False, "No tienes permiso para modificar el seguimiento."
        actual = self.seguimiento_repo.crear_si_no_existe(solicitud)
        cambios = {}
        if faltas is not None:
            try:
                valor_faltas = int(faltas)
                if str(faltas).strip() != str(valor_faltas) or valor_faltas < 0:
                    raise ValueError
            except (TypeError, ValueError):
                return False, "Las faltas deben ser un entero igual o mayor que cero."
            cambios["faltas"] = valor_faltas
        if nota_final is not None:
            try:
                valor_nota = float(nota_final)
                if not math.isfinite(valor_nota) or not 0 <= valor_nota <= 12:
                    raise ValueError
            except (TypeError, ValueError):
                return False, "La nota final debe ser un número entre 0 y 12."
            cambios["nota_final"] = int(valor_nota) if valor_nota.is_integer() else valor_nota
        if not cambios:
            return False, "Indica al menos un dato para actualizar."
        faltas_finales = cambios.get("faltas", actual.get("faltas", 0))
        nota = cambios.get("nota_final", actual.get("nota_final"))
        if faltas_finales > 25:
            estado, recursa = "Suspendida - debe recursar el año", True
        elif nota is None:
            estado, recursa = "En curso", False
        elif nota > 9:
            estado, recursa = "Aprobada", False
        else:
            estado, recursa = "No aprobada", False
        cambios.update({"estado": estado, "debe_recursar": recursa, "actualizado_por_user_id": actor_user_id})
        self.seguimiento_repo.actualizar(solicitud_id, cambios)
        return True, "Seguimiento actualizado."

    def _listar_seguimientos(self, filtro):
        solicitudes = {str(s.get("id")): s for s in self.solicitudes_repo.cargar_todos()}
        instituciones = {str(i.get("id")): i.get("nombre", "Institución desconocida") for i in self.instituciones_repo.cargar_todos()}
        estudiantes = {str(e.get_user_id()): str(e) for e in self.estudiantes.listar_estudiantes()}
        resultado = []
        for solicitud in solicitudes.values():
            if solicitud.get("estado") != "aceptada" or not filtro(solicitud):
                continue
            seguimiento = self.seguimiento_repo.crear_si_no_existe(solicitud)
            item = dict(seguimiento)
            item.update({
                "estudiante": estudiantes.get(str(solicitud.get("student_user_id")), "Estudiante sin perfil"),
                "institucion": instituciones.get(str(solicitud.get("institucion_id")), "Institución desconocida"),
                "tipo_descripcion": TIPOS_PRACTICA.get(solicitud.get("tipo_practica"), solicitud.get("tipo_practica")),
            })
            resultado.append(item)
        return resultado

    def _cupos_ocupados(self, institucion_id, tipo_practica):
        return sum(
            1 for solicitud in self.solicitudes_repo.cargar_todos()
            if str(solicitud.get("institucion_id")) == str(institucion_id)
            and solicitud.get("tipo_practica") == tipo_practica
            and solicitud.get("estado") == "aceptada"
        )

    def _buscar_solicitud(self, solicitud_id):
        for solicitud in self.solicitudes_repo.cargar_todos():
            if str(solicitud.get("id")) == str(solicitud_id):
                return solicitud
        return None

    @staticmethod
    def _categoria_grado(grado):
        texto = str(grado or "").strip().lower()
        texto = "".join(
            caracter for caracter in unicodedata.normalize("NFD", texto)
            if unicodedata.category(caracter) != "Mn"
        )
        if "segundo" in texto or re.search(r"(^|\D)2(\D|$)", texto):
            return "segundo_tercero"
        if "tercer" in texto or re.search(r"(^|\D)3(\D|$)", texto):
            return "segundo_tercero"
        if "cuarto" in texto or re.search(r"(^|\D)4(\D|$)", texto):
            return "cuarto"
        return None
