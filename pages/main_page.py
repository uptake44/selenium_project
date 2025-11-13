from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators:
    UNIQUE_ELEMENT = (
        By.XPATH,
        "//*[@id='home_takeunder_ctn']"
    )
    LOGIN_PAGE_BTN = (
        By.XPATH,
        "//a[contains(@class, 'global_action_link')]"
    )


class MainPage(BasePage):
    PAGE_URL = "https://store.steampowered.com"
