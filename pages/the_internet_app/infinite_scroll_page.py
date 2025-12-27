from tenacity import retry, stop_after_attempt, wait_fixed

from elements.label import Label
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class SectionsNotLoaded(Exception):
    pass


class InfiniteScrollPage(BasePage):
    MAX_ATTEMPTS = 60
    WAIT_TIMEOUT = 0.2

    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'added')]//br"

    SECTIONS_MULTI_WEB_ELEMENT_LOC = "//div[contains(@class, 'added')][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinite Scroll Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Infinite Scroll Page -> Paragraph",
        )

        self.sections_multi_web_element = MultiWebElement(
            self.browser,
            self.SECTIONS_MULTI_WEB_ELEMENT_LOC,
            description="Infinite Scroll Page -> Sections",
            timeout=0
        )

    def get_sections_number(self) -> int:
        return len([
            section
            for section in self.sections_multi_web_element
        ])

    @retry(
        stop=stop_after_attempt(MAX_ATTEMPTS),
        wait=wait_fixed(WAIT_TIMEOUT),
        reraise=True,
    )
    def scroll_sections(self, target: int) -> None:
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        if self.get_sections_number() == target:
            return
        raise SectionsNotLoaded(
            f"Элементы не загрузились за {self.MAX_ATTEMPTS} попыток"
        )
