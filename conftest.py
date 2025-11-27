import pytest

from src.config.config_reader import ConfigReader
# from src.config.config_reader import ConfigReader
from src.drivers.chrome_driver import ChromeDriver


@pytest.fixture(
    params=ConfigReader.get_languages()
)
def driver(request):
    browser = ChromeDriver(request.param)
    yield browser
    ChromeDriver.quit_driver()
