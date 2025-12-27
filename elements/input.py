from selenium.common import WebDriverException

from elements.base_element import BaseElement
from src.logger.logger import Logger


class Input(BaseElement):
    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear {element}")
        try:
            element.clear()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def js_clear(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js clear {element}")
        self.browser.execute_script(
            "arguments[0].value = ''",
            element
        )

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()

        element = self.wait_for_visible()
        Logger.info(f"{self}: send keys [{keys}]")
        try:
            element.send_keys(keys)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def js_send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.js_clear()

        element = self.wait_for_presence()
        Logger.info(f"{self}: send keys [{keys}]")
        self.browser.execute_script(
            "arguments[0].value = arguments[1]",
            element,
            keys
        )
