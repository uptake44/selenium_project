from typing import Optional

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class MainPage(BasePage):
    UNIQUE_ELEMENT = (
        By.ID,
        "home_specialoffers"
    )
    LOGIN_PAGE_BTN = (
        By.XPATH,
        "//a[contains(@class, 'global_action_link')]"
    )
    SEARCH_FIELD = (
        By.NAME,
        "term"
    )
    SEARCH_BTN = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def is_page_opened(self):
        try:
            self.wait.until(
                ec.visibility_of_element_located(
                    self.UNIQUE_ELEMENT
                )
            )
            return True
        except TimeoutException:
            return False

    def click_login_button(self):
        self.wait.until(
            ec.element_to_be_clickable(self.LOGIN_PAGE_BTN)
        ).click()

    def search(self, value: Optional[str] = None):
        if value:
            self.wait.until(
                ec.element_to_be_clickable(self.SEARCH_FIELD)
            ).send_keys(value)
        self.wait.until(
            ec.element_to_be_clickable(self.SEARCH_BTN)
        ).click()
