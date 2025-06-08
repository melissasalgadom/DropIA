import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os

class DSersIntegration:
    """
    Clase para integración con DSers utilizando automatización web
    ya que no dispone de una API pública gratuita
    """
    
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.logged_in = False
        self.driver = None
        
    def initialize_driver(self):
        """Inicializa el navegador en modo headless"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        return self.driver
        
    def login(self):
        """Inicia sesión en DSers"""
        if not self.username or not self.password:
            raise ValueError("Se requieren credenciales para iniciar sesión")
            
        if not self.driver:
            self.initialize_driver()
            
        try:
            self.driver.get("https://www.dsers.com/login")
            
            # Esperar a que cargue el formulario de login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            
            # Ingresar credenciales
            self.driver.find_element(By.ID, "username").send_keys(self.username)
            self.driver.find_element(By.ID, "password").send_keys(self.password)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            
            # Esperar a que se complete el login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
            )
            
            self.logged_in = True
            return True
            
        except Exception as e:
            print(f"Error al iniciar sesión: {str(e)}")
            return False
            
    def search_products(self, keyword, max_results=10):
        """
        Busca productos en AliExpress a través de DSers
        """
        if not self.logged_in and not self.login():
            return []
            
        try:
            # Navegar a la página de búsqueda de productos
            self.driver.get(f"https://www.dsers.com/product/search?keyword={keyword}")
            
            # Esperar a que carguen los resultados
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-item"))
            )
            
            # Extraer información de productos
            product_elements = self.driver.find_elements(By.CLASS_NAME, "product-item")[:max_results]
            products = []
            
            for element in product_elements:
                try:
                    product = {
                        'id': element.get_attribute("data-id"),
                        'name': element.find_element(By.CLASS_NAME, "product-title").text,
                        'price': element.find_element(By.CLASS_NAME, "product-price").text,
                        'image': element.find_element(By.TAG_NAME, "img").get_attribute("src"),
                        'supplier': "AliExpress",
                        'url': element.find_element(By.CLASS_NAME, "product-link").get_attribute("href")
                    }
                    products.append(product)
                except Exception as e:
                    print(f"Error al extraer datos del producto: {str(e)}")
                    
            return products
            
        except Exception as e:
            print(f"Error al buscar productos: {str(e)}")
            return []
            
    def import_product(self, product_id):
        """
        Importa un producto específico a la tienda
        """
        if not self.logged_in and not self.login():
            return False
            
        try:
            # Navegar a la página del producto
            self.driver.get(f"https://www.dsers.com/product/detail/{product_id}")
            
            # Esperar a que cargue el botón de importar
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "import-button"))
            )
            
            # Hacer clic en importar
            self.driver.find_element(By.ID, "import-button").click()
            
            # Esperar confirmación
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            
            return True
            
        except Exception as e:
            print(f"Error al importar producto: {str(e)}")
            return False
            
    def get_orders(self, limit=20):
        """
        Obtiene los pedidos recientes
        """
        if not self.logged_in and not self.login():
            return []
            
        try:
            # Navegar a la página de pedidos
            self.driver.get("https://www.dsers.com/orders")
            
            # Esperar a que carguen los pedidos
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "order-item"))
            )
            
            # Extraer información de pedidos
            order_elements = self.driver.find_elements(By.CLASS_NAME, "order-item")[:limit]
            orders = []
            
            for element in order_elements:
                try:
                    order = {
                        'id': element.get_attribute("data-id"),
                        'date': element.find_element(By.CLASS_NAME, "order-date").text,
                        'customer': element.find_element(By.CLASS_NAME, "customer-name").text,
                        'total': element.find_element(By.CLASS_NAME, "order-total").text,
                        'status': element.find_element(By.CLASS_NAME, "order-status").text
                    }
                    orders.append(order)
                except Exception as e:
                    print(f"Error al extraer datos del pedido: {str(e)}")
                    
            return orders
            
        except Exception as e:
            print(f"Error al obtener pedidos: {str(e)}")
            return []
            
    def process_order(self, order_id):
        """
        Procesa un pedido específico
        """
        if not self.logged_in and not self.login():
            return False
            
        try:
            # Navegar a la página del pedido
            self.driver.get(f"https://www.dsers.com/orders/detail/{order_id}")
            
            # Esperar a que cargue el botón de procesar
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "process-button"))
            )
            
            # Hacer clic en procesar
            self.driver.find_element(By.ID, "process-button").click()
            
            # Esperar confirmación
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            
            return True
            
        except Exception as e:
            print(f"Error al procesar pedido: {str(e)}")
            return False
            
    def close(self):
        """Cierra el navegador"""
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.logged_in = False

# Función para simular búsqueda cuando no hay credenciales disponibles
def search_products(keyword, max_results=10):
    """
    Función para simular búsqueda de productos cuando no hay credenciales
    o para desarrollo/pruebas
    """
    # Productos de ejemplo para desarrollo
    sample_products = [
        {
            'id': '1001',
            'name': f'Auriculares Bluetooth 5.0 - Relacionado con: {keyword}',
            'price': '€12.99',
            'image': 'https://example.com/images/headphones.jpg',
            'supplier': 'AliExpress',
            'url': 'https://aliexpress.com/item/1001'
        },
        {
            'id': '1002',
            'name': f'Cargador USB-C rápido - Relacionado con: {keyword}',
            'price': '€8.50',
            'image': 'https://example.com/images/charger.jpg',
            'supplier': 'AliExpress',
            'url': 'https://aliexpress.com/item/1002'
        },
        {
            'id': '1003',
            'name': f'Funda de teléfono {keyword} - Impermeable',
            'price': '€5.99',
            'image': 'https://example.com/images/phonecase.jpg',
            'supplier': 'AliExpress',
            'url': 'https://aliexpress.com/item/1003'
        },
        {
            'id': '1004',
            'name': f'Lámpara LED inteligente - Búsqueda: {keyword}',
            'price': '€15.75',
            'image': 'https://example.com/images/smartlamp.jpg',
            'supplier': 'AliExpress',
            'url': 'https://aliexpress.com/item/1004'
        },
        {
            'id': '1005',
            'name': f'Organizador de cables - Relacionado con: {keyword}',
            'price': '€3.99',
            'image': 'https://example.com/images/cableorganizer.jpg',
            'supplier': 'AliExpress',
            'url': 'https://aliexpress.com/item/1005'
        }
    ]
    
    return sample_products[:max_results]
