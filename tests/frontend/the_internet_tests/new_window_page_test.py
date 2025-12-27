import pytest

from pages.the_internet_app.new_window_page import NewWindowPage
from pages.the_internet_app.windows_page import WindowsPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/windows"


@pytest.mark.parametrize(
    "expected",
    [
        "New Window"
    ]
)
def test_new_window(browser, expected) -> None:
    windows_page = WindowsPage(browser)
    new_window_page = NewWindowPage(browser)

    def open_new_tab() -> tuple[str, str]:
        windows_page.click_new_page_button()
        browser.switch_to_new_tab()
        return new_window_page.get_label_text(), browser.get_title()

    browser.get(BASE_URL)
    windows_page.wait_for_open()

    actual_label, actual_title = open_new_tab()

    assert actual_label == expected, (
        f"Ожидалось: {expected}\n"
        f"Получено: {actual_label}"
    )

    assert actual_title == expected, (
        f"Ожидалось: {expected}\n"
        f"Получено: {actual_title}"
    )

    browser.switch_to_default_window()
    windows_page.wait_for_open()

    actual_label, actual_title = open_new_tab()

    assert actual_label == expected, (
        f"Ожидалось: {expected}\n"
        f"Получено: {actual_label}"
    )

    assert actual_title == expected, (
        f"Ожидалось: {expected}\n"
        f"Получено: {actual_title}"
    )

    browser.switch_to_default_window()

    browser.close_other_tabs()
