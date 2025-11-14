from pages.login_page import LoginPage
from pages.main_page import MainPage


PAGE_URL = "https://store.steampowered.com/"

def test_navigate_to_main_page(driver):
    main_page = MainPage(driver)
    driver.get(PAGE_URL)
    assert main_page.is_page_opened(), "Ошибка загрузки страницы"

def test_click_login_button(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    driver.get(PAGE_URL)
    main_page.click_login_button()
    assert login_page.is_page_opened(), "Ошибка загрузки страницы"
