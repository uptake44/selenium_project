from selenium.webdriver.support.wait import WebDriverWait

from src.config.config_reader import ConfigReader


class BasePage:
    LANG_COOKIE_NAME = "Steam_Language"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver, ConfigReader.get_timeout()
        )

    def set_page_language(self, language):
        self.driver.delete_cookie(self.LANG_COOKIE_NAME)
        self.driver.add_cookie(
            {
                "name": self.LANG_COOKIE_NAME,
                "value": language
            }
        )
