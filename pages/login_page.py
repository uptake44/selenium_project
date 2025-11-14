from typing import Optional

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class LoginPage(BasePage):
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
        "//div[contains(@class, 'tool-tip-source')]/following::div[2]"
    )

    def is_page_opened(self):
        try:
            self.wait.until(
                ec.presence_of_element_located(
                    self.PASSWORD_INPUT
                )
            )
            return True
        except TimeoutException:
            return False

    def login(
            self,
            username: Optional[str] = None,
            password: Optional[str] = None
    ):
        if username:
            self.wait.until(
                ec.element_to_be_clickable(self.LOGIN_INPUT)
            ).send_keys(username)

        if password:
            self.wait.until(
                ec.element_to_be_clickable(self.PASSWORD_INPUT)
            ).send_keys(username)

        self.wait.until(
            ec.element_to_be_clickable(self.LOGIN_BTN)
        ).click()

    def is_error_present(self, error_text: str) -> bool:
        try:
            self.wait.until(
                ec.text_to_be_present_in_element(
                    self.INVALID_CREDENTIALS_ERROR,
                    error_text
                )
            )
            return True
        except TimeoutException:
            return False
