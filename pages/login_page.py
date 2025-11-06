from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from base.base_page import BasePage

PAGE_URL = Links.LOGIN_PAGE
LOGIN_FIELD = (
    By.XPATH,
    "//*[@data-featuretarget='login']//input[@type='text']"
)
PASSWORD_FIELD = (
    By.XPATH,
    "//input[@type='password']"
)
SUBMIT_BUTTON = (
    By.XPATH,
    "//*[@data-featuretarget='login']//button"
)
LOGIN_FAILED_ELEMENT = (
    By.XPATH,
    "//div[contains(text(), 'Пожалуйста, проверьте')]"
)
FAILED_LOGIN_TEXT = (
    "Пожалуйста, "
    "проверьте свой пароль и имя "
    "аккаунта и попробуйте снова."
)


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(PAGE_URL)

    def enter_login(self, login):
        self.wait.until(
            EC.element_to_be_clickable(LOGIN_FIELD)
        ).send_keys(login)

    def enter_password(self, password):
        self.wait.until(
            EC.element_to_be_clickable(PASSWORD_FIELD)
        ).send_keys(password)

    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable(SUBMIT_BUTTON)
        ).click()

    def login_error_displayed(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                LOGIN_FAILED_ELEMENT, FAILED_LOGIN_TEXT
            )
        )
