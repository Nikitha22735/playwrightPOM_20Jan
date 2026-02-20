from playwright.sync_api import Page, expect

from pages.homePage import homePageClass
from pages.resultsPage import resultsPageClass

# @pytest.mark.results()
def test_validateNavigationToResultsScreen(page, loginToAmazon):
    homePage = homePageClass(page)
    resultsPage =resultsPageClass(page)
    homePage.enterProductInTheSearchBox("iphone")
    homePage.clickOnSearchBtn()
    resultsPage.validateTheVisibilityOfResultsText()
    page.wait_for_timeout(5000)
    resultsPage.clickOnAddToCart("iPhone 16 Pro")
    page.wait_for_timeout(5000)



