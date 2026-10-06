from src.composables.Usuarios.usuarios_repo import UsuariosRepo


usuarios_repo = UsuariosRepo()


def usuario_existe(username: str) -> bool:
    return usuarios_repo.existe_username(username)


def iniciar_sesion(username: str, password: str):
    usuario = usuarios_repo.obtener_por_username(username)
    if usuario and usuario.get("pass") == password:
        return usuario
    return None


def registrar_usuario(username: str, password: str, role: str = "estudiante", cedula: str = ""):
    if not username or not password or usuarios_repo.existe_username(username):
        return None
    roles_actuales = {"alumno": "estudiante", "profesor": "tutor"}
    role = roles_actuales.get(role.strip().lower(), role.strip().lower())
    usuario = usuarios_repo.agregar(username, password, role, cedula)
    return usuario["id"]
