import os

import pytest
from playwright.sync_api import Page, expect, sync_playwright

from pages.loginPage import loginClass
# from pages.loginPage importloginClass,  

@pytest.fixture()
def launchAmazon(page):
    page.goto("https://www.amazon.in/?")


@pytest.fixture()
def loginToAmazon(page):
    # page.goto("https://www.amazon.in/?")
    page.goto(os.getenv("url"))
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

# @pytest.fixture()
# def page():
#     with sync_playwright as p:
#         browser = 