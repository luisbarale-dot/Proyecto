import logging
from pathlib import Path


LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_FILE = LOGS_DIR / "app.log"
LOGGER_NAME = "gestor-practicas"


def _crear_logger() -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if logger.handlers:
        return logger

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    consola = logging.StreamHandler()
    consola.setLevel(logging.INFO)
    consola.setFormatter(logging.Formatter("%(message)s"))

    archivo = logging.FileHandler(LOG_FILE, encoding="utf-8")
    archivo.setLevel(logging.DEBUG)
    archivo.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))

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
