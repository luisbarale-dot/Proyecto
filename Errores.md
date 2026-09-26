**Error #007** — Error de sintaxis por f-string sin cerrar  
**Archivo:** `inicio_sesion.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Al intentar ejecutar el proyecto, Python indicaba un `SyntaxError: unterminated f-string literal`, impidiendo que el programa pudiera iniciarse correctamente.

**Causa:** Una cadena formateada mediante `f-string` no había sido cerrada correctamente en `inicio_sesion.py`.

**Solución:** Se corrigió la estructura de la cadena, cerrando correctamente el `f-string`. Posteriormente se comprobó la compilación del proyecto sin errores de sintaxis.

\=================================================================

**Error #008** — Uso incorrecto de `super()` en la clase `Adscriptores`  
**Archivo:** `professors_class.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** La clase `Adscriptores`, que hereda de `Professors`, realizaba incorrectamente la llamada al constructor de la clase padre.

**Causa:** Se utilizaba `super().__init__(self, ...)`, enviando manualmente `self` al constructor heredado. Python ya proporciona automáticamente la instancia al utilizar `super()`.

**Solución:** Se corrigió la llamada utilizando `super().__init__(user_id, ci, name, course)`, permitiendo que `Adscriptores` herede correctamente los atributos definidos en `Professors`.

\=================================================================

**Error #009** — Comprobación incompleta de profesores existentes  
**Archivo:** `Professors__controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** El método encargado de comprobar si un profesor ya estaba registrado solamente comprobaba correctamente el primer elemento de la lista de profesores.

**Causa:** El `return False` se encontraba dentro del bucle `for`. Por este motivo, si el primer profesor no coincidía con el `user_id` buscado, el método terminaba inmediatamente sin comprobar los demás registros.

**Solución:** Se desplazó `return False` fuera del bucle `for`. De esta forma, el método recorre todos los profesores y solamente devuelve `False` después de comprobar la lista completa.

\=================================================================

**Error #010** — Comprobación incompleta de adscriptores existentes  
**Archivo:** `Adscriptores_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** La búsqueda de un adscriptor existente podía finalizar después de comprobar solamente el primer elemento de la lista.

**Causa:** Al igual que en el controller de profesores, `return False` se encontraba dentro del bucle `for`.

**Solución:** Se colocó `return False` después del bucle, permitiendo comprobar todos los adscriptores antes de determinar que el `user_id` buscado no existe.

\=================================================================

**Error #011** — Comprobación incompleta de alumnos existentes  
**Archivo:** `Students_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** El método utilizado para comprobar la existencia de un alumno podía devolver `False` después de analizar únicamente el primer registro.

**Causa:** La instrucción `return False` se encontraba dentro del bucle utilizado para recorrer la lista de alumnos.

**Solución:** Se trasladó `return False` fuera del bucle para garantizar que se comprueben todos los alumnos registrados.

\=================================================================

**Error #012** — Validación de profesor duplicado ubicada dentro de `except`  
**Archivo:** `Professors__controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** La comprobación destinada a impedir el registro de profesores duplicados solamente se ejecutaba cuando ocurría una excepción.

**Causa:** La llamada a `__professor_exists(user_id)` se había colocado dentro del bloque `except`, confundiendo la validación normal del programa con el tratamiento de errores inesperados.

**Solución:** Se trasladó la comprobación del `user_id` al flujo normal del método, antes de crear y guardar el profesor. Si el profesor ya existe, el método devuelve `False`; el bloque `except` queda reservado para errores inesperados.

\=================================================================

**Error #013** — Registro de profesor sin valor de retorno en caso de éxito  
**Archivo:** `Professors__controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** El método `register_Professor()` devolvía `False` cuando ocurría un problema, pero no devolvía ningún valor cuando el registro se completaba correctamente.

**Causa:** Faltaba una instrucción `return True` después de guardar correctamente los datos del profesor.

**Solución:** Se agregó `return True` después del almacenamiento del nuevo profesor, permitiendo distinguir claramente entre un registro exitoso (`True`) y uno fallido (`False`).

\=================================================================

**Error #014** — Manejo incorrecto del objeto `Exception`  
**Módulos:** Controllers de profesores y adscriptores  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Algunos bloques de tratamiento de errores utilizaban `str(Exception)`, por lo que no mostraban correctamente el error concreto ocurrido durante la ejecución.

**Causa:** Se estaba utilizando directamente la clase `Exception` en lugar de capturar la instancia de la excepción producida.

**Solución:** Se modificaron los bloques correspondientes utilizando `except Exception as e` y posteriormente `str(e)`, permitiendo mostrar información sobre la excepción realmente producida.

\=================================================================

**Error #015** — Clave `ci` escrita incorrectamente en los diccionarios  
**Módulos:** Controllers de profesores y adscriptores  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Algunos diccionarios utilizaban la clave `"ci:"` mientras otras partes del proyecto utilizaban `"ci"`.

**Causa:** Se había agregado accidentalmente el carácter `:` dentro del nombre de la clave.

**Solución:** Se unificó el nombre utilizando `"ci"` en los diccionarios correspondientes.

\=================================================================

**Error #016** — Orden incorrecto de `name` y `ci` al crear un alumno  
**Archivo:** `Students_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Al instanciar la clase `Students`, los valores correspondientes al nombre y la cédula eran enviados en un orden diferente al definido por el constructor.

