from day1 import test2 as bl
from selenium.webdriver.common.keys import Keys

bl.driver.get("https://www.amazon.in")

bl.driver.find_element_by_id("twotabsearchtextbox").send_keys("shuttle rackets",Keys.ENTER)