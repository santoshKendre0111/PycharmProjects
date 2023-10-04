import time

import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_Chrome_Obj = Service()
driver = webdriver.Chrome(service=service_Chrome_Obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# static selection from Drpdown

stat_dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
stat_dropdown.select_by_index(1)
# time.sleep()
stat_dropdown.select_by_visible_text("Male")
# time.sleep(3)

# Handling autosuggestive dropdown

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(2)
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == 'India':
        # print(country.text)
        country.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(3)