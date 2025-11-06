from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from base.base_page import BasePage

LOGIN_PAGE_BUTTON = (
    By.XPATH,
    "//a[contains(@class, 'global_action_link')]"
)
PAGE_URL = Links.HOST


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(PAGE_URL)

    def click_login_page_button(self):
        self.wait.until(
            EC.element_to_be_clickable(LOGIN_PAGE_BUTTON)
        ).click()

    def login_page_is_opened(self):
        self.wait.until(EC.url_contains("/login"))
