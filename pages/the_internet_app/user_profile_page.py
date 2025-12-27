from elements.label import Label
from pages.base_page import BasePage


class UserProfilePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[text()='Not Found']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "User Profile Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="User Profile Page -> Main Label"
        )
