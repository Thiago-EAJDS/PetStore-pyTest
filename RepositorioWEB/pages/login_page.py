from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Representa a página de login do SauceDemo seguindo o padrão Page Object Model
class LoginPage(BasePage):

    # Localizadores dos elementos da página de login
    USERNAME  = (By.ID, "user-name")
    PASSWORD  = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self, base_url):
        # Navega para a URL base da aplicação
        self.driver.get(base_url)

    def login(self, username, password):
        # Preenche as credenciais e clica no botão de login
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        # Retorna o texto da mensagem de erro exibida após login inválido
        return self.get_text(self.ERROR_MSG)