from selenium import webdriver
import pytest
import os

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set an attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def auto_test_fail(request, browser):
    yield
    # Check if the test failed
    if request.node.rep_call.failed:
        # Create the screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take a screenshot if the test failed
        browser.save_screenshot(f"screenshots/{request.node.name}.png")
