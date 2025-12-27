from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = "result"
    JS_ALERT_LOC = "//button[@onclick='jsAlert()']"
    JS_CONFIRM_LOC = "//button[@onclick='jsConfirm()']"
    JS_PROMPT_LOC = "//button[@onclick='jsPrompt()']"
    RESULT_ELEMENT_LOC = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Alert Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Alert Page -> Alert Result"
        )

        self.alert_button_element = Button(
            self.browser,
            self.JS_ALERT_LOC,
            description="Alert Page -> JS Alert Button"
        )

        self.confirm_button_element = Button(
            self.browser,
            self.JS_CONFIRM_LOC,
            description="Alert Page -> JS Confirm Button"
        )

        self.prompt_button_element = Button(
            self.browser,
            self.JS_PROMPT_LOC,
            description="Alert Page -> JS Prompt Button"
        )

        self.result_element = Label(
            self.browser,
            self.RESULT_ELEMENT_LOC,
            description="Alert Page -> Alert Button -> Result Label"
        )

    def click_alert_button(self) -> None:
        self.alert_button_element.click()

    def click_alert_button_js(self):
        self.alert_button_element.js_click()

    def click_confirm_button(self) -> None:
        self.confirm_button_element.click()

    def click_confirm_button_js(self) -> None:
        self.confirm_button_element.js_click()

    def click_prompt_button(self) -> None:
        return self.prompt_button_element.click()

    def click_prompt_button_js(self) -> None:
        return self.prompt_button_element.js_click()

    def get_result_text(self) -> str:
        return self.result_element.get_text()