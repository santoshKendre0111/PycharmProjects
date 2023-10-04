from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Chrome_Obj = Service()
driver = webdriver.Chrome(service=service_Chrome_Obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
print(driver.title)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()   # By Link Text
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")     # By Xpath -parent to child
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("pass@321") # By CSS Selector parent to child
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("pass@321")
driver.find_element(By.XPATH, "//*[contains(text(), 'Save New Password')]").click()