import os
from datetime import datetime
import shutil

import pytest
import allure
from playwright.sync_api import Page, expect, sync_playwright

from pages.homePage import homePageClass
from pages.loginPage import loginClass
from pages.resultsPage import resultsPageClass
# from pages.loginPage importloginClass,  

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Create a timestamped Allure results folder for each test execution
    """
    # Generate timestamp (format: YYYY-MM-DD_HH-MM-SS)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create timestamped allure results directory
    allure_results_dir = os.path.join("allureResults", timestamp)
    
    # Create the directory if it doesn't exist
    os.makedirs(allure_results_dir, exist_ok=True)
    
    # Store the timestamp and directory path in config for later use
    config.timestamp = timestamp
    config.allure_results_dir = allure_results_dir
    
    # Set the alluredir option
    config.option.alluredir = allure_results_dir
    
    print(f"\nAllure results will be saved to: {allure_results_dir}")


def pytest_sessionfinish(session, exitstatus):
    """
    Ensure results are in the correct timestamped folder
    """
    if hasattr(session.config, 'allure_results_dir'):
        allure_dir = session.config.allure_results_dir
        parent_dir = "allureResults"
        
        # If allure created files in parent directory, move them to timestamped folder
        if os.path.exists(parent_dir):
            for item in os.listdir(parent_dir):
                item_path = os.path.join(parent_dir, item)
                # Skip if it's already the timestamped folder
                if os.path.isdir(item_path) and item != session.config.timestamp:
                    target_path = os.path.join(allure_dir, item)
                    if os.path.exists(target_path):
                        shutil.rmtree(target_path)
                    shutil.move(item_path, target_path)
                elif os.path.isfile(item_path):
                    target_path = os.path.join(allure_dir, item)
                    if os.path.exists(target_path):
                        os.remove(target_path)
                    shutil.move(item_path, target_path)

@pytest.fixture()
# @pytest.mark.parametrize("browserValue",["firefox","chromium"] )
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1850,"height":2000})
        page = context.new_page()
        yield page


@pytest.fixture()
def launchAmazon(page):
    page.goto("https://www.amazon.in/?")


@pytest.fixture()
def loginToAmazon(page):
    page.goto("https://www.amazon.in/?")
    # page.goto(os.getenv("url"))
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    # login.clickOnSigInBtn()
    login.enteruserName("trainingplaywright@gmail.com")
    # username = os.getenv("usname")
    # pw = os.getenv("pwrd")
    # login.enteruserName(os.getenv("usname"))
    login.clickOnContinueBtn()
    login.enterPassword("Welcome@04")
    # login.enterPassword(os.getenv("pwrd"))
    login.clickOnLogInBtn()

@pytest.fixture()
def resultsPage(page):
    resultsPage =resultsPageClass(page)
    return resultsPage

@pytest.fixture()
def homePage(page):
    homePage = homePageClass(page)
    return homePage



@pytest.fixture()
def commonObj(page):
    resultsPage =resultsPageClass(page)
    homePage = homePageClass(page)
    return resultsPage,homePage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot when a test fails
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.failed and call.when == "call":
        try:
            # Get the page fixture if it exists
            page = item.funcargs.get("page")
            if page:
                # Take screenshot
                screenshot_path = f"screenshot_{item.name}.png"
                page.screenshot(path=screenshot_path)
                
                # Attach to Allure report
                allure.attach.file(
                    screenshot_path,
                    name=f"Screenshot - {item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # Clean up screenshot file
                if os.path.exists(screenshot_path):
                    os.remove(screenshot_path)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
