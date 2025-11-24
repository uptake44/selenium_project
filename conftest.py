import pytest

from src.drivers.chrome_driver import ChromeDriver


@pytest.fixture()
def driver():
    browser = ChromeDriver()
    yield browser
    ChromeDriver.quit_driver()
