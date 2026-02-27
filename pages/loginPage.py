import allure
from playwright.sync_api import Page, expect
from allureWraper import BasePage

class loginClass(BasePage):
    # accountsAndListBtn = page.locator("//span[contains(text(),'Account & Lists')]")
    def __init__(self, page):
        self.accountsAndListBtn = page.locator("//span[contains(text(),'Account & Lists')]")
        self.signInBtn =  page.get_by_role("link", name="Sign in", exact=True)
        self.userNameTextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.passwordTextBox = page.get_by_role("textbox", name="Password")
        self.loginBtn = page.get_by_role("button", name="Sign in")
        self.invalidEmailErrorMesg = page.locator("//*[contains(text(),'Invalid email address')]")

    @allure.step("Hover on Account and List")
    def hoverOnAccountAndList(self):
    #    self.accountsAndListBtn.hover()
        self.accountsAndListBtn.click()

    @allure.step("clickOnAccountAndList")
    def clickOnAccountAndList(self):
        self.accountsAndListBtn.click()

    @allure.step("validateTheVisibilityOfAccountAndList")
    def validateTheVisibilityOfAccountAndList(self):
        expect(self.accountsAndListBtn).to_be_visible()

    def clickOnSigInBtn(self):
        self.signInBtn.click()

    def enteruserName(self, username):
        self.userNameTextBox.fill(username)


    def clickOnContinueBtn(self):
        self.continueBtn.click()


    def enterPassword(self, pw):
         self.passwordTextBox.fill(pw)

    def clickOnLogInBtn(self):
       self.loginBtn.click()


    def validateUsernameErrorMessage(self):
        expect(self.invalidEmailErrorMesg).to_be_visible()