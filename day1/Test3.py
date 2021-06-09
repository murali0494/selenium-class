from selenium import webdriver

driver=webdriver.Edge(executable_path="E:\\pythonProject\\selenium@class\\msedgedriver.exe" )
driver.get("http://yahoo.com")
print(driver.title)
print(driver.current_url)
driver.quit()