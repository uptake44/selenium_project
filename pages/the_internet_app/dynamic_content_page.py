from tenacity import retry, wait_fixed, stop_after_delay, retry_if_result

from elements.label import Label
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    RETRY_TIMEOUT = 15
    RETRY_WAIT = 0.5

    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'columns')]//img"
    IMAGES_MULTI_WEB_ELEMENT_LOC = "(//div[contains(@class, 'columns')]//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Dynamic Content Page -> Main Label"
        )

        self.images_multi_web_element = MultiWebElement(
            self.browser,
            self.IMAGES_MULTI_WEB_ELEMENT_LOC,
            description="Dynamic Content Page -> Image Elements",
            timeout=0
        )

    def _has_duplicates(self) -> bool:
        images = [
            img.get_attribute("src")
            for img in self.images_multi_web_element
        ]
        return len(set(images)) != len(images)

    @retry(
        stop=stop_after_delay(RETRY_TIMEOUT),
        wait=wait_fixed(RETRY_WAIT),
        retry=retry_if_result(lambda result: result is False),
        retry_error_callback=lambda last_value: last_value.outcome.result(),
    )
    def check_duplicates(self) -> bool:
        if not self._has_duplicates():
            self.browser.refresh()
            return False

        return True
