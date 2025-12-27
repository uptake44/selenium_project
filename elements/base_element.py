from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.config.config_reader import ConfigReader
from src.drivers.browser.browser import Browser
from src.logger.logger import Logger


class BaseElement:
    DEFAULT_TIMEOUT = ConfigReader.get_default_timeout()

    def __init__(
            self,
            browser: Browser,
            locator: tuple | str,
            description: str | None = None,
            timeout: int = DEFAULT_TIMEOUT
    ):
        self.browser = browser
        self.timeout = timeout

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)

        self._wait = WebDriverWait(
            self.browser.driver,
            timeout=self.timeout
        )

        self._action = ActionChains(self.browser.driver)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(
                f"{self}: wait for {expected_condition.__name__}"
            )
            element = self._wait.until(
                method=expected_condition(self.locator)
            )
            return element
        except TimeoutException as e:
            Logger.error(f"{self}: {e}")
            raise

    def _wait_for_not(self, expected_condition) -> WebElement:
        try:
            Logger.info(
                f"{self}: wait for not {expected_condition.__name__}"
            )
            element = self._wait.until_not(
                method=expected_condition(self.locator)
            )
            return element
        except TimeoutException as e:
            Logger.error(f"{self}: {e}")
            raise

    def is_exists(self) -> bool:
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(
            expected_condition=ec.presence_of_element_located
        )

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(
            expected_condition=ec.element_to_be_clickable
        )

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(
            expected_condition=ec.visibility_of_element_located
        )

    def click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def js_click(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();",
            element
        )

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get text")
        try:
            text = element.text
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise
        Logger.info(f"{self}: text = '{text}'")
        return text

    def get_attribute(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get attribute '{name}'")
        try:
            value = element.get_attribute(name)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def get_css_property(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get css property '{name}'")
        try:
            value = element.value_of_css_property(name)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise
        Logger.info(f"{self}: css property '{name}' = '{value}'")
        return value

    def double_click(self):
        element = self.wait_for_clickable()
        Logger.info(f"{self}: double click")
        try:
            self._action.double_click(element).perform()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def context_click(self):
        element = self.wait_for_visible()
        Logger.info(f"{self}: context click")
        try:
            self._action.context_click(element).perform()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def hover_element(self):
        element = self.wait_for_visible()
        Logger.info(f"{self}: hover element")
        try:
            self._action.move_to_element(element).perform()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise
