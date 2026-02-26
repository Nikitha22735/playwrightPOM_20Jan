import os

import pytest
import allure
from playwright.sync_api import Page, expect, sync_playwright

from pages.homePage import homePageClass
from pages.loginPage import loginClass
from pages.resultsPage import resultsPageClass
# from pages.loginPage importloginClass,  

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
    login.clickOnSigInBtn()
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
