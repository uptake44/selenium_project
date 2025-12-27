from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'text-center') and text()='Nested Frames']"

    PARENT_FRAME_LOC = "frame1"
    PARENT_FRAME_TEXT_LOC = "//body"

    CHILD_FRAME_LOC = "//iframe"
    CHILD_FRAME_TEXT_LOC = "//p"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Nested Frames Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Nested Frames -> Parent Frame"
        )

        self.parent_frame = WebElement(
            self.browser,
            self.PARENT_FRAME_LOC,
            description="Nested Frames -> Parent Frame"
        )

        self.parent_frame_text = Label(
            self.browser,
            self.PARENT_FRAME_TEXT_LOC,
            description="Parent Frame > Label"
        )

        self.child_frame = WebElement(
            self.browser,
            self.CHILD_FRAME_LOC,
            description="Parent Frame -> Child Frame"
        )

        self.child_frame_text = Label(
            self.browser,
            self.CHILD_FRAME_TEXT_LOC,
            description="Child Frame -> Label"
        )

    def _switch_to_parent_frame(self) -> None:
        self.browser.switch_to_default_content()
        self.browser.switch_to_frame(self.parent_frame)

    def get_parent_frame_text(self) -> str:
        self._switch_to_parent_frame()
        parent_text =  self.parent_frame_text.get_text()
        self.browser.switch_to_default_content()
        return parent_text

    def _switch_to_child_frame(self) -> None:
        self._switch_to_parent_frame()
        self.browser.switch_to_frame(self.child_frame)

    def get_child_frame_text(self) -> str:
        self._switch_to_child_frame()
        child_text = self.child_frame_text.get_text()
        self.browser.switch_to_default_content()
        return child_text
