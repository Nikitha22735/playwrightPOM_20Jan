from playwright.sync_api import Page, expect
from pages.loginPage import loginClass


def test_example_positive(page: Page, launchAmazon):
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    login.enteruserName("trainingplaywright@gmail.com")
    login.clickOnContinueBtn()
    login.enterPassword()
    login.clickOnLogInBtn()

def test_example_negitive(page, launchAmazon):
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    login.enteruserName("testing123")
    login.clickOnContinueBtn()
    login.validateUsernameErrorMessage()


def test_example_negitive12(page, launchAmazon):
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    login.enteruserName("testing123")
    login.clickOnContinueBtn()
    login.validateUsernameErrorMessage()
