from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config_reader import ConfigReader


class ChromeDriver:
    _driver = None

    def __new__(cls):
        if cls._driver is None:
            cls._driver = cls._get_driver()
        return cls._driver

    @classmethod
    def _get_driver(cls) -> webdriver.Chrome:
        options = Options()
        if ConfigReader.is_headless():
            options.add_argument("--headless=new")
        for opt in ConfigReader.get_options():
            options.add_argument(opt)
        return webdriver.Chrome(options=options)

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
