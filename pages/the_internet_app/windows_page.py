from elements.button import Button
from pages.base_page import BasePage


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//a[contains(@href, '/windows/new')]"
    NEW_PAGE_ELEMENT = "//a[contains(@href, '/windows/new')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows Page"
        self.unique_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Windows Page -> Click Here Button"
        )

        self.new_page_button = Button(
            self.browser,
            self.NEW_PAGE_ELEMENT,
            description="New Page -> Click Here Button"
        )

    def click_new_page_button(self) -> None:
        self.new_page_button.click()