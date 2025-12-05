import json
from json import JSONDecodeError
from enum import StrEnum


class Language(StrEnum):
    ENG = "en"
    RUS = "ru"


class ConfigError(Exception):
    pass


class ConfigReader:
    CONFIG_FILE = "./src/config/config.json"
    _data = None

    @classmethod
    def _load(cls):
        if cls._data is None:
            try:
                with open(cls.CONFIG_FILE) as f:
                    cls._data = json.load(f)
            except FileNotFoundError:
                raise ConfigError("Файл конфигурации не найден")
            except JSONDecodeError:
                raise ConfigError("Ошибка чтения JSON")
        return cls._data

    @classmethod
    def get_options(cls) -> list:
        return cls._load().get("options")

    @classmethod
    def get_url(cls) -> str:
        return cls._load().get("base_url")

    @classmethod
    def get_timeout(cls) -> int:
        return cls._load().get("timeout")

    @classmethod
    def get_fast_poll_frequency(cls) -> int:
        return cls._load().get("fast_poll_frequency")

    @classmethod
    def get_languages(cls) -> list:
        return cls._load().get("lang")

    @classmethod
    def is_headless(cls) -> bool:
        return cls._load().get("headless")

    @classmethod
    def get_lang_cookie(cls) -> str:
        return cls._load().get("language_cookie")
