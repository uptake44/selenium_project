from enum import StrEnum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config_reader import ConfigReader
from src.logger.logger import Logger


class BrowserType(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(browser_type: BrowserType):
        Logger.info(f"Start webdriver {browser_type} with options: {ConfigReader.get_chrome_options()}")

        if browser_type == BrowserType.CHROME:
            options = Options()
            for arg in ConfigReader.get_chrome_options():
                options.add_argument(arg)
            if ConfigReader.is_headless():
                options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)
