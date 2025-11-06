from faker import Faker

from base.base_test import BaseTest


class TestLogin(BaseTest):
    PASSWORD_LENGTH = 8

    def test_login(self, driver):
        fake = Faker()
        self.login_page.open()
        self.login_page.enter_login(fake.user_name())
        self.login_page.enter_password(fake.password(self.PASSWORD_LENGTH))
        self.login_page.click_submit_button()
        self.login_page.login_error_displayed()