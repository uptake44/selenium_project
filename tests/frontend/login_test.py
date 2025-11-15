import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.main_page import MainPage

PASSWORD_LENGTH = 8
fake = Faker()
PAGE_URL = "https://store.steampowered.com"


@pytest.mark.parametrize(
    "expected_error",
    [
        ("Пожалуйста, проверьте свой "
         "пароль и имя аккаунта "
         "и попробуйте снова."),
    ]
)
def test_login_error(driver, expected_error: str):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    driver.get(PAGE_URL)
    main_page.click_login_button()
    login_page.login(
        username=fake.user_name(),
        password=fake.password(PASSWORD_LENGTH)
    )
    actual_error = login_page.get_error_text()
    assert actual_error == expected_error, (
        f"Ожидалось: '{expected_error}'\n"
        f"Получено: {actual_error}'"
    )
