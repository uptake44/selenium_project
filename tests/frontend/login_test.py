import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.main_page import MainPage
from src.config.config_reader import ConfigReader

PASSWORD_LENGTH = 8
fake = Faker()


@pytest.mark.parametrize(
    "expected_error",
    [
        ("Пожалуйста, проверьте свой "
         "пароль и имя аккаунта "
         "и попробуйте снова."),

        ("Please check your "
         "password and account name "
         "and try again.")
    ]
)
def test_login_error(driver, expected_error: str):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    driver.get(ConfigReader.get_url())
    main_page.click_login_button()

    login_page.login(
        username=fake.user_name(),
        password=fake.password(PASSWORD_LENGTH)
    )
    actual_error = login_page.get_error_text()

    assert actual_error == expected_error, (
        f"Ожидалось: '{expected_error}'\n"
        f"Получено: {actual_error}"
    )
