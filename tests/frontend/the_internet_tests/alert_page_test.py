import pytest
from faker import Faker

from pages.the_internet_app.alert_page import AlertPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/javascript_alerts"

fake = Faker()


def test_open_alert_page_test(browser):
    alert_page = AlertPage(browser)
    browser.get(BASE_URL)
    alert_page.wait_for_open()


@pytest.mark.parametrize(
    "expected_alert_text, expected_result_text, use_js",
    [
        pytest.param(
            "I am a JS Alert",
            "You successfully clicked an alert",
            False,
            id="normal_click"

        ),
        pytest.param(
            "I am a JS Alert",
            "You successfully clicked an alert",
            True,
            id="js_click"
        )
    ]
)
def test_alert(
        browser,
        expected_alert_text,
        expected_result_text,
        use_js
):
    alert_page = AlertPage(browser)
    browser.get(BASE_URL)
    alert_page.wait_for_open()

    if use_js:
        alert_page.click_alert_button_js()
    else:
        alert_page.click_alert_button()

    actual_alert_text = browser.get_alert_text()
    assert expected_alert_text == actual_alert_text, (
        f"Ожидалось: {expected_alert_text} \n"
        f"Получено: {actual_alert_text}"
    )
    browser.confirm_alert()
    browser.wait_alert_not_present()

    actual_result_text = alert_page.get_result_text()
    assert expected_result_text == actual_result_text, (
        f"Ожидалось: {expected_result_text} \n"
        f"Получено: {actual_result_text}"
    )


@pytest.mark.parametrize(
    "expected_alert_text, expected_result_text, use_js",
    [
        pytest.param(
            "I am a JS Confirm",
            "You clicked: Ok",
            False,
            id="normal_click"
        ),
        pytest.param(
            "I am a JS Confirm",
            "You clicked: Ok",
            True,
            id="js_click"
        )
    ]
)
def test_confirm_alert(
        browser, expected_alert_text,
        expected_result_text,
        use_js
):
    alert_page = AlertPage(browser)
    browser.get(BASE_URL)
    alert_page.wait_for_open()

    if use_js:
        alert_page.click_confirm_button_js()
    else:
        alert_page.click_confirm_button()

    actual_alert_text = browser.get_alert_text()
    assert expected_alert_text == actual_alert_text, (
        f"Ожидалось: {expected_alert_text} \n"
        f"Получено: {actual_alert_text}"
    )

    browser.confirm_alert()
    browser.wait_alert_not_present()

    actual_result_text = alert_page.get_result_text()
    assert expected_result_text == actual_result_text, (
        f"Ожидалось: {expected_result_text} \n"
        f"Получено: {actual_result_text}"
    )


@pytest.mark.parametrize(
    "expected_alert_text, expected_result_text, use_js",
    [
        pytest.param(
            "I am a JS prompt",
            fake.sentence(),
            False,
            id="normal_click"
        ),
        pytest.param(
            "I am a JS prompt",
            fake.sentence(),
            True,
            id="js_click"
        )
    ]
)
def test_prompt_alert(
        browser,
        expected_alert_text,
        expected_result_text,
        use_js
):
    alert_page = AlertPage(browser)
    browser.get(BASE_URL)
    alert_page.wait_for_open()

    if use_js:
        alert_page.click_prompt_button_js()
    else:
        alert_page.click_prompt_button()

    actual_alert_text = browser.get_alert_text()
    assert actual_alert_text == expected_alert_text, (
        f"Ожидалось: {expected_alert_text} \n"
        f"Получено: {actual_alert_text}"
    )

    browser.send_keys_alert(expected_result_text)
    browser.confirm_alert()
    browser.wait_alert_not_present()

    actual_result_text = alert_page.get_result_text()
    assert actual_result_text.endswith(expected_result_text), (
        f"Ожидалось {expected_result_text} в {actual_result_text}\n"
    )
