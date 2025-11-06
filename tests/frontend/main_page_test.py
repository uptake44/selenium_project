from base.base_test import BaseTest


class TestMainPage(BaseTest):

    def test_login_button(self, driver):
        self.main_page.open()
        self.main_page.click_login_page_button()
        self.main_page.login_page_is_opened()