from faker import Faker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('incognito')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, 1)
fake = Faker()

TARGET_URL = "https://store.steampowered.com/"
LOGIN_PAGE_BUTTON = (
    "xpath",
    "//a[contains(@class, 'global_action_link')]"
)
LOGIN_INPUT = (
    "xpath",
    "//form[contains(@class, '_2v60tM463fW0V7GDe92E5f')]//input[@type='text']"
)
PASSWORD_INPUT = (
    "xpath",
    "//input[@type='password']"
)
SUBMIT_BUTTON = (
    "xpath",
    "//button[contains(@class, 'DjSvCZoKKfoNSmarsEcTS')]"
)
LOGIN_FAILED_ELEMENT = (
    "xpath",
    "//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]"
)

driver.get(TARGET_URL)

wait.until(EC.element_to_be_clickable(LOGIN_PAGE_BUTTON)).click()

login_field = wait.until(
    EC.visibility_of_element_located(LOGIN_INPUT)
)
password_field = wait.until(
    EC.visibility_of_element_located(PASSWORD_INPUT)
)

login_field.send_keys(fake.user_name())
password_field.send_keys(fake.password(length=8))

driver.find_element(*SUBMIT_BUTTON).click()

wait.until(lambda d: d.find_element(*LOGIN_FAILED_ELEMENT).text != '')
