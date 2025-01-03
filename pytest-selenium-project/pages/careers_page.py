from .base_page import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//h2[contains(@class, 'elementor-heading-title elementor-size-default') and text()='Life at Insider']")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//section[contains(@class, 'elementor-section') and @data-id='a8e7b90']")
    OUR_LOCATIONS_BLOCK = (By.XPATH, "//h3[contains(@class, 'category-title-media') and normalize-space(text())='Our Locations']")
    OUR_LOCATIONS_SECTION = (By.XPATH, "//section[@id='career-our-location']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_life_at_insider_section_present(self):
        return self.wait_for_element(*self.LIFE_AT_INSIDER_SECTION) is not None

    def is_life_at_insider_block_present(self):
        return self.wait_for_element(*self.LIFE_AT_INSIDER_BLOCK) is not None

    def is_our_locations_block_present(self):
        return self.wait_for_element(*self.OUR_LOCATIONS_BLOCK) is not None

    def is_our_locations_section_present(self):
        return self.wait_for_element(*self.OUR_LOCATIONS_SECTION) is not None
