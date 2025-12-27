import pytest

from src.drivers.browser.browser import Browser
from src.drivers.browser.browser_factory import BrowserType


@pytest.fixture()
def browser():
    chrome_driver = Browser(BrowserType.CHROME)

    yield chrome_driver

    chrome_driver.quit()
