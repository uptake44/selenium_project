from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIMEOUT)
