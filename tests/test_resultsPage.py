from playwright.sync_api import Page, expect
import pytest

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


# def test_verifySearchResults(page: Page, loginToAmazon):
#     homePage = homePageClass(page)
#     resultsPage =resultsPageClass(page)
#     page.wait_for_timeout(5000)
#     homePage.enterProductInTheSearchBox("iphone")
#     homePage.clickOnSearchBtn()
#     page.wait_for_timeout(5000)
#     resultsText = []
#     errors =[]
#     for i in range(resultsPage.resultsText.count()):
#         resultsText.append(resultsPage.resultsText.nth(i).text_content())

#     print(resultsText[0])
#     for text in resultsText:
#         try:
#             assert "iphone" in text.lower() or "apple" in text.lower()
#         except Exception as e:
#             errors.append(e)
#     print(errors)
#     print("---------------------------")
#     assert errors.count==0, "displayed results has results other than iphone and apple"
    


