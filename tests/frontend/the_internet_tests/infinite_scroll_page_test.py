import pytest

from pages.the_internet_app.infinite_scroll_page import InfiniteScrollPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/infinite_scroll"


@pytest.mark.parametrize(
    "target_sections",
    [
        23
    ]
)
def test_infinite_scroll(browser, target_sections):
    infinite_scroll_page = InfiniteScrollPage(browser)
    browser.get(BASE_URL)
    infinite_scroll_page.wait_for_open()

    infinite_scroll_page.scroll_sections(target_sections)
    actual_sections = infinite_scroll_page.get_sections_number()

    assert actual_sections == target_sections, (
        f"Получено: {actual_sections}\n"
        f"Ожидалось: {target_sections}"
    )
