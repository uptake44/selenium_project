from elements.label import Label
from pages.base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//*[text()='New Window']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New Window Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="New Window Page -> Label"
        )

        self.new_page_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="New Window Page -> Label"
        )

    def get_label_text(self) -> str:
        return self.new_page_element.get_text()
