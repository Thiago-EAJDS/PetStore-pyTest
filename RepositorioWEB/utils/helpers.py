# URL base do site SauceDemo utilizada como ponto de entrada nos testes
BASE_URL = "https://www.saucedemo.com"

# Credenciais válidas fornecidas pela própria aplicação SauceDemo para fins de teste
CREDENTIALS = {
    "username": "standard_user",
    "password": "secret_sauce"
}

# Produtos que serão adicionados ao carrinho durante o fluxo E2E
PRODUCTS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light"
]

# Dados fictícios utilizados no preenchimento do formulário de checkout
CHECKOUT_INFO = {
    "first_name": "Test",
    "last_name": "User",
    "postal_code": "12345"
}