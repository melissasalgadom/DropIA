# Manual de Usuario - DropAI

## Aplicación de Dropshipping Automatizado con Inteligencia Artificial

### Índice

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Configuración Inicial](#configuración-inicial)
5. [Funcionalidades Principales](#funcionalidades-principales)
   - [Dashboard](#dashboard)
   - [Búsqueda e Importación de Productos](#búsqueda-e-importación-de-productos)
   - [Análisis de Mercado con IA](#análisis-de-mercado-con-ia)
   - [Gestión de Pedidos](#gestión-de-pedidos)
   - [Automatización de Tareas](#automatización-de-tareas)
6. [Limitaciones y Consideraciones](#limitaciones-y-consideraciones)
7. [Solución de Problemas](#solución-de-problemas)
8. [Preguntas Frecuentes](#preguntas-frecuentes)

## Introducción

DropAI es una aplicación de dropshipping automatizada con inteligencia artificial diseñada para ayudarte a generar ingresos extra sin inversión inicial. La aplicación integra plataformas gratuitas de dropshipping con herramientas de IA para automatizar la selección de productos, optimización de precios y gestión de pedidos.

Esta solución ha sido desarrollada para aprovechar al máximo los recursos gratuitos disponibles, permitiéndote iniciar un negocio de dropshipping sin costos asociados mientras maximizas la eficiencia mediante la automatización y la inteligencia artificial.

## Requisitos del Sistema

Para ejecutar DropAI, necesitarás:

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Edge)
- Conexión a Internet
- 500 MB de espacio en disco
- 2 GB de RAM (recomendado)

## Instalación

Sigue estos pasos para instalar DropAI en tu sistema:

1. Clona o descarga el repositorio de DropAI:
   ```
   git clone https://github.com/usuario/dropai.git
   cd dropai
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Inicializa la base de datos:
   ```
   cd app
   python -c "import sqlite3; conn = sqlite3.connect('dropshipping.db'); conn.executescript(open('schema.sql').read()); conn.close()"
   ```

4. Inicia la aplicación:
   ```
   python app.py
   ```

5. Accede a la aplicación desde tu navegador:
   ```
   http://localhost:5000
   ```

## Configuración Inicial

Antes de comenzar a utilizar todas las funcionalidades de DropAI, es necesario realizar algunas configuraciones iniciales:

1. **Configuración de Plataformas de Dropshipping**:
   - Navega a la sección "Configuración" desde el menú principal
   - Introduce tus credenciales de DSers (si dispones de ellas)
   - Configura el margen de beneficio deseado para el cálculo automático de precios

2. **Preferencias de Automatización**:
   - Establece la frecuencia de actualización de precios
   - Configura los criterios para la selección automática de productos
   - Define las categorías de productos de interés

## Funcionalidades Principales

### Dashboard

El dashboard proporciona una visión general de tu negocio de dropshipping, mostrando:

- Número de productos activos
- Pedidos pendientes
- Tareas automatizadas programadas
- Acceso rápido a las principales funcionalidades

### Búsqueda e Importación de Productos

DropAI te permite buscar e importar productos de diferentes plataformas de dropshipping:

1. **Búsqueda de Productos**:
   - Navega a la sección "Buscar Productos"
   - Introduce palabras clave relacionadas con los productos que deseas vender
   - Selecciona la plataforma de búsqueda (por defecto: DSers/AliExpress)
   - Haz clic en "Buscar"

2. **Importación de Productos**:
   - Revisa los resultados de la búsqueda
   - Haz clic en "Importar" junto a los productos que desees añadir a tu catálogo
   - Los productos importados aparecerán en la sección "Productos"

3. **Mejora de Descripciones con IA**:
   - Para cada producto importado, puedes generar descripciones mejoradas con IA
   - Navega a la página del producto y haz clic en "Generar Descripción con IA"
   - La IA creará una descripción atractiva basada en las características del producto

### Análisis de Mercado con IA

La funcionalidad de análisis de mercado utiliza inteligencia artificial para identificar tendencias y oportunidades:

1. **Análisis de Tendencias**:
   - Navega a la sección "Análisis de Mercado"
   - Visualiza las categorías y productos en tendencia
   - Observa las tasas de crecimiento y puntuaciones de popularidad

2. **Recomendaciones de Productos**:
   - Basándose en tus preferencias y el análisis de mercado, la IA recomienda productos con alto potencial
   - Puedes filtrar las recomendaciones por categoría o presupuesto
   - Haz clic en "Importar" para añadir directamente los productos recomendados a tu catálogo

### Gestión de Pedidos

DropAI simplifica la gestión de pedidos de tu negocio de dropshipping:

1. **Visualización de Pedidos**:
   - Navega a la sección "Pedidos"
   - Visualiza todos los pedidos recibidos y su estado actual

2. **Procesamiento de Pedidos**:
   - Selecciona los pedidos pendientes
   - Haz clic en "Procesar Pedidos" para iniciar el proceso de cumplimiento
   - La aplicación se comunicará con la plataforma de dropshipping para gestionar el envío

3. **Seguimiento de Envíos**:
   - Para cada pedido procesado, podrás ver el número de seguimiento
   - Actualiza el estado de los pedidos manualmente o mediante la automatización

### Automatización de Tareas

DropAI permite automatizar diversas tareas para maximizar la eficiencia:

1. **Programación de Tareas**:
   - Navega a la sección "Configuración" > "Automatización"
   - Selecciona el tipo de tarea a programar (actualización de precios, importación de productos, procesamiento de pedidos, análisis de mercado)
   - Establece la frecuencia de ejecución

   > **Nota importante**: La ejecución de tareas programadas periódicas puede estar temporalmente deshabilitada debido a limitaciones de recursos del sistema. En este caso, deberás ejecutar las tareas manualmente cuando sea necesario.

2. **Monitoreo de Tareas**:
   - Visualiza el estado de las tareas programadas
   - Consulta los resultados de las últimas ejecuciones
   - Cancela o modifica tareas según sea necesario

## Limitaciones y Consideraciones

Es importante tener en cuenta las siguientes limitaciones de DropAI:

1. **Planes Gratuitos de Plataformas**:
   - Los planes gratuitos de plataformas como DSers tienen limitaciones en el número de productos (hasta 3,000 para DSers)
   - Modalyst permite hasta 25 productos en su plan gratuito
   - Trendsi es completamente gratuito pero se limita a productos de moda

2. **Automatización**:
   - La automatización completa puede requerir que la aplicación esté en ejecución constante
   - Algunas funcionalidades de automatización pueden estar limitadas por las políticas de las plataformas

3. **Inteligencia Artificial**:
   - Los modelos de IA locales tienen capacidades limitadas comparados con servicios pagos
   - El análisis de mercado se basa en datos simulados cuando no hay conexión a APIs externas

4. **Integración con Plataformas**:
   - La integración con plataformas sin APIs públicas (como DSers) se realiza mediante automatización web, lo que puede ser menos estable

## Solución de Problemas

### Problemas de Conexión con Plataformas

Si experimentas problemas al conectar con plataformas de dropshipping:

1. Verifica tus credenciales en la sección de Configuración
2. Asegúrate de tener una conexión a Internet estable
3. Comprueba si la plataforma está en mantenimiento
4. Reinicia la aplicación

### Errores en la Importación de Productos

Si encuentras errores al importar productos:

1. Verifica que no hayas alcanzado el límite de productos de tu plan gratuito
2. Intenta con palabras clave diferentes
3. Comprueba la conexión con la plataforma

### Problemas con la Automatización

Si las tareas automatizadas no se ejecutan correctamente:

1. Verifica que la aplicación esté en ejecución
2. Comprueba los registros de errores en la sección de Automatización
3. Recuerda que algunas funcionalidades de automatización periódica pueden estar temporalmente deshabilitadas

## Preguntas Frecuentes

**P: ¿Puedo usar DropAI sin credenciales de plataformas de dropshipping?**

R: Sí, DropAI incluye un modo de demostración que simula la integración con plataformas, permitiéndote explorar las funcionalidades sin credenciales reales.

**P: ¿Cómo puedo maximizar mis beneficios con DropAI?**

R: Utiliza el análisis de mercado con IA para identificar productos en tendencia, configura márgenes de beneficio adecuados, y aprovecha la automatización para mantener precios competitivos.

**P: ¿Es posible integrar DropAI con mi tienda online existente?**

R: Actualmente, DropAI funciona como una herramienta independiente. La integración directa con tiendas online requeriría desarrollo adicional.

**P: ¿Qué hago si necesito más productos que los permitidos en los planes gratuitos?**

R: Puedes rotar tu inventario, eliminando productos menos rentables para añadir nuevos, o considerar la posibilidad de actualizar a planes pagos de las plataformas si tu negocio crece.

**P: ¿La IA de DropAI puede predecir qué productos serán más rentables?**

R: La IA proporciona recomendaciones basadas en tendencias de mercado y datos históricos simulados, pero no puede garantizar el éxito de ventas de productos específicos.

---

¡Gracias por elegir DropAI para tu negocio de dropshipping! Si tienes más preguntas o necesitas asistencia adicional, no dudes en contactarnos.
