from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = Edge(executable_path="E:\\pythonProject\\selenium@class\\msedgedriver.exe" )


driver.get("http://durgasoftonline.com/")

time.sleep(5)
driver.quit()