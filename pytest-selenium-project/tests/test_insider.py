import time
import pytest
import logging
import sys
import os
from selenium.webdriver.common.by import By

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestInsiderWebsite:

    def test_web_page_open(self, browser):
        home_page = HomePage(browser)
        assert "Insider" in browser.title

    def test_career_page(self, browser):
        home_page = HomePage(browser)
        home_page.click_company_menu()
        home_page.click_careers_link()

        careers_page = CareersPage(browser)
        assert careers_page.is_life_at_insider_section_present()
        assert careers_page.is_life_at_insider_block_present()
        assert careers_page.is_our_locations_block_present()
        assert careers_page.is_our_locations_section_present()

    def test_qa_jobs_filter(self, browser):
        qa_jobs_page = QAJobsPage(browser)
        qa_jobs_page.click_see_all_qa_jobs()

        time.sleep(15)  # Add a delay to wait for the filters to load

        qa_jobs_page.filter_jobs_by_location("Istanbul, Turkey")
        qa_jobs_page.filter_jobs_by_department("Quality Assurance")

        job_items = qa_jobs_page.get_job_items()
        assert job_items is not None

        browser.execute_script("window.scrollBy(0, 500)")
        time.sleep(2)

        while True:
            job_items = qa_jobs_page.get_job_items()
            logger.info(f"Number of job items found: {len(job_items)}")

            for job in job_items:
                job_title = job.find_element(By.XPATH, "./p[contains(@class, 'position-title')]").text
                job_department = job.find_element(By.XPATH, "./span[contains(@class, 'position-department')]").text
                job_location = job.find_element(By.XPATH, "./div[contains(@class, 'position-location')]").text
                logger.info(f"Job Title: {job_title}, Department: {job_department}, Location: {job_location}")
                assert "Quality Assurance" in job_department
                assert "Istanbul, Turkey" in job_location

            try:
                qa_jobs_page.click_next_button()
                time.sleep(1)
            except:
                break

        view_role_button = job_items[0].find_element(By.XPATH, "./a[contains(@class, 'btn btn-navy rounded')]")
        job_link = view_role_button.get_attribute("href")
        logger.info(f"Job Link: {job_link}")
        browser.execute_script("arguments[0].click();", view_role_button)
        time.sleep(2)

        browser.switch_to.window(browser.window_handles[-1])
        assert browser.current_url == job_link, f"Expected URL: {job_link}, but got: {browser.current_url}"
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
