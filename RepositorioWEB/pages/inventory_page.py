from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_by_name(self, product_name):
        # Localiza o botão "Add to cart" pelo nome do produto
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(By.CSS_SELECTOR, "button").click()
                return
        raise Exception(f"Produto '{product_name}' não encontrado.")

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)