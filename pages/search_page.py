from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from src.config.config_reader import ConfigReader


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
    LOADING_ELEMENT = (
        By.XPATH,
        "//*[@id='search_result_container' and contains(@style, 'opacity')]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(
            driver,
            ConfigReader.get_timeout(),
            ConfigReader.get_poll_frequency()
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

        self.wait.until(
            ec.presence_of_element_located(self.LOADING_ELEMENT)
        )

        self.wait.until_not(
            ec.presence_of_element_located(self.LOADING_ELEMENT)
        )

    def get_item_price_list(self, value) -> list:
        elements = self.wait.until(
            ec.presence_of_all_elements_located(self.PRICE_ELEMENT)
        )
        return [
            int(el.get_attribute("data-price-final"))
            for el in elements[:value]
        ]
