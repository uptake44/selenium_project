from typing import Optional

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_INPUT = (
        By.XPATH,
        "//*[@data-featuretarget='login']//input[@type='text']"
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )
    LOGIN_BTN = (
        By.XPATH,
        "//*[@data-featuretarget='login']//button"
    )
    INVALID_CREDENTIALS_ERROR = (
        By.XPATH,
        "//*[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]"
    )


class LoginPage(BasePage):
    PAGE_URL = "https://store.steampowered.com/login"
    FAILED_LOGIN_TEXT = (
        "Пожалуйста, "
        "проверьте свой пароль и имя "
        "аккаунта и попробуйте снова."
    )

    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        if username:
            self.fill_form(
                selector=LoginPageLocators.LOGIN_INPUT,
                value=username
            )
        if password:
            self.fill_form(
                selector=LoginPageLocators.PASSWORD_INPUT,
                value=password
            )
        self.click(LoginPageLocators.LOGIN_BTN)

    def is_login_error_present(self) -> bool:
        try:
            self.wait.until(
                EC.text_to_be_present_in_element(
                    LoginPageLocators.INVALID_CREDENTIALS_ERROR,
                    self.FAILED_LOGIN_TEXT
                )
            )
            return True
        except TimeoutException:
            return False
