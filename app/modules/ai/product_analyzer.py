import requests
import json
import random
from transformers import pipeline
import os

class ProductAnalyzer:
    """
    Clase para análisis de productos y mercado utilizando IA
    """
    
    def __init__(self):
        # Inicializar modelos de IA si están disponibles localmente
        self.sentiment_analyzer = None
        self.text_generator = None
        try:
            # Intentar cargar modelos ligeros para análisis de sentimiento
            self.sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
            # Para generación de texto usamos un modelo más pequeño
            self.text_generator = pipeline('text-generation', model='distilgpt2')
        except Exception as e:
            print(f"No se pudieron cargar los modelos de IA: {str(e)}")
            print("Se utilizarán funciones simuladas para desarrollo")
    
    def analyze_product_sentiment(self, product_name, reviews):
        """
        Analiza el sentimiento de las reseñas de un producto
        """
        if self.sentiment_analyzer:
            try:
                results = self.sentiment_analyzer(reviews)
                positive_count = sum(1 for r in results if r['label'] == 'POSITIVE')
                sentiment_score = positive_count / len(reviews) if reviews else 0.5
                return {
                    'product': product_name,
                    'sentiment_score': sentiment_score,
                    'positive_reviews': positive_count,
                    'total_reviews': len(reviews)
                }
            except Exception as e:
                print(f"Error en análisis de sentimiento: {str(e)}")
        
        # Simulación para desarrollo
        sentiment_score = random.uniform(0.3, 0.9)
        return {
            'product': product_name,
            'sentiment_score': sentiment_score,
            'positive_reviews': int(len(reviews) * sentiment_score) if reviews else 5,
            'total_reviews': len(reviews) if reviews else 10
        }
    
    def generate_product_description(self, product_name, keywords):
        """
        Genera una descripción mejorada para un producto
        """
        if self.text_generator:
            try:
                prompt = f"Este producto {product_name} es perfecto para quienes buscan {', '.join(keywords)}. "
                result = self.text_generator(prompt, max_length=150, num_return_sequences=1)
                return result[0]['generated_text']
            except Exception as e:
                print(f"Error en generación de descripción: {str(e)}")
        
        # Descripciones predefinidas para desarrollo
        descriptions = [
            f"Descubre el increíble {product_name}, diseñado para ofrecer la mejor experiencia en {keywords[0] if keywords else 'uso diario'}. Con características premium y materiales de alta calidad, este producto superará tus expectativas.",
            f"El {product_name} es la solución perfecta para quienes buscan {keywords[0] if keywords else 'calidad'}. Su diseño innovador y funcionalidad avanzada lo convierten en la opción ideal para uso diario.",
            f"Presentamos el {product_name}, la elección preferida por expertos en {keywords[0] if keywords else 'el sector'}. Combina estilo, durabilidad y rendimiento excepcional en un solo producto.",
            f"El {product_name} revoluciona la manera en que experimentas {keywords[0] if keywords else 'la tecnología'}. Con su diseño elegante y funcionalidades avanzadas, transformará tu rutina diaria."
        ]
        return random.choice(descriptions)
    
    def get_market_trends(self, category=None):
        """
        Obtiene tendencias de mercado para una categoría específica o general
        """
        # En una implementación real, esto podría conectarse a APIs de tendencias
        # o analizar datos de redes sociales
        
        # Tendencias simuladas para desarrollo
        trends = [
            {
                'category': 'Electrónica',
                'trending_products': ['Auriculares inalámbricos', 'Cargadores rápidos', 'Smartwatches'],
                'growth_rate': '15%',
                'popularity_score': 0.85
            },
            {
                'category': 'Hogar',
                'trending_products': ['Organizadores minimalistas', 'Luces LED inteligentes', 'Difusores de aromas'],
                'growth_rate': '12%',
                'popularity_score': 0.78
            },
            {
                'category': 'Moda',
                'trending_products': ['Ropa deportiva sostenible', 'Accesorios minimalistas', 'Calzado vegano'],
                'growth_rate': '18%',
                'popularity_score': 0.92
            },
            {
                'category': 'Belleza',
                'trending_products': ['Productos orgánicos', 'Herramientas faciales', 'Maquillaje vegano'],
                'growth_rate': '20%',
                'popularity_score': 0.88
            },
            {
                'category': 'Mascotas',
                'trending_products': ['Juguetes interactivos', 'Alimentos naturales', 'Accesorios personalizados'],
                'growth_rate': '14%',
                'popularity_score': 0.75
            }
        ]
        
        if category:
            filtered_trends = [t for t in trends if t['category'].lower() == category.lower()]
            return filtered_trends if filtered_trends else trends
        
        return trends
    
    def recommend_products(self, user_preferences=None, budget=None):
        """
        Recomienda productos basados en preferencias del usuario y presupuesto
        """
        # Productos simulados para recomendación
        all_products = [
            {
                'id': '2001',
                'name': 'Auriculares Bluetooth Premium',
                'category': 'Electrónica',
                'price': 25.99,
                'profit_margin': 0.45,
                'popularity': 0.88
            },
            {
                'id': '2002',
                'name': 'Organizador de Cables Magnético',
                'category': 'Hogar',
                'price': 8.50,
                'profit_margin': 0.65,
                'popularity': 0.72
            },
            {
                'id': '2003',
                'name': 'Lámpara LED con Control Remoto',
                'category': 'Hogar',
                'price': 18.75,
                'profit_margin': 0.55,
                'popularity': 0.81
            },
            {
                'id': '2004',
                'name': 'Pulsera Inteligente Deportiva',
                'category': 'Electrónica',
                'price': 22.50,
                'profit_margin': 0.50,
                'popularity': 0.85
            },
            {
                'id': '2005',
                'name': 'Mochila Impermeable USB',
                'category': 'Moda',
                'price': 29.99,
                'profit_margin': 0.60,
                'popularity': 0.79
            },
            {
                'id': '2006',
                'name': 'Set de Cuidado Facial Orgánico',
                'category': 'Belleza',
                'price': 15.99,
                'profit_margin': 0.70,
                'popularity': 0.83
            },
            {
                'id': '2007',
                'name': 'Juguete Interactivo para Mascotas',
                'category': 'Mascotas',
                'price': 12.50,
                'profit_margin': 0.65,
                'popularity': 0.76
            }
        ]
        
        # Filtrar por presupuesto si se especifica
        if budget:
            all_products = [p for p in all_products if p['price'] <= float(budget)]
        
        # Filtrar por preferencias si se especifican
        if user_preferences and 'categories' in user_preferences:
            preferred_categories = user_preferences['categories']
            filtered_products = [p for p in all_products if p['category'] in preferred_categories]
            if filtered_products:
                all_products = filtered_products
        
        # Ordenar por una combinación de popularidad y margen de beneficio
        all_products.sort(key=lambda x: (x['popularity'] * 0.7 + x['profit_margin'] * 0.3), reverse=True)
        
        return all_products[:5]  # Devolver los 5 mejores productos

# Instancia para uso directo
product_analyzer = ProductAnalyzer()

# Funciones de conveniencia para acceso directo
def get_market_trends(category=None):
    return product_analyzer.get_market_trends(category)

def recommend_products(user_preferences=None, budget=None):
    return product_analyzer.recommend_products(user_preferences, budget)

def generate_product_description(product_name, keywords=None):
    if not keywords:
        keywords = []
    return product_analyzer.generate_product_description(product_name, keywords)

def analyze_product_sentiment(product_name, reviews=None):
    if not reviews:
        reviews = []
    return product_analyzer.analyze_product_sentiment(product_name, reviews)
