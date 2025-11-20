import json
from json import JSONDecodeError


class ConfigReader:
    config_file = "./src/config/config.json"
    _data = None

    @classmethod
    def _load(cls):
        if cls._data is None:
            try:
                with open(cls.config_file) as f:
                    cls._data = json.load(f)
            except FileNotFoundError:
                raise "Файл конфигурации не найден"
            except JSONDecodeError:
                raise "Ошибка чтения JSON"
        return cls._data

    @classmethod
    def get_options(cls) -> str:
        return ' '.join(cls._load().get("options"))

    @classmethod
    def get_url(cls) -> str:
        return cls._load().get("base_url")

    @classmethod
    def get_timeout(cls) -> int:
        return cls._load().get("timeout")
