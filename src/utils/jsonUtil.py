import json
import os
import tempfile
from pathlib import Path

import src.utils.queue as QueueUtil


class JsonUtil:
    def __init__(self, path: str):
        self.filepath = Path(path)
        self.queue = QueueUtil.Queue()

    def read(self) -> dict:
        try:
            content = self.filepath.read_text(encoding="utf-8")
        except FileNotFoundError:
            return {}

        if not content.strip():
            return {}
        data = json.loads(content)
        if not isinstance(data, dict):
            raise ValueError(f"El archivo JSON debe contener un objeto: {self.filepath}")
        return data

    def __write(self, data: dict) -> None:
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.filepath.parent,
                prefix=f"{self.filepath.name}.",
                suffix=".tmp",
                delete=False,
            ) as temporary_file:
                temporary_path = Path(temporary_file.name)
                json.dump(data, temporary_file, ensure_ascii=False, indent=4)
                temporary_file.write("\n")
                temporary_file.flush()
                os.fsync(temporary_file.fileno())
            os.replace(temporary_path, self.filepath)
        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()

    def __apply(self) -> None:
        if self.queue.is_empty():
            return
        item = self.queue.dequeue()
        key, value = item
        try:
            data = self.read()
            data[key] = value
            self.__write(data)
        except Exception:
            self.queue.items.insert(0, item)
            raise

    def add_to_json_queue(self, key: str, value) -> None:
        if not key or value is None:
            raise ValueError("Se requiere una clave y un valor para actualizar el JSON")
        self.queue.enqueue((key, value))
        self.__apply()
