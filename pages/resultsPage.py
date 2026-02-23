from playwright.sync_api import Page, expect

class resultsPageClass():
    def __init__(self, page:Page):
        self.resultsText = page.locator("//h2[text()='Results']")
        self.productAddToCartBtn = lambda product:page.locator(f"//span[contains(text(),'{product}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart']")
        self.decrementicon = page.locator("span[data-a-selector='decrement-icon']")
        self.cartIcon = page.locator("#nav-cart-text-container")

    # def productAddToCartBtn(self, page,product):
    #     page.locator(f"//span[contains(text(),'{product}')]//ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart']")

    def validateTheVisibilityOfResultsText(self):
        expect(self.resultsText).to_be_visible(timeout=60000)
        

    def clickOnAddToCart(self, product):       
        self.productAddToCartBtn(product).first.click()
    
    def getResultsText(self):
        return self.resultsText.text_content()

    def clickOnAddToCartBtn(self, product):
        self.productAddToCartBtn(product).first.click()
        

    def validateTheVisibilityOfDecementIconAfterAddingTheElementToCart(self):
        expect(self.decrementicon.first).to_be_visible()

    def clickOnDecrementicon(self):
        self.decrementicon.first.click()

    def validateThatTheDecrementionIsNotVisible(self):
        expect(self.decrementicon).not_to_be_visible()

    def clickOnCartBtn(self):
        self.cartIcon.click()


