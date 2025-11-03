from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

target_url = "https://store.steampowered.com/"

driver.get(target_url)

# Кнопка со страницей скидок (2 из 4)
specials_button = driver.find_elements('xpath', "//a[contains(@class, 'big_button')]")[1]
specials_button.click()
