from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME  = (By.ID, "last-name")
    POSTAL     = (By.ID, "postal-code")
    CONTINUE   = (By.ID, "continue")
    FINISH     = (By.ID, "finish")
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")
    TITLE      = (By.CLASS_NAME, "title")

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE)

    def finish_order(self):
        self.click(self.FINISH)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRM_HEADER)

    def get_page_title(self):
        return self.get_text(self.TITLE)