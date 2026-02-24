import os

import pytest
from playwright.sync_api import Page, expect, sync_playwright

from pages.homePage import homePageClass
from pages.loginPage import loginClass
from pages.resultsPage import resultsPageClass
# from pages.loginPage importloginClass,  

@pytest.fixture()
# @pytest.mark.parametrize("browserValue",["firefox","chromium"] )
def page():
    browserValue = os.getenv("browser","chromium")
    with sync_playwright() as p:
        if browserValue=="firefox":
            browser = p.firefox.launch(headless=False)
        if browserValue=="chromium":
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
    # login.enteruserName("trainingplaywright@gmail.com")
    # username = os.getenv("usname")
    # pw = os.getenv("pwrd")
    login.enteruserName(os.getenv("usname"))
    login.clickOnContinueBtn()
    # login.enterPassword("Welcome@04")
    login.enterPassword(os.getenv("pwrd"))
    login.clickOnLogInBtn()

@pytest.fixture()
def resultsPage(page):
    resultsPage =resultsPageClass(page)
    return resultsPage

@pytest.fixture()
def homePage(page):
    homePage = homePageClass(page)
    return 



@pytest.fixture()
def commonObj(page):
    resultsPage =resultsPageClass(page)
    homePage = homePageClass(page)
    return resultsPage,homePage

