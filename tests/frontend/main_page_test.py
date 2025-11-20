from pages.login_page import LoginPage
from pages.main_page import MainPage
from src.config.config_reader import ConfigReader


def test_navigate_to_main_page(driver):
    main_page = MainPage(driver)

    driver.get(ConfigReader.get_url())
    assert main_page.is_page_opened(), "Ошибка загрузки страницы"

def test_click_login_button(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    driver.get(ConfigReader.get_url())
    main_page.click_login_button()

    assert login_page.is_page_opened(), "Ошибка загрузки страницы"
