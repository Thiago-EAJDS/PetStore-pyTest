from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Representa a página de listagem de produtos seguindo o padrão Page Object Model
class InventoryPage(BasePage):

    # Localizadores dos elementos da página de inventário
    TITLE      = (By.CLASS_NAME, "title")
    CART_ICON  = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_by_name(self, product_name):
        # Percorre todos os produtos da página e clica em "Add to cart" pelo nome
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(By.CSS_SELECTOR, "button").click()
                return
        # Lança exceção caso o produto não seja encontrado na listagem
        raise Exception(f"Produto '{product_name}' não encontrado.")

    def go_to_cart(self):
        # Navega para o carrinho de compras
        self.click(self.CART_ICON)

    def get_page_title(self):
        # Retorna o título da página atual
        return self.get_text(self.TITLE)

    def get_cart_count(self):
        # Retorna a quantidade de itens exibida no ícone do carrinho
        return self.get_text(self.CART_BADGE)