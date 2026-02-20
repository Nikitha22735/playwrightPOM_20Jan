from playwright.sync_api import Page, expect

class resultsPageClass():
    def __init__(self, page:Page):
        self.resultsText = page.locator("//h2[text()='Results']")
        self.productAddToCartBtn = lambda product:page.locator(f"//span[contains(text(),'{product}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart']")

    # def productAddToCartBtn(self, page,product):
    #     page.locator(f"//span[contains(text(),'{product}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart']")

    def validateTheVisibilityOfResultsText(self):
        expect(self.resultsText).to_be_visible()
        

    def clickOnAddToCart(self, product):       
        self.productAddToCartBtn(product).first.click()


