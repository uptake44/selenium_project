from faker import Faker

PASSWORD_LENGTH = 8
fake = Faker()


def test_login_invalid_creds(driver, login_page):
    login_page.open(login_page.PAGE_URL)
    login_page.login(username=fake.user_name(), password=fake.password(PASSWORD_LENGTH))
    assert login_page.is_login_error_present()