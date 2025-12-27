from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class AuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "content"
    SUCCESS_NOTIFICATION_LOC = "//div[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Auth page"

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Auth Modal -> Auth Page"
        )

        self.success_notification_element = Label(
            self.browser,
            self.SUCCESS_NOTIFICATION_LOC,
            description="Auth Page -> Auth Label"
        )

    def get_notification_text(self) -> str:
        return self.success_notification_element.get_text().strip()
