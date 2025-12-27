from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoverPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'figure')]"

    USER_PROFILE_ELEMENT_LOC = "//div[contains(@class, 'figure')][{}]"
    USER_NAME_ELEMENT_LOC = "(//*[contains(text(), 'name:')])[{}]"
    PROFILE_BUTTON_ELEMENT_LOC = "(//div[contains(@class, 'figcaption')]//a)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hover Page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Hover Page -> User Image Figure"
        )

        self.profiles_multi_element = MultiWebElement(
            self.browser,
            self.USER_PROFILE_ELEMENT_LOC,
            description="Hover Page -> User Profile Image",
            timeout=0
        )

        self.user_name_element = MultiWebElement(
            self.browser,
            self.USER_NAME_ELEMENT_LOC,
            description="Hover User Profile -> User Name",
            timeout=0
        )

        self.user_profile_button = MultiWebElement(
            self.browser,
            self.PROFILE_BUTTON_ELEMENT_LOC,
            description="Hover User Profile -> View Profile Button",
            timeout=0
        )

    def hover_profile(self, index: int):
        self.profiles_multi_element[index].hover_element()

    def get_user_name(self, index: int) -> str:
        return self.user_name_element[index].get_text()

    def get_profile_link(self, index: int) -> str:
        return self.user_profile_button[index].get_attribute("href")

    def click_profile_button(self, index: int):
        self.user_profile_button[index].click()
