from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service


service_ChromeObj = Service()
# service_ChromeObj = Service("C:\\Applications\\webDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_ChromeObj)

# service_FirefoxObj = Service()
# service_FirefoxObj = Service("C:\\Applications\\webDrivers\\geckodriver.exe")
# driver = webdriver.Firefox(service=service_FirefoxObj)

# service_EdgeObj = Service()
# service_EdgeObj = Service("C:\\Applications\\webDrivers\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_EdgeObj)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.back()
driver.forward()
driver.refresh()

driver.close()
