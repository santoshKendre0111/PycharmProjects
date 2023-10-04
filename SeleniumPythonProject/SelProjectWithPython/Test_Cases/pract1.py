from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class browser_initilazation:
    def browser_initilaze(self):
        ser_ChromeObj = Service()
        driver = webdriver.Chrome(service=ser_ChromeObj)
        driver.maximize_window()

        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.maximize_window()

        print(driver.title)
        print(driver.current_url)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.back()
        driver.forward()
        driver.refresh()

classObject = browser_initilazation()
classObject.browser_initilaze()