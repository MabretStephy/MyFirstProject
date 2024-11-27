import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DriverWrapper:

    def __init__(self):
        # Use webdriver-manager to manage the ChromeDriver
        self.driver = webdriver.Chrome()

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator_type, locator_value):
        element = self.driver.find_element(locator_type, locator_value)
        element.click()

    def input_value(self, locator_type, locator_value, value):
        element = self.driver.find_element(locator_type, locator_value)
        element.send_keys(value)

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    test = DriverWrapper()
    test.open_url("https://www.saucedemo.com/")
    test.input_value(By.XPATH, '//input[@id="user-name"]', "standard_user")
    test.input_value(By.ID, 'password', "secret_sauce")
    test.click_element(By.ID, 'login-button')
    time.sleep(30)
    test.close()
