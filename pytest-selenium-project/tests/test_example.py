from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome"])
class TestInsiderWebsite:

    # def test_web_page_open(self, browser, request):
    #     if browser == "chrome":
    #         driver = webdriver.Chrome()
    #     else:
    #         driver = webdriver.Firefox()
    #
    #     driver.get("https://useinsider.com")
    #     
    #     # Check for a specific element on the Insider web page
    #     assert "Insider" in driver.title  # Example: Check if "Insider" is in the page title
    #
    #     # Optionally, you can check for other elements unique to the Insider page
    #     # Example: Check if a specific element is present on the page
    #     # element = driver.find_element_by_css_selector("unique-element-selector")
    #     # assert element is not None
    #
    #     driver.quit()

    def test_career_page(self, browser, request):
        if browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        # Maximize the browser window
        driver.maximize_window()

        driver.get("https://useinsider.com")

        # Wait for the "Company" menu to be present and visible
        wait = WebDriverWait(driver, 10)
        company_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@class, 'navbar-nav')]//a[contains(@class, 'nav-link dropdown-toggle') and normalize-space(text())='Company']")))

        # Hover over the "Company" menu using its class and text
        ActionChains(driver).move_to_element(company_menu).perform()

        # Click on the "Company" menu
        company_menu.click()

        driver.quit()