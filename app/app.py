from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os
import json
from datetime import datetime

# Importar módulos personalizados
from modules.integration import dsers_integration
from modules.ai import product_analyzer
from modules.automation import task_scheduler

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuración de la base de datos
DATABASE = 'dropshipping.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Página principal del dashboard"""
    return render_template('index.html')

@app.route('/products')
def products():
    """Gestión de productos"""
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/search_products', methods=['GET', 'POST'])
def search_products():
    results = []
    if request.method == 'POST':
        keyword = request.form.get('keyword', '')
        platform = request.form.get('platform', 'dsers')
        
        # En un entorno real, aquí se conectaría con la API de la plataforma seleccionada
        # Para el prototipo, generamos datos simulados
        if keyword:
            # Datos simulados para demostración
            results = [
                {
                    'id': '1001',
                    'name': f'Producto {keyword} Premium',
                    'supplier': 'AliExpress',
                    'price': '€19.99',
                    'image': 'https://via.placeholder.com/300',
                    'url': '#'
                },
                {
                    'id': '1002',
                    'name': f'{keyword} Profesional',
                    'supplier': 'AliExpress',
                    'price': '€24.99',
                    'image': 'https://via.placeholder.com/300',
                    'url': '#'
                },
                {
                    'id': '1003',
                    'name': f'{keyword} Económico',
                    'supplier': 'AliExpress',
                    'price': '€14.99',
                    'image': 'https://via.placeholder.com/300',
                    'url': '#'
                }
            ]
    
    return render_template('search_products.html', results=results )


@app.route('/import_product/<int:product_id>')
def import_product(product_id):
    """Importar un producto específico"""
    # Lógica para importar producto
    flash('Producto importado correctamente')
    return redirect(url_for('products'))

@app.route('/analyze_market')
def analyze_market():
    """Análisis de mercado con IA"""
    # Usar el módulo de IA para analizar tendencias
    trends = product_analyzer.get_market_trends()
    return render_template('market_analysis.html', trends=trends)

@app.route('/orders')
def orders():
    """Gestión de pedidos"""
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders').fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

@app.route('/settings')
def settings():
    """Configuración de la aplicación"""
    return render_template('settings.html')

@app.route('/save_settings', methods=['POST'])
def save_settings():
    """Guardar configuración"""
    settings = {
        'dsers_username': request.form['dsers_username'],
        'dsers_password': request.form['dsers_password'],
        'update_frequency': request.form['update_frequency'],
        'price_margin': request.form['price_margin']
    }
    
    # Guardar configuración en la base de datos
    conn = get_db_connection()
    conn.execute('DELETE FROM settings')  # Limpiar configuración anterior
    conn.execute('INSERT INTO settings (key, value) VALUES (?, ?)', 
                ('app_settings', json.dumps(settings)))
    conn.commit()
    conn.close()
    
    flash('Configuración guardada correctamente')
    return redirect(url_for('settings'))

@app.route('/api/products', methods=['GET'])
def api_products():
    """API para obtener productos en formato JSON"""
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'cost': product['cost'],
            'platform': product['platform'],
            'status': product['status']
        })
    
    return jsonify(product_list)

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    """Programar una tarea automatizada"""
    task_type = request.form['task_type']
    frequency = request.form['frequency']
    
    # Usar el módulo de automatización para programar la tarea
    task_id = task_scheduler.schedule_task(task_type, frequency)
    
    flash(f'Tarea programada correctamente con ID: {task_id}')
    return redirect(url_for('settings'))

if __name__ == '__main__':
    # Verificar si la base de datos existe, si no, inicializarla
    if not os.path.exists(DATABASE):
        init_db()
    
    app.run(debug=True, host='0.0.0.0')
