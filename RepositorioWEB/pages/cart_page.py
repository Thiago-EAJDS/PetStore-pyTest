from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Representa a página do carrinho de compras seguindo o padrão Page Object Model
class CartPage(BasePage):

    # Localizadores dos elementos da página do carrinho
    TITLE        = (By.CLASS_NAME, "title")
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEMS   = (By.CLASS_NAME, "cart_item")

    def get_page_title(self):
        # Retorna o título da página atual
        return self.get_text(self.TITLE)

    def get_item_names(self):
        # Retorna uma lista com os nomes de todos os produtos presentes no carrinho
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def proceed_to_checkout(self):
        # Clica no botão de checkout para avançar para o preenchimento dos dados
        self.click(self.CHECKOUT_BTN)