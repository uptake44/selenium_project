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
    ERROR_ELEMENT = (
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

        self.wait.until(
            ec.element_to_be_clickable(self.LOGIN_BTN)
        )

    def get_error_text(self) -> str | None:
        self.wait.until(
            lambda d: d.find_element(
                *self.ERROR_ELEMENT
            ).text.strip() != ""
        )
        try:
            return self.wait.until(
                ec.presence_of_element_located(self.ERROR_ELEMENT)
            ).text
        except TimeoutException:
            return None
