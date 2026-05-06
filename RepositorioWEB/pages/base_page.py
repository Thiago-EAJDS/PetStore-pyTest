from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Classe base para todas as páginas, implementando o padrão Page Object Model.
# Centraliza os métodos de interação com elementos para evitar duplicação de código.
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # Define um tempo máximo de espera de 10 segundos para localizar elementos
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        # Aguarda o elemento estar presente no DOM antes de retorná-lo
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        # Aguarda o elemento estar clicável antes de interagir
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        # Limpa o campo e digita o texto informado
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        # Retorna o texto visível de um elemento
        return self.find(locator).text

    def is_visible(self, locator):
        # Verifica se o elemento está visível na página, retornando True ou False
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False