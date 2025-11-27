from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config_reader import ConfigReader

class ChromeDriver:
    _driver = None

    def __new__(cls, language):
        if cls._driver is None:
            cls._driver = cls._get_driver(language)
        return cls._driver

    @classmethod
    def _get_driver(cls, language) -> webdriver.Chrome:
        options = Options()
        if ConfigReader.is_headless():
            options.add_argument("--headless=new")
        options.add_argument(ConfigReader.get_options())
        options.add_argument(f"--lang={language}")
        return webdriver.Chrome(options=options)

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
