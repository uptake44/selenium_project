import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config_reader import ConfigReader


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument(ConfigReader.get_options())
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
