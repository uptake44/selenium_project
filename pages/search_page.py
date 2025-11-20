from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_BY_TRIGGER = (
        By.ID,
        "sort_by_trigger"
    )
    SORT_DROPLIST = (
        By.ID,
        "sort_by_droplist"
    )
    SORT_PRICE_DESC = (
        By.ID,
        "Price_DESC"
    )
    SEARCH_RESULT = (
        By.ID,
        "search_resultsRows"
    )
    PRICE_ELEMENT = (
        By.XPATH,
        "//div[contains(@class, 'search_price_discount_combined')]"
    )

    def is_page_opened(self):
        try:
            self.wait.until(
                ec.visibility_of_element_located(self.SORT_BY_TRIGGER)
            )
            return True
        except TimeoutException:
            return False

    def set_filters(self):
        self.wait.until(
            ec.element_to_be_clickable(self.SORT_BY_TRIGGER)
        ).click()

        self.wait.until(
            ec.visibility_of_element_located(self.SORT_DROPLIST)
        )

        self.wait.until(
            ec.element_to_be_clickable(self.SORT_PRICE_DESC)
        ).click()

        element = self.wait.until(
            ec.presence_of_element_located(self.PRICE_ELEMENT)
        )
        self.wait.until(
            ec.staleness_of(element)
        )

    def get_item_price_list(self, value) -> list:
        elements = self.wait.until(
            ec.presence_of_all_elements_located(self.PRICE_ELEMENT)
        )
        return [
            int(el.get_attribute("data-price-final"))
            for el in elements[:value]
        ]
