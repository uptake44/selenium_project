from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.config.config_reader import ConfigReader
from src.drivers.browser.browser_factory import BrowserFactory, BrowserType
from src.logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = ConfigReader.get_default_timeout()
    PAGE_LOAD_TIMEOUT = ConfigReader.get_page_load_timeout()

    def __init__(self, browser_type: BrowserType):
        self._driver = BrowserFactory.get_driver(browser_type)

        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        self._wait = WebDriverWait(
            self._driver,
            timeout=self.DEFAULT_TIMEOUT,
        )

        self.main_handle = None

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url) -> None:
        Logger.info(f"{self}: get {url}")
        try:
            self._driver.get(url)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise
        self.main_handle = self._driver.current_window_handle

    def back(self) -> None:
        Logger.info(f"{self}: back")
        self._driver.back()

    def forward(self) -> None:
        Logger.info(f"{self}: forward")
        self._driver.forward()

    def refresh(self) -> None:
        Logger.info(f"{self}: refresh")
        self._driver.refresh()

    def close(self) -> None:
        Logger.info(
            f"{self}: close window handle = "
            f"{self._driver.current_window_handle}"
        )
        self._driver.close()

    def quit(self) -> None:
        Logger.info(f"{self}: quit driver")
        try:
            self._driver.quit()
        except WebDriverException() as e:
            Logger.error(f"{self}: {e}")
            raise

    def wait_alert_present(self):
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(ec.alert_is_present())

    def wait_alert_not_present(self):
        try:
            Logger.info(f"{self}: wait alert not present")
            return self._wait.until_not(ec.alert_is_present())
        except TimeoutException as e:
            Logger.error(f"{self}: {e}")
            raise

    def switch_to_alert(self):
        Logger.info(f"{self}: switch to alert")
        self.wait_alert_present()
        return self._driver.switch_to.alert

    def confirm_alert(self) -> None:
        Logger.info(f"{self}: confirm alert")
        self.switch_to_alert().accept()

    def dismiss_alert(self) -> None:
        Logger.info(f"{self}: dismiss alert")
        self.switch_to_alert().dismiss()

    def get_alert_text(self) -> str:
        Logger.info(f"{self}: get alert text")
        return self.switch_to_alert().text

    def send_keys_alert(self, text: str) -> None:
        Logger.info(f"{self}: alert send keys: {text}")
        self.switch_to_alert().send_keys(text)

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script [{script}] with args = {args}")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def take_screenshot(self, filename: str) -> None:
        Logger.info(f"{self}: take screenshot")
        try:
            self._driver.save_screenshot(filename=filename)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def switch_to_frame(self, frame) -> None:
        Logger.info(f"{self}: switch to iframe")
        return self._driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_default_content(self) -> None:
        Logger.info(f"{self}: switch to default content")
        self._driver.switch_to.default_content()

    def switch_to_default_window(self) -> None:
        Logger.info(f"{self}: switch to default window")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def switch_to_new_tab(self) -> None:
        Logger.info(f"{self}: switch to new tab")

        tabs = self._driver.window_handles
        if self.main_handle is None:
            err = f"{self}: main handle is None"
            Logger.error(err)
            raise WebDriverException(err)
        elif not tabs:
            err = f"{self}: no available tabs to switch"
            Logger.error(err)
            raise WebDriverException(err)
        elif len(tabs) < 2:
            err = f"{self}: only main tab available"
            Logger.error(err)
            raise WebDriverException(err)

        try:
            self._driver.switch_to.window(tabs[-1])
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def close_new_tab(self) -> None:
        Logger.info(f"{self}: close new tab")

        if self.main_handle is None:
            Logger.error(f"{self}: main handle is None")
            raise WebDriverException

        try:
            self.switch_to_new_tab()
            self.close()
            self.switch_to_default_window()
        except WebDriverException as e:
            Logger.error(f"{self}: {e}")
            raise

    def close_other_tabs(self) -> None:
        Logger.info(f"{self}: close other tabs")

        if self.main_handle is None:
            Logger.error(f"{self}: main handle is None")
            raise WebDriverException
        tabs = self._driver.window_handles

        if len(tabs) < 2:
            Logger.error(f"{self}: single tab is opened, unable to close")
            raise WebDriverException

        for tab in tabs:
            if tab != self.main_handle:
                self._driver.switch_to.window(tab)
                self.close()

        self.switch_to_default_window()

    def get_title(self) -> str:
        Logger.info(f"{self}: get title")
        return self._driver.title

    def get_url(self) -> str:
        Logger.info(f"{self}: get url")
        return self._driver.current_url
