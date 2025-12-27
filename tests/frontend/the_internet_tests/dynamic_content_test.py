from pages.the_internet_app.dynamic_content_page import DynamicContentPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/dynamic_content"


def test_duplicated_images(browser):
    dynamic_content = DynamicContentPage(browser)
    browser.get(BASE_URL)

    dynamic_content.wait_for_open()

    assert dynamic_content.check_duplicates(), "Дубликаты не найдены"
