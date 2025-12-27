import os

import dotenv
import pytest

from pages.the_internet_app.auth_page import AuthPage

dotenv.load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = "the-internet.herokuapp.com/basic_auth"


@pytest.mark.parametrize(
    "expected_result",
    [
        "Congratulations! You must have the proper credentials."
    ]
)
def test_basic_auth(browser, expected_result):
    auth_page = AuthPage(browser)
    auth_url = f"http://{LOGIN}:{PASSWORD}@{BASE_URL}"

    browser.get(auth_url)

    auth_page.wait_for_open()

    actual_result = auth_page.get_notification_text()

    assert expected_result == actual_result, (
        f"Ожидалось: {expected_result} \n Получено: {actual_result}"
    )