**Causa:** El controller enviaba primero `ci` y después `name`, mientras que `Students.__init__()` esperaba primero `name` y después `ci`.

**Solución:** Se modificó el orden de los argumentos utilizados por `StudentController` para que coincida con el constructor de `Students`.

\=================================================================

**Error #017** — Inconsistencia en el nombre del archivo y clave de Adscriptores  
**Archivos:** `Adscriptores_controller.py` y JSON de Adscriptores  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Existían diferentes nombres para identificar los datos correspondientes a los adscriptores. Esto podía provocar que el controller no encontrara el archivo o la lista esperada dentro del JSON.

**Causa:** Se utilizaban variantes como `Adcriptores.json`, `Adscriptores.json` y la clave `"Adscriptos"`.

**Solución:** Se unificó la nomenclatura utilizando `Adscriptores.json` como nombre del archivo y `"Adscriptores"` como clave de almacenamiento.

\=================================================================

**Error #018** — Inconsistencia en la clave identificadora de usuarios  
**Archivo:** `Usuarios.json`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** El usuario administrador utilizaba `"user_id"` para almacenar su identificador, mientras los usuarios creados posteriormente utilizaban `"id"`.

**Causa:** Los registros habían sido creados utilizando estructuras diferentes.

**Solución:** Se unificó la estructura de los usuarios utilizando `"id"`, coincidiendo con la clave consultada por `UserController` durante el inicio de sesión.

\=================================================================

**Error #019** — Cálculo redundante del ID después de registrar un usuario  
**Archivo:** `auth.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Después de calcular el nuevo ID, crear el usuario y agregarlo a la lista, el código volvía a asignar `nuevo_id = len(usuarios)` antes de retornarlo.

**Causa:** El ID era calculado dos veces durante el mismo proceso de registro.

**Solución:** Se eliminó la segunda asignación y se retorna directamente el `nuevo_id` calculado al comienzo del registro.

\=================================================================

**Error #020** — `AdminController` continuaba el registro sin comprobar la creación del usuario  
**Archivo:** `Admin_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Los métodos de registro del administrador obtenían el resultado de `UserController.register()`, pero inicialmente no controlaban correctamente si el registro del usuario había fallado antes de intentar crear un profesor, adscriptor o alumno.

**Causa:** No existía una comprobación explícita del valor almacenado en `user_id`.

**Solución:** Se agregó una condición `if user_id` antes de crear los datos específicos de cada rol. Si no se obtiene un ID válido, el método devuelve `False` y se interrumpe únicamente ese proceso de registro.

\=================================================================

**Error #021** — Intento de registrar dos veces al usuario desde `AdminController`  
**Archivo:** `Admin_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** Durante el desarrollo de `register_Professor()` se planteó utilizar `UserController.register()` primero como condición de un `if` y posteriormente volver a ejecutarlo para obtener el ID.

**Causa:** Se intentó separar la comprobación del éxito del registro de la obtención del ID, aunque ambas operaciones estaban representadas por el mismo valor de retorno.

**Solución:** Se estableció una única llamada a `register()`. Su resultado se almacena en `user_id` y posteriormente se comprueba mediante `if user_id`. Así se evita intentar registrar dos veces al mismo usuario.

\=================================================================

**Error #022** — Parámetro `registration_card` sin utilización  
**Archivo:** `Admin_controller.py`  
**Estado:** Solucionado (aún en Branch)

**Descripción:** El método `register_Student()` recibía el parámetro `registration_card`, pero este valor no era utilizado para construir los datos del alumno ni posteriormente almacenado.

**Causa:** El parámetro permaneció en la definición del método aunque ya no formaba parte de la estructura utilizada para registrar alumnos.

**Solución:** Se eliminó `registration_card` de los parámetros de `register_Student()`.

\=================================================================

**Error #023** — Atributos privados inaccesibles desde los controllers  
**Archivos:** `professors_class.py`, `students_class.py` y sus respectivos controllers  
**Estado:** Pendiente

**Descripción:** Los modelos almacenan varios atributos mediante encapsulamiento, utilizando nombres como `__ci`, `__course`, `__grade`, etc. Sin embargo, los controllers intentan acceder a ellos mediante expresiones como `professor.ci`, `professor.course`, `student.ci` o `student.grade`.

**Causa:** Los atributos fueron definidos como privados mediante doble guion bajo, pero todavía no existen propiedades públicas que permitan acceder a ellos desde los controllers.

**Solución prevista:** Implementar getters y setters utilizando `@property`. Esto permitirá conservar los atributos privados y, al mismo tiempo, acceder a ellos mediante expresiones como `professor.ci` y `student.grade`. Además, los setters podrán utilizarse posteriormente para incorporar validaciones.

\=================================================================