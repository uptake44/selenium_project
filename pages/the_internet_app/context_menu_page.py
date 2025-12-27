from elements.button import Button
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "ContextMenuPage"

        self.unique_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="ContextMenuPage > Context Box"
        )

        self.context_box_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="ContextMenuPage > Context Box"
        )

    def right_click_context_box(self) -> None:
        self.context_box_element.context_click()