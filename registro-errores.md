**Error #001** — Dependencia innecesaria de la librería Rich
Módulos: Vistas del proyecto
Estado: Solucionado (aún en Branch)

**Descripción:**
Las interfaces del proyecto utilizaban componentes de la librería externa rich para mostrar mensajes y solicitar datos al usuario. Esto agregaba una dependencia externa que no era necesaria para el funcionamiento principal del programa.

**Causa:**
Las vistas habían sido desarrolladas utilizando elementos como Console y Prompt de Rich en lugar de las funciones estándar de Python.

**Solución:**
Se decidió eliminar Rich de las vistas y utilizar únicamente herramientas incorporadas en Python.

=================================================================

**Error #002** — inicio_sesion.py todavía dependía de Rich
Archivo: inicio_sesion.py
Estado: Solucionado (aún en Branch)

**Descripción:**
Después de decidir eliminar Rich, la vista de inicio de sesión todavía utilizaba elementos como Prompt.ask() y console.input(). Esto hacía que el proyecto continuara dependiendo de Rich para realizar el login.

**Causa:**
El archivo había sido desarrollado originalmente utilizando la interfaz proporcionada por Rich.

**Solución:**
Se modificó inicio_sesion.py reemplazando las entradas de Rich por input() y las salidas correspondientes por herramientas estándar de Python. De esta manera, el inicio de sesión dejó de necesitar Rich.

===============================================================

**Error #003** — El flujo continuaba después de un inicio de sesión exitoso
Archivo: inicio_sesion.py
Estado: Solucionado (aún en Branch)

**Descripción:**
Después de validar correctamente las credenciales de un usuario, la función podía continuar ejecutando instrucciones que ya no correspondían al flujo de inicio de sesión.

**Causa:**
No se estaba finalizando correctamente la función después de completar un inicio de sesión exitoso.

**Solución:**
Se agregó el return correspondiente después de completar el inicio de sesión y enviar al usuario al menú adecuado. Esto permitió finalizar correctamente el flujo del login.

=======================================================================

**Error #004** — Falta de conexión entre el inicio de sesión y el registro de usuarios
Archivos: inicio_sesion.py / registro_menu.py
Estado: Solucionado (aún en Branch)

**Descripción:**
Cuando se intentaba iniciar sesión con un usuario que todavía no estaba registrado, el programa no tenía correctamente integrado el acceso al proceso de creación de una nueva cuenta.

**Causa:**
El inicio de sesión y el registro de usuario todavía no estaban correctamente conectados.

**Solución:**
Se modificó el funcionamiento para permitir acceder al registro cuando el usuario no existe. También se realizaron cambios en registro_menu.py para adaptar el proceso de registro al nuevo funcionamiento del proyecto sin Rich.

=================================================================

**Error #005** — Falta de centralización del registro de usuarios
Archivo: auth.py
Estado: Solucionado (aún en Branch)

**Descripción:**
El proyecto necesitaba una función encargada de registrar y almacenar correctamente los nuevos usuarios desde el sistema de autenticación.

**Causa:**
La lógica necesaria para guardar un usuario nuevo todavía no estaba completamente integrada con el sistema de autenticación.

**Solución:**
Se incorporó la función registrar_usuario() en auth.py. Para almacenar los usuarios se utilizó:
json_utils.add_to_json_queue("Usuarios", usuarios)
De esta manera, el registro quedó conectado con el sistema utilizado por el proyecto para almacenar los datos en JSON.

=================================================================

**Error #006** — Dependencia de Rich en el sistema de logs
Archivo: logs.py
Estado: Identificado / Pendiente de revisión

**Descripción:**
Durante el proceso de eliminación de Rich del proyecto se detectó que logs.py también contenía una dependencia relacionada con esta librería. Esto impedía considerar completamente eliminada la dependencia de Rich del proyecto.

**Causa:**
El sistema de logs había sido desarrollado utilizando componentes asociados a Rich.

**Solución:**
Se identificó logs.py como uno de los archivos que debía ser revisado para completar la eliminación de Rich. La modificación definitiva del sistema de logs quedó pendiente de revisión.