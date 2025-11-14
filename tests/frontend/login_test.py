import pytest
from faker import Faker

from pages.login_page import LoginPage

PASSWORD_LENGTH = 8
fake = Faker()


@pytest.mark.parametrize(
    "error_text",
    [
        ("Пожалуйста, проверьте свой "
         "пароль и имя аккаунта "
         "и попробуйте снова."),
    ]
)
def test_login_error(driver, error_text: str):
    login_page = LoginPage(driver)
    driver.get("https://store.steampowered.com/login")
    login_page.login(
        username=fake.user_name(),
        password=fake.password(PASSWORD_LENGTH)
    )
    assert login_page.is_error_present(error_text), (
        f"Ошибка {error_text} не найдена"
    )
