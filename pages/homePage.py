from playwright.sync_api import Page, expect

class homePageClass():
    def __init__(self, page:Page):
        self.searchBoxTextField = page.locator("input#twotabsearchtextbox")
        self.searchBtn = page.locator("input#nav-search-submit-button")

    def enterProductInTheSearchBox(self,product):
         self.searchBoxTextField.fill(product)


    def clickOnSearchBtn(self):
        self.searchBtn.click()