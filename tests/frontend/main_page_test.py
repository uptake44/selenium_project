from pages.login_page import LoginPageLocators
from pages.main_page import MainPage, MainPageLocators


def test_navigate_to_main_page(driver, main_page):
    driver.get(MainPage.PAGE_URL)
    assert main_page.is_element_present(
        selector=MainPageLocators.UNIQUE_ELEMENT
    ), "Главная страница не открылась"


def test_click_login_button(driver, main_page, login_page):
    main_page.open(MainPage.PAGE_URL)
    main_page.click(MainPageLocators.LOGIN_PAGE_BTN)
    assert login_page.is_element_present(
        LoginPageLocators.PASSWORD_INPUT
    ), "Не удалось перейти на страницу логина"
