from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def get_item_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)