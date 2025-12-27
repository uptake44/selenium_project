from selenium.common import WebDriverException
from selenium.webdriver.common.keys import Keys

from elements.base_element import BaseElement
from src.logger.logger import Logger


class Slider(BaseElement):
    def move(self, presses: int) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: move slider [{presses}] times")
        try:
            self._action.click(element) \
                .send_keys(Keys.HOME) \
                .send_keys(Keys.RIGHT * presses) \
                .perform()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def get_max_value(self) -> float:
        return float(self.get_attribute("max"))

    def get_min_value(self) -> float:
        return float(self.get_attribute("min"))

    def get_step_value(self) -> float:
        return float(self.get_attribute("step"))