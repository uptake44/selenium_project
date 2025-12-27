from pages.the_internet_app.context_menu_page import ContextMenuPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/context_menu"

def test_context_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    browser.get(BASE_URL)
    context_menu_page.wait_for_open()

    context_menu_page.right_click_context_box()
    browser.confirm_alert()
    browser.wait_alert_not_present()
