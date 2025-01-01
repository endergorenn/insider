Here are the contents for the file: /my-pytest-selenium-project/my-pytest-selenium-project/tests/test_example.py

from selenium import webdriver
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_example(browser, request):
    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get("https://example.com")
    
    assert "Example Domain" in driver.title

    driver.quit()