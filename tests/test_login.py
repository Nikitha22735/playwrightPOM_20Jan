import csv
import json
import pytest

from playwright.sync_api import Page, expect
from pages.loginPage import loginClass
from utils.handlingJsonData import readJsonData

@pytest.mark.login()
def test_example_positive(page: Page, launchAmazon):
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    login.enteruserName("trainingplaywright@gmail.com")
    login.clickOnLogInBtn()
    login.clickOnContinueBtn()
    login.enterPassword("Welcome@04")
    login.clickOnLogInBtn()

# def test_example_negitive(page, launchAmazon):
#     page.wait_for_timeout(5000)
#     login = loginClass(page)
#     login.hoverOnAccountAndList()
#     login.clickOnSigInBtn()
#     login.enteruserName("testing123")
#     login.clickOnContinueBtn()
#     login.validateUsernameErrorMessage()


# def test_example_negitive12(page, launchAmazon):
#     page.wait_for_timeout(5000)
#     login = loginClass(page)
#     login.hoverOnAccountAndList()
#     login.clickOnSigInBtn()
#     login.enteruserName("testing123")
#     login.clickOnContinueBtn()
#     login.validateUsernameErrorMessage()


# def test_example_positive(page: Page, launchAmazon):
#     page.wait_for_timeout(5000)
#     login = loginClass(page)
#     login.hoverOnAccountAndList()
#     login.clickOnSigInBtn()
#     credentials = readJsonData("testData\\credentials.json")
#     print(credentials["positiveCredentials"]["username"])
#     login.enteruserName(credentials["positiveCredentials"]["username"])
#     login.clickOnContinueBtn()
#     login.enterPassword(credentials["positiveCredentials"]["password"])
#     login.clickOnLogInBtn()


def test_example_positive(page: Page, launchAmazon):
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    credentials = []
    # with open("testData\\credentails.csv") as csvVariable:
    #     data = csv.DictReader(csvVariable)
        
    #     for row in data:
    #         credentials.append(row)

    # print(credentials)
    # print(credentials[0]["username"])

    with open("testData\\credentails.csv", mode="w") as csvVariable:
        data = csv.DictWriter(csvVariable,fieldnames=["username","password"])
        data.writeheader()
        data.writerow({"username": "22trainingplaywright@gmail.com", "password": "Welcome@04"})
        
