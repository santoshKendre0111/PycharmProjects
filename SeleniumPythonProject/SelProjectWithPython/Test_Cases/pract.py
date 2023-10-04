import pytest
from selenium import webdriver


# Fixture for setting up the Selenium WebDriver
@pytest.fixture
def setup():
    # Initialize the WebDriver (you should specify the path to your driver executable)
    driver = webdriver.Chrome()

    # Optional: You can maximize the browser window or set other configurations here
    driver.maximize_window()

    # Pass the driver instance to the test function
    yield driver

    # Teardown: Close the browser after the test is finished
    driver.quit()


# Test using Selenium with Python
def test_open_website_and_assert_title(setup):
    driver = setup

    # Navigate to a website
    driver.get("https://www.google.com/")
    print(driver.title)

    # Assert the page title
    assert "Google" in driver.title