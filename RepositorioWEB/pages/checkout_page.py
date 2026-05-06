from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Representa as etapas de checkout seguindo o padrão Page Object Model
class CheckoutPage(BasePage):

    # Localizadores dos campos do formulário e botões da página de checkout
    FIRST_NAME     = (By.ID, "first-name")
    LAST_NAME      = (By.ID, "last-name")
    POSTAL         = (By.ID, "postal-code")
    CONTINUE       = (By.ID, "continue")
    FINISH         = (By.ID, "finish")
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")
    TITLE          = (By.CLASS_NAME, "title")

    def fill_info(self, first_name, last_name, postal_code):
        # Preenche o formulário com os dados pessoais necessários para finalizar a compra
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL, postal_code)

    def continue_checkout(self):
        # Avança para a tela de resumo do pedido
        self.click(self.CONTINUE)

    def finish_order(self):
        # Confirma e finaliza a compra
        self.click(self.FINISH)

    def get_confirmation_message(self):
        # Retorna a mensagem de confirmação exibida após a compra ser concluída
        return self.get_text(self.CONFIRM_HEADER)

    def get_page_title(self):
        # Retorna o título da página atual
        return self.get_text(self.TITLE)