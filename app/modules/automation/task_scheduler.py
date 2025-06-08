import schedule
import time
import threading
import json
import os
import sqlite3
from datetime import datetime, timedelta

class TaskScheduler:
    """
    Clase para programar y ejecutar tareas automatizadas
    """
    
    def __init__(self, db_path=None):
        self.tasks = {}
        self.running = False
        self.thread = None
        self.db_path = db_path
        
    def start(self):
        """Inicia el programador de tareas en un hilo separado"""
        if self.running:
            return False
            
        self.running = True
        self.thread = threading.Thread(target=self._run_scheduler)
        self.thread.daemon = True
        self.thread.start()
        return True
        
    def stop(self):
        """Detiene el programador de tareas"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
            self.thread = None
        return True
        
    def _run_scheduler(self):
        """Función principal del hilo del programador"""
        while self.running:
            schedule.run_pending()
            time.sleep(1)
            
    def schedule_task(self, task_type, frequency, params=None):
        """
        Programa una nueva tarea
        
        Args:
            task_type: Tipo de tarea (update_prices, import_products, etc.)
            frequency: Frecuencia de ejecución (hourly, daily, weekly)
            params: Parámetros adicionales para la tarea
            
        Returns:
            task_id: Identificador único de la tarea programada
        """
        task_id = f"{task_type}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        if not params:
            params = {}
            
        task_info = {
            'id': task_id,
            'type': task_type,
            'frequency': frequency,
            'params': params,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'last_run': None,
            'status': 'scheduled'
        }
        
        # Guardar la tarea en la base de datos si está disponible
        if self.db_path:
            self._save_task_to_db(task_info)
        
        # Programar la tarea según su frecuencia
        if frequency == 'hourly':
            schedule.every().hour.do(self._execute_task, task_id=task_id)
        elif frequency == 'daily':
            schedule.every().day.at("02:00").do(self._execute_task, task_id=task_id)
        elif frequency == 'weekly':
            schedule.every().monday.at("03:00").do(self._execute_task, task_id=task_id)
        else:
            # Frecuencia personalizada en minutos
            try:
                minutes = int(frequency)
                schedule.every(minutes).minutes.do(self._execute_task, task_id=task_id)
            except ValueError:
                print(f"Frecuencia no válida: {frequency}")
                return None
        
        self.tasks[task_id] = task_info
        return task_id
        
    def _execute_task(self, task_id):
        """
        Ejecuta una tarea programada
        
        Args:
            task_id: Identificador de la tarea a ejecutar
        """
        if task_id not in self.tasks:
            print(f"Tarea no encontrada: {task_id}")
            return False
            
        task = self.tasks[task_id]
        task['status'] = 'running'
        task['last_run'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            # Ejecutar la tarea según su tipo
            if task['type'] == 'update_prices':
                result = self._task_update_prices(task['params'])
            elif task['type'] == 'import_products':
                result = self._task_import_products(task['params'])
            elif task['type'] == 'process_orders':
                result = self._task_process_orders(task['params'])
            elif task['type'] == 'analyze_market':
                result = self._task_analyze_market(task['params'])
            else:
                print(f"Tipo de tarea no soportado: {task['type']}")
                task['status'] = 'error'
                return False
                
            task['status'] = 'completed'
            task['last_result'] = result
            
            # Actualizar la tarea en la base de datos
            if self.db_path:
                self._update_task_in_db(task)
                
            return True
            
        except Exception as e:
            print(f"Error al ejecutar tarea {task_id}: {str(e)}")
            task['status'] = 'error'
            task['error'] = str(e)
            
            # Actualizar la tarea en la base de datos
            if self.db_path:
                self._update_task_in_db(task)
                
            return False
            
    def _task_update_prices(self, params):
        """
        Tarea para actualizar precios de productos
        
        Args:
            params: Parámetros de la tarea (margin, min_price, etc.)
        """
        print(f"Ejecutando tarea de actualización de precios con parámetros: {params}")
        
        # En una implementación real, aquí se conectaría con la base de datos
        # y se actualizarían los precios según los parámetros
        
        # Simulación para desarrollo
        return {
            'updated_products': 15,
            'average_increase': '5.2%',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    def _task_import_products(self, params):
        """
        Tarea para importar productos automáticamente
        
        Args:
            params: Parámetros de la tarea (keywords, max_products, etc.)
        """
        print(f"Ejecutando tarea de importación de productos con parámetros: {params}")
        
        # En una implementación real, aquí se conectaría con la plataforma
        # de dropshipping y se importarían productos según los criterios
        
        # Simulación para desarrollo
        return {
            'imported_products': 8,
            'categories': ['Electrónica', 'Hogar'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    def _task_process_orders(self, params):
        """
        Tarea para procesar pedidos pendientes
        
        Args:
            params: Parámetros de la tarea (status, max_orders, etc.)
        """
        print(f"Ejecutando tarea de procesamiento de pedidos con parámetros: {params}")
        
        # En una implementación real, aquí se procesarían los pedidos pendientes
        
        # Simulación para desarrollo
        return {
            'processed_orders': 5,
            'failed_orders': 0,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    def _task_analyze_market(self, params):
        """
        Tarea para analizar el mercado y tendencias
        
        Args:
            params: Parámetros de la tarea (categories, depth, etc.)
        """
        print(f"Ejecutando tarea de análisis de mercado con parámetros: {params}")
        
        # En una implementación real, aquí se conectaría con el módulo de IA
        # para analizar tendencias y generar recomendaciones
        
        # Simulación para desarrollo
        return {
            'trending_categories': ['Electrónica', 'Moda Sostenible'],
            'recommended_products': 12,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    def _save_task_to_db(self, task):
        """
        Guarda una tarea en la base de datos
        
        Args:
            task: Información de la tarea a guardar
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Asegurarse de que la tabla existe
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS scheduled_tasks (
                id TEXT PRIMARY KEY,
                type TEXT,
                frequency TEXT,
                params TEXT,
                created_at TEXT,
                last_run TEXT,
                status TEXT,
                last_result TEXT,
                error TEXT
            )
            ''')
            
            # Insertar la tarea
            cursor.execute('''
            INSERT INTO scheduled_tasks (id, type, frequency, params, created_at, status)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                task['id'],
                task['type'],
                task['frequency'],
                json.dumps(task['params']),
                task['created_at'],
                task['status']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error al guardar tarea en la base de datos: {str(e)}")
            
    def _update_task_in_db(self, task):
        """
        Actualiza una tarea en la base de datos
        
        Args:
            task: Información actualizada de la tarea
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Actualizar la tarea
            cursor.execute('''
            UPDATE scheduled_tasks
            SET last_run = ?, status = ?, last_result = ?, error = ?
            WHERE id = ?
            ''', (
                task.get('last_run'),
                task.get('status'),
                json.dumps(task.get('last_result', {})),
                task.get('error', ''),
                task['id']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error al actualizar tarea en la base de datos: {str(e)}")
            
    def get_all_tasks(self):
        """
        Obtiene todas las tareas programadas
        
        Returns:
            Lista de tareas programadas
        """
        return list(self.tasks.values())
        
    def get_task(self, task_id):
        """
        Obtiene información de una tarea específica
        
        Args:
            task_id: Identificador de la tarea
            
        Returns:
            Información de la tarea o None si no existe
        """
        return self.tasks.get(task_id)
        
    def cancel_task(self, task_id):
        """
        Cancela una tarea programada
        
        Args:
            task_id: Identificador de la tarea a cancelar
            
        Returns:
            True si se canceló correctamente, False en caso contrario
        """
        if task_id not in self.tasks:
            return False
            
        # Eliminar la tarea del programador
        schedule.clear(task_id)
        
        # Actualizar estado en la base de datos
        task = self.tasks[task_id]
        task['status'] = 'cancelled'
        
        if self.db_path:
            self._update_task_in_db(task)
            
        # Eliminar de la lista de tareas
        del self.tasks[task_id]
        
        return True

# Instancia global para uso directo
task_scheduler = TaskScheduler()

# Funciones de conveniencia para acceso directo
def schedule_task(task_type, frequency, params=None):
    return task_scheduler.schedule_task(task_type, frequency, params)

def get_all_tasks():
    return task_scheduler.get_all_tasks()

def get_task(task_id):
    return task_scheduler.get_task(task_id)

def cancel_task(task_id):
    return task_scheduler.cancel_task(task_id)

# Iniciar el programador automáticamente
task_scheduler.start()
