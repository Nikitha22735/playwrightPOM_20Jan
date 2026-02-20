import pytest

from pages.loginPage import loginClass
# from pages.loginPage importloginClass,  

@pytest.fixture()
def launchAmazon(page):
    page.goto("https://www.amazon.in/?")


@pytest.fixture()
def loginToAmazon(page):
    page.goto("https://www.amazon.in/?")
    page.wait_for_timeout(5000)
    login = loginClass(page)
    login.hoverOnAccountAndList()
    login.clickOnSigInBtn()
    login.enteruserName("trainingplaywright@gmail.com")
    login.clickOnContinueBtn()
    login.enterPassword()
    login.clickOnLogInBtn()