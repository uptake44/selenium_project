from selenium.webdriver.support.wait import WebDriverWait

from src.config.config_reader import ConfigReader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver, ConfigReader.get_timeout()
        )
