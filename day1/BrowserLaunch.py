from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = "Chrome"
global driver

if browser == "Firefox":
    driver = Firefox(GeckoDriverManager().install())
elif browser == "Chrome":
    driver = Chrome(ChromeDriverManager().install())


