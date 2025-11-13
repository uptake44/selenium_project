import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--lang=ru-RU')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver) -> MainPage:
    return MainPage(driver)


@pytest.fixture()
def login_page(driver) -> LoginPage:
    return LoginPage(driver)
