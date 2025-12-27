from elements.label import Label
from elements.slider import Slider
from pages.base_page import BasePage


class SliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "range"
    INDICATOR_ELEMENT_LOC = "range"
    SLIDER_ELEMENT_LOC = "//input[@type='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Slider Page"
        self.unique_element = Slider(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Slider Page -> Slider Label"
        )

        self.slider_element = Slider(
            self.browser,
            self.SLIDER_ELEMENT_LOC,
            description="Slider Page -> Slider Input"
        )

        self.indicator_element = Label(
            self.browser,
            self.INDICATOR_ELEMENT_LOC,
            description="Slider Page -> Slider Slider Label"
        )

    def move_slider(self, presses: int) -> None:
        self.slider_element.move(presses)

    def get_indicator_value(self) -> float:
        return float(self.indicator_element.get_text())

    def get_max_value(self) -> float:
        return self.slider_element.get_max_value()

    def get_min_value(self) -> float:
        return self.slider_element.get_min_value()

    def get_step_value(self) -> float:
        return self.slider_element.get_step_value()
