from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def get_element_text(self, by, value):
        element = self.wait_for_element(by, value)
        return element.text
