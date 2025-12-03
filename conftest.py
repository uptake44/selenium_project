import pytest

from src.config.config_reader import Language, ConfigReader
from src.drivers.chrome_driver import ChromeDriver


@pytest.fixture()
def language(request):
    if hasattr(request, 'param'):
        return request.param
    return Language.RUS


@pytest.fixture()
def driver(language):
    browser = ChromeDriver()

    browser.get(ConfigReader.get_url())

    browser.delete_cookie(ConfigReader.get_lang_cookie())

    browser.add_cookie({
        "name": ConfigReader.get_lang_cookie(),
        "value": language,
    })

    yield browser
    ChromeDriver.quit_driver()
