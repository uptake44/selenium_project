import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from src.config.config_reader import ConfigReader


@pytest.mark.parametrize(
    "search_value, items_in_list",
    [
        ("The Witcher", 10),
        ("Fallout", 20)
    ]
)
def test_search(driver, search_value: str, items_in_list: int):
    main_page = MainPage(driver)
    search_page = SearchPage(driver)

    driver.get(ConfigReader.get_url())
    assert main_page.is_page_opened(), "Домашняя страница не открылась"
    main_page.search(search_value)
    assert search_page.is_page_opened(), "Страница поиска не открылась"

    search_page.set_filters()

    actual_prices = search_page.get_item_price_list(items_in_list)
    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices, (
        f"Ожидалось: {expected_prices}\n"
        f"Получено: {actual_prices}"
    )
