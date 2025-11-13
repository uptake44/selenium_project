from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def is_element_present(self, selector: tuple[str, str]) -> bool:
        try:
            self.wait.until(
                EC.presence_of_element_located(selector)
            )
            return True
        except TimeoutException:
            return False

    def fill_form(self, selector: tuple[str, str], value: str) -> None:
        element = self.wait.until(
            EC.visibility_of_element_located(selector)
        )
        element.clear()
        element.send_keys(value)

    def click(self, selector: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(selector)).click()
