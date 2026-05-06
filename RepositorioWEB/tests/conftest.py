import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Adiciona a pasta raiz do projeto ao path para permitir imports dos módulos pages e utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Fixture com escopo de função: um navegador novo é iniciado e encerrado para cada teste
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--headless")           # Modo sem interface gráfica para o CI
    options.add_argument("--no-sandbox")          # Necessário para rodar no Linux/CI
    options.add_argument("--disable-dev-shm-usage")  # Evita erros de memória no CI

    # Desativa verificações de segurança que podem interromper o fluxo do teste
    options.add_argument("--disable-features=PasswordCheck,SafeBrowsingEnhancedProtection")

    # Desativa o gerenciador de senhas e a detecção de vazamento de credenciais do Chrome
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    # Inicializa o ChromeDriver automaticamente com a versão compatível ao Chrome instalado
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver  # Disponibiliza o driver para o teste

    driver.quit() # Encerra o navegador ao fim de cada teste