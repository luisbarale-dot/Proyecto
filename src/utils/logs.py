import logging # Importa el modulo de logging para manejar los logs de manera estructurada y facil de leer
from pathlib import Path

from rich.logging import RichHandler # Importa el RichHandler de la libreria rich para mostrar los logs en la consola con formato mas bonico


LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_FILE = LOGS_DIR / "app.log"
LOGGER_NAME = "gestor-practicas" # Nombre del logger, que se utiliza para identificar los logs generados por este modulo

# Funciones para mostrar logs en consola con diferentes niveles, como debug, info, success, warning, error y exception, cada uno con un icono y un color diferente
def _crear_logger() -> logging.Logger:
	logger = logging.getLogger(LOGGER_NAME)
	logger.setLevel(logging.DEBUG)
	logger.propagate = False # Evita que los logs se propaguen a otros loggers, para que solo se muestren en este logger y no se dupliquen en otros loggers

	if logger.handlers: # Si el logger ya tiene handlers, no se crean nuevos handlers para evitar duplicar los logs
		return logger

	LOGS_DIR.mkdir(parents=True, exist_ok=True) # Crea el directorio de logs si no existe, con la opcion parents=True para crear los directorios padres si no existen y exist_ok=True para no lanzar un error si el directorio ya existe

	consola = RichHandler( # Crea un handler de RichHandler para mostrar los logs en la consola con formato bonito y colores
		rich_tracebacks=True,
		show_path=False,
		markup=True,
	)
	consola.setLevel(logging.INFO) # Establece el nivel de logeo del handler de consola a INFO, para que solo se muestren los logs de nivel INFO o superior en la consola

	archivo = logging.FileHandler(LOG_FILE, encoding="utf-8") # Crea un handler de FileHandler para guardar los logs en un archivo de texto plano con codificacion UTF-8
	archivo.setLevel(logging.DEBUG) # Establece el nivel de logeo del handler de archivo a DEBUG, para que se guarden todos los logs de nivel DEBUG o superior en el archivo de logs
	archivo.setFormatter( # Establece el formato de los logs en el archivo de logs, con la fecha y hora, el nivel de logeo, el nombre del logger y el mensaje del log
		logging.Formatter(
			"%(asctime)s | %(levelname)s | %(name)s | %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S",
		)
	)
	# Agrega los handlers de consola y archivo al logger, para que los logs se muestren en la consola y se guarden en el archivo de logs
	logger.addHandler(consola)
	logger.addHandler(archivo)
	return logger


logger = _crear_logger()


def debug(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.debug("🔍 %s", mensaje, *args, **kwargs)


def info(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.info("ℹ️ %s", mensaje, *args, **kwargs)


def success(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.info("✅ %s", mensaje, *args, **kwargs)


def warning(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.warning("⚠️ %s", mensaje, *args, **kwargs)


def error(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.error("❌ %s", mensaje, *args, **kwargs)


def exception(mensaje: str, *args: object, **kwargs: object) -> None:
	logger.exception("❌ %s", mensaje, *args, **kwargs)
