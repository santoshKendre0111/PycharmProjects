from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_chromeObj = Service()
driver = webdriver.Chrome(service=service_chromeObj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Demo User")  # By CSS
driver.find_element(By.NAME, "email").send_keys("demo@gmail.com")  # By Name
driver.find_element(By.ID, "exampleInputPassword1").send_keys("pass@123")  # By ID
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")    # By CSS ID
driver.find_element(By.XPATH, "//input[@type='submit']").click()  # By Xpath
suc_msg = driver.find_element(By.CLASS_NAME, "alert-success").text  # By ClassName
print(suc_msg)
assert "Success!" in suc_msg

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("Demo User too")
