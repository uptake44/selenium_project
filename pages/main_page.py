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