import json
from json import JSONDecodeError


class ConfigError(Exception):
    pass


class ConfigReader:
    CONFIG_FILE = "./src/config/config.json"
    _data = None

    @classmethod
    def _load(cls):
        if cls._data is None:
            try:
                with open(cls.CONFIG_FILE, "r") as cfg:
                    cls._data = json.load(cfg)
            except FileNotFoundError:
                raise ConfigError("Файл не найден")
            except JSONDecodeError:
                raise ConfigError("Ошибка чтения JSON")
        return cls._data

    @classmethod
    def get_chrome_options(cls) -> list:
        options = cls._load().setdefault("chrome_options", [])
        if len(options) < 1:
            raise ConfigError("Параметры запуска не заданы")
        return options

    @classmethod
    def is_headless(cls) -> bool:
        return cls._load().setdefault("headless", False)

    @classmethod
    def get_default_timeout(cls) -> int:
        return cls._load().setdefault("default_timeout", 15)

    @classmethod
    def get_page_load_timeout(cls) -> int:
        return cls._load().setdefault("page_load_timeout", 120)

    @classmethod
    def get_fast_poll_frequency(cls) -> float:
        return cls._load().setdefault("fast_poll_frequency", 0.1)

    @classmethod
    def get_base_url(cls) -> str:
        base_url = cls._load().get("base_url")
        if base_url is None:
            raise ConfigError("URL не задан")
        return base_url
