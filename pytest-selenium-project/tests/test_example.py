import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
class TestInsiderWebsite:

    def test_web_page_open(self, browser, request):
        if browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        # Maximize the browser window
        driver.maximize_window()

        driver.get("https://useinsider.com")
        WebDriverWait(driver, 10)

        # Check for a specific element on the Insider web page
        assert "Insider" in driver.title  # Example: Check if "Insider" is in the page title

        driver.quit()

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

        # Wait for the dropdown to be visible after clicking "Company"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'new-menu-dropdown-layout-6 show')]")))

        # Wait for the "Careers" link to be present and visible in the dropdown
        careers_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'new-menu-dropdown-layout-6')]//a[normalize-space(text())='Careers']")))

        # Click on the "Careers" link
        careers_link.click()

        # Wait for the Careers page to load
        wait.until(EC.url_contains("careers"))

        # Check if the "Life at Insider" section is present
        life_at_insider_section = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'elementor-heading-title elementor-size-default') and text()='Life at Insider']")))
        assert life_at_insider_section is not None

        # Check if the "Life at Insider" block is present
        life_at_insider_block = wait.until(EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'elementor-section') and @data-id='a8e7b90']")))
        assert life_at_insider_block is not None

        # Check if the "Our Locations" block is present
        our_locations_block = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(@class, 'category-title-media') and normalize-space(text())='Our Locations']")))
        assert our_locations_block is not None

        # Check if the "Our Locations" section is present
        our_locations_section = wait.until(EC.presence_of_element_located((By.XPATH, "//section[@id='career-our-location']")))
        assert our_locations_section is not None

        driver.quit()

    def test_qa_jobs_filter(self, browser, request):
        if browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        # Maximize the browser window
        driver.maximize_window()

        driver.get("https://useinsider.com/careers/quality-assurance/")

        # Wait for the "See all QA jobs" button to be present and visible
        wait = WebDriverWait(driver, 10)
        see_all_qa_jobs_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'See all QA jobs')]")))

        # Click on the "See all QA jobs" button
        see_all_qa_jobs_button.click()

        # Wait for the jobs page to load and verify the correct page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//section[@id='career-position-filter']")))

        # TODO: Database load time is too long. It may take a while to load the filters.
        time.sleep(15)  # Add a delay to wait for the filters to load

        # Filter jobs by Location: "Istanbul, Turkey"
        location_filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-filter-by-location-container']")))
        location_filter.click()
        location_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Istanbul, Turkey')]")))
        location_option.click()

        # Verify that the location filter displays "Istanbul, Turkey"
        selected_location = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-filter-by-location-container' and contains(text(), 'Istanbul, Turkey')]")))
        assert "Istanbul, Turkey" in selected_location.text

        # Filter jobs by Department: "Quality Assurance"
        department_filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-filter-by-department-container']")))
        department_filter.click()
        department_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Quality Assurance')]")))
        department_option.click()

        # Verify that the department filter displays "Quality Assurance"
        selected_department = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-filter-by-department-container' and contains(text(), 'Quality Assurance')]")))
        assert "Quality Assurance" in selected_department.text

        # Check the presence of the job list
        job_list = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='jobs-list']")))
        assert job_list is not None

        driver.execute_script("window.scrollBy(0, 500)")
        # TODO: At the beginning of the job list, it shows all the jobs. A few seconds later, it shows filtered jobs.
        time.sleep(2)

        while True:
            # Log the number of job items found
            job_items = job_list.find_elements(By.XPATH, ".//div[contains(@class, 'position-list-item-wrapper')]")
            logger.info(f"Number of job items found: {len(job_items)}")

            # Log the HTML content of each found element for debugging
            for job in job_items:
                logger.info(job.get_attribute('outerHTML'))

            # Iterate through the job listings and verify their presence
            for job in job_items:
                job_title = job.find_element(By.XPATH, "./p[contains(@class, 'position-title')]").text
                job_department = job.find_element(By.XPATH, "./span[contains(@class, 'position-department')]").text
                job_location = job.find_element(By.XPATH, "./div[contains(@class, 'position-location')]").text
                logger.info(f"Job Title: {job_title}, Department: {job_department}, Location: {job_location}")
                assert "Quality Assurance" in job_department
                assert "Istanbul, Turkey" in job_location

            # Check if the next button is enabled, does not have the disabled attribute, and is interactable
            next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-yellow rounded has-icon page-button next')]")
            if not next_button.get_attribute("disabled") and next_button.is_displayed() and next_button.is_enabled():
                next_button.click()
                time.sleep(1)
            else:
                break

        # Scroll the "View Role" button into view and click it
        view_role_button = job_items[0].find_element(By.XPATH, "./a[contains(@class, 'btn btn-navy rounded')]")
        job_link = view_role_button.get_attribute("href")
        logger.info(f"Job Link: {job_link}")
        driver.execute_script("arguments[0].click();", view_role_button)
        time.sleep(2)

        # Switch to the new window and verify the URL
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == job_link, f"Expected URL: {job_link}, but got: {driver.current_url}"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        driver.quit()
