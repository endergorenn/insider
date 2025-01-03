from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//ul[contains(@class, 'navbar-nav')]//a[contains(@class, 'nav-link dropdown-toggle') and normalize-space(text())='Company']")
    CAREERS_LINK = (By.XPATH, "//div[contains(@class, 'new-menu-dropdown-layout-6')]//a[normalize-space(text())='Careers']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com")

    def click_company_menu(self):
        self.wait_for_element(*self.COMPANY_MENU)
        self.click_element(*self.COMPANY_MENU)

    def click_careers_link(self):
        self.click_element(*self.CAREERS_LINK)
