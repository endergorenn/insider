from .base_page import BasePage
from selenium.webdriver.common.by import By

class QAJobsPage(BasePage):
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    LOCATION_FILTER = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    DEPARTMENT_FILTER = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOB_LIST = (By.XPATH, "//div[@id='jobs-list']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-yellow rounded has-icon page-button next')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def click_see_all_qa_jobs(self):
        self.click_element(*self.SEE_ALL_QA_JOBS_BUTTON)

    def filter_jobs_by_location(self, location):
        self.click_element(*self.LOCATION_FILTER)
        location_option = self.wait_for_element(By.XPATH, f"//li[contains(text(), '{location}')]")
        location_option.click()

    def filter_jobs_by_department(self, department):
        self.click_element(*self.DEPARTMENT_FILTER)
        department_option = self.wait_for_element(By.XPATH, f"//li[contains(text(), '{department}')]")
        department_option.click()

    def get_job_items(self):
        return self.driver.find_elements(By.XPATH, ".//div[contains(@class, 'position-list-item-wrapper')]")

    def click_next_button(self):
        self.click_element(*self.NEXT_BUTTON)
