from day1 import test2 as bl
from selenium.webdriver.common.keys import Keys
import time


bl.driver.get("https://www.facebook.com/");

bl.driver.find_element_by_xpath("//a[text()='Create New Account' or text()='ಸೈನ್ ಅಪ್ ಮಾಡಿ']").click()
time.sleep(5)
bl.driver.find_element_by_name("firstname" ).send_keys("Murali")
bl.driver.find_element_by_name("lastname").send_keys("vemula")
bl.driver.find_element_by_name("reg_email__").send_keys("ramamurali35@gmail.com")
bl.driver.find_element_by_id("password_step_input").send_keys("7396192654")


title = bl.driver.find_element_by_xpath("(//button[contains(text(),'Sign Up') or  starts-with(text(),'ಸೈನ್ ಅಪ್ ಮಾಡಿ')])[1]").text

print(title)

