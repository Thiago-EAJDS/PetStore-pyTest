import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.helpers import BASE_URL, CREDENTIALS, PRODUCTS_TO_ADD, CHECKOUT_INFO

class TestE2EPurchase:

    def test_login_success(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(CREDENTIALS["username"], CREDENTIALS["password"])

        inventory = InventoryPage(driver)
        assert inventory.get_page_title() == "Products"

    def test_add_products_to_cart(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(CREDENTIALS["username"], CREDENTIALS["password"])

        inventory = InventoryPage(driver)
        for product in PRODUCTS_TO_ADD:
            inventory.add_product_by_name(product)

        assert inventory.get_cart_count() == str(len(PRODUCTS_TO_ADD))

    def test_full_purchase_flow(self, driver):
        # Login
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(CREDENTIALS["username"], CREDENTIALS["password"])

        # Adicionar produtos
        inventory = InventoryPage(driver)
        for product in PRODUCTS_TO_ADD:
            inventory.add_product_by_name(product)
        inventory.go_to_cart()

        # Verificar carrinho
        cart = CartPage(driver)
        assert cart.get_page_title() == "Your Cart"
        item_names = cart.get_item_names()
        for product in PRODUCTS_TO_ADD:
            assert product in item_names
        cart.proceed_to_checkout()

        # Preencher dados e finalizar
        checkout = CheckoutPage(driver)
        assert checkout.get_page_title() == "Checkout: Your Information"
        checkout.fill_info(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        checkout.continue_checkout()
        checkout.finish_order()

        # Confirmar compra
        assert checkout.get_confirmation_message() == "Thank you for your order!"