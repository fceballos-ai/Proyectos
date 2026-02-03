# 🐍 Python DevOps: Automatización y Consumo de APIs

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

> Proyecto práctico de automatización DevOps desarrollado en Python para la gestión de infraestructura, consumo de APIs y automatización de tareas repetitivas.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Dependencias](#-dependencias)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Ejemplos de Ejecución](#-ejemplos-de-ejecución)
- [Automatización con Cron](#-automatización-con-cron)
- [Conceptos DevOps Aplicados](#-conceptos-devops-aplicados)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## 🎯 Descripción del Proyecto

Este repositorio contiene **dos soluciones principales** desarrolladas como parte de un curso de DevOps con Python:

1. **🧹 Automatización de Limpieza de Archivos**: Script que elimina automáticamente archivos antiguos de directorios específicos para liberar espacio en disco.

2. **🌦️ Consulta de Clima vía API**: Cliente que consume la API de OpenWeatherMap para obtener información meteorológica en tiempo real.

3. **📊 Monitor de Sistema Integrado** (BONUS): Combinación de ambas funcionalidades con generación de reportes.

### ¿Por qué este proyecto?

En entornos de **producción y servidores**, es común que los logs y archivos temporales llenen el disco, causando caídas del sistema. La limpieza automática previene estos problemas.

La **integración con APIs** es fundamental en arquitecturas modernas (microservicios, cloud) para comunicar sistemas heterogéneos y automatizar flujos de trabajo.

---

## ✨ Características

### Script de Limpieza de Archivos

- ✅ Elimina archivos basándose en antigüedad configurable
- ✅ Modo de vista previa seguro (no elimina hasta confirmar)
- ✅ Filtrado por extensiones específicas (.log, .tmp, .bak, etc.)
- ✅ Estadísticas detalladas de espacio liberado
- ✅ Conversión automática de tamaños (B → KB → MB → GB)
- ✅ Manejo robusto de errores de permisos
- ✅ Menú interactivo con confirmaciones

### Script de Consulta de Clima

- ✅ Consulta información meteorológica de cualquier ciudad del mundo
- ✅ Datos completos: temperatura, humedad, viento, presión atmosférica
- ✅ Soporte para múltiples idiomas (español por defecto)
- ✅ Manejo de errores de conexión y timeout
- ✅ Modo interactivo y modo CLI con argumentos
- ✅ Interfaz visual profesional con emojis

### Monitor de Sistema (BONUS)

- ✅ Combina clima + análisis de directorios
- ✅ Genera reportes completos del sistema
- ✅ Guarda logs históricos
- ✅ Detecta automáticamente directorios que necesitan limpieza

---

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.7 o superior**
  ```bash
  python3 --version
  ```

- **pip** (gestor de paquetes de Python)
  ```bash
  pip --version
  ```

- **Conexión a Internet** (para la consulta de clima)

- **(Opcional) Git** para clonar el repositorio
  ```bash
  git --version
  ```

---

## 📦 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/python-devops-automation.git
cd python-devops-automation
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar en Linux/Mac
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar API Key (Solo para clima)

1. Regístrate gratis en [OpenWeatherMap](https://openweathermap.org/api)
2. Obtén tu API key
3. Reemplázala en los scripts:
   ```python
   API_KEY = "tu_api_key_aqui"
   ```

---

## 📚 Dependencias

### Librerías Estándar de Python (Incluidas por defecto)

Estas librerías vienen pre-instaladas con Python y **no requieren instalación adicional**:

#### `os` - Sistema de Archivos
**¿Por qué se usa?**
- Interactuar con el sistema operativo
- Leer, crear, eliminar archivos y directorios
- Obtener información de archivos (tamaño, fecha de modificación)

**Funciones utilizadas:**
```python
os.path.exists()    # Verificar si existe una ruta
os.path.isfile()    # Verificar si es un archivo
os.listdir()        # Listar contenido de directorios
os.remove()         # Eliminar archivos
os.path.getmtime()  # Obtener fecha de modificación
os.path.getsize()   # Obtener tamaño de archivo
```

#### `time` - Manejo de Tiempo
**¿Por qué se usa?**
- Calcular antigüedad de archivos
- Comparar fechas
- Convertir timestamps Unix

**Funciones utilizadas:**
```python
time.time()  # Obtener timestamp actual en segundos
# Usado para calcular: tiempo_actual - 30_dias = archivos_antiguos
```

**¿Cómo funciona el cálculo de antigüedad?**
```python
# 30 días = 30 * 24 horas * 60 minutos * 60 segundos
segundos_en_30_dias = 30 * 24 * 60 * 60  # = 2,592,000 segundos
tiempo_actual = time.time()                # ej: 1738598400
tiempo_limite = tiempo_actual - segundos_en_30_dias

# Si un archivo fue modificado antes del tiempo_limite, es "antiguo"
if fecha_modificacion < tiempo_limite:
    # Eliminar archivo
```

#### `datetime` - Fechas y Horas
**¿Por qué se usa?**
- Formatear fechas para mostrar al usuario
- Convertir timestamps a formato legible

**Funciones utilizadas:**
```python
datetime.now()                    # Fecha y hora actual
datetime.fromtimestamp()          # Convertir timestamp a fecha
.strftime('%d/%m/%Y %H:%M:%S')   # Formatear: 03/02/2026 15:30:45
```

#### `argparse` - Argumentos de Línea de Comandos
**¿Por qué se usa?**
- Crear interfaces CLI profesionales
- Procesar argumentos y opciones
- Generar ayuda automática

**Ejemplo de uso:**
```python
parser = argparse.ArgumentParser(description="Script de limpieza")
parser.add_argument("directorio", help="Directorio a limpiar")
parser.add_argument("--dias", type=int, default=30)
args = parser.parse_args()
```

#### `sys` - Sistema Python
**¿Por qué se usa?**
- Acceder a argumentos de línea de comandos
- Controlar el flujo de ejecución

**Funciones utilizadas:**
```python
sys.argv  # Lista de argumentos: ['script.py', 'arg1', 'arg2']
```

---

### Librerías Externas (Requieren instalación)

#### `requests` - Cliente HTTP
**Versión:** 2.31.0

**¿Por qué se usa?**

`requests` es **LA librería estándar de facto** para realizar peticiones HTTP en Python. Es mucho más simple y pythónica que la librería estándar `urllib`.

**Casos de uso en este proyecto:**
- 🌐 Consumir la API REST de OpenWeatherMap
- 📡 Enviar peticiones GET con parámetros
- 📥 Recibir y procesar respuestas JSON
- ⚠️ Manejar errores HTTP y de conexión
- ⏱️ Configurar timeouts de conexión

**¿Cómo funciona paso a paso?**

1. **Construcción de la URL con parámetros**
   ```python
   ciudad = "Madrid"
   API_KEY = "tu_api_key"
   URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
   # Resultado: http://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=...&units=metric
   ```

2. **Envío de petición HTTP GET**
   ```python
   respuesta = requests.get(URL, timeout=10)
   # Envía petición al servidor
   # timeout=10 significa que esperará máximo 10 segundos
   ```

3. **Verificación del código de estado HTTP**
   ```python
   if respuesta.status_code == 200:
       # 200 = OK, todo bien
   elif respuesta.status_code == 404:
       # 404 = Not Found, ciudad no encontrada
   elif respuesta.status_code == 401:
       # 401 = Unauthorized, API key inválida
   ```

4. **Conversión de JSON a diccionario Python**
   ```python
   datos = respuesta.json()
   # JSON de la API:
   # {
   #   "main": {"temp": 15.5, "humidity": 60},
   #   "weather": [{"description": "cielo despejado"}]
   # }
   
   # Acceso a los datos:
   temperatura = datos['main']['temp']        # 15.5
   clima = datos['weather'][0]['description'] # "cielo despejado"
   ```

5. **Manejo de excepciones de red**
   ```python
   try:
       respuesta = requests.get(URL, timeout=10)
   except requests.exceptions.Timeout:
       print("⏱️ Tiempo de espera agotado")
   except requests.exceptions.ConnectionError:
       print("🔌 Sin conexión a Internet")
   except requests.exceptions.RequestException as e:
       print(f"❌ Error general: {e}")
   ```

**Ejemplo completo del flujo:**
```python
import requests

def obtener_clima(ciudad):
    # 1. Preparar URL
    API_KEY = "9c216ad30f4189183a77d9bab672ef1d"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
    
    try:
        # 2. Enviar petición
        respuesta = requests.get(URL, timeout=10)
        
        # 3. Verificar código de estado
        if respuesta.status_code == 200:
            # 4. Convertir JSON a diccionario
            datos = respuesta.json()
            
            # 5. Extraer datos específicos
            temp = datos['main']['temp']
            clima = datos['weather'][0]['description']
            
            # 6. Mostrar resultado
            print(f"Temperatura: {temp}°C")
            print(f"Condición: {clima}")
        else:
            print(f"Error HTTP {respuesta.status_code}")
            
    except requests.exceptions.Timeout:
        print("Timeout: La API no respondió a tiempo")
    except requests.exceptions.ConnectionError:
        print("Error de conexión: Verifica tu Internet")
```

**¿Por qué requests y no urllib?**

Comparación de código para hacer lo mismo:

**Con requests (simple):**
```python
import requests
respuesta = requests.get(URL)
datos = respuesta.json()
```

**Con urllib (complejo):**
```python
import urllib.request
import json
req = urllib.request.Request(URL)
with urllib.request.urlopen(req) as response:
    datos = json.loads(response.read().decode())
```

**Instalación:**
```bash
pip install requests
```

**Alternativas consideradas:**
- ❌ `urllib` - Incluida en Python pero más compleja y verbosa
- ❌ `httpx` - Moderna pero menos establecida, overkill para este caso
- ❌ `aiohttp` - Para operaciones asíncronas, innecesario aquí

---

## 🚀 Uso

### Scripts Originales (Versión Simple)

#### 1. Consulta de Clima

```bash
# Instalar dependencias primero
pip install requests

# Ejecutar el script
python3 consulta_api.py
```

**Salida esperada:**
```
--- Reporte para Madrid ---
Temperatura: 12.5°C
Condición: nubes dispersas
```

**Personalizar la ciudad:**
Edita la línea 26 del archivo:
```python
obtener_clima("Madrid")  # Cambia "Madrid" por tu ciudad
```

#### 2. Limpieza de Archivos

```bash
# Crear carpeta de prueba
mkdir mi_carpeta_de_logs

# Ejecutar el script
python3 Limepieza_archivos.py
```

**Personalizar el directorio:**
Edita la línea 31 del archivo:
```python
limpiar_descargas('./mi_carpeta_de_logs')  # Cambia la ruta
```

---

### Scripts Mejorados (Versión Avanzada)

#### 1. Consulta de Clima Mejorada

**Modo Interactivo:**
```bash
python3 consulta_clima_mejorado.py
```

**Modo CLI (una ciudad):**
```bash
python3 consulta_clima_mejorado.py Madrid
python3 consulta_clima_mejorado.py "Santo Domingo"
```

#### 2. Limpieza de Archivos Mejorada

**Vista Previa (Seguro - No elimina):**
```bash
python3 limpieza_archivos_mejorado.py /tmp
python3 limpieza_archivos_mejorado.py /tmp --dias 60
python3 limpieza_archivos_mejorado.py /tmp --extensiones .log .tmp
```

**Eliminación Real:**
```bash
# ⚠️ CUIDADO: Esto SÍ elimina archivos
python3 limpieza_archivos_mejorado.py /tmp --dias 30 --ejecutar
```

#### 3. Monitor de Sistema Integrado

```bash
# Reporte básico
python3 monitor_sistema_integrado.py

# Personalizado
python3 monitor_sistema_integrado.py \
  --ciudad "Santo Domingo" \
  --directorios /tmp ~/Downloads \
  --log /var/log/sistema.log
```

---



---

## 📸 Ejemplos de Ejecución

### Consulta de Clima

```bash
$ python3 consulta_clima_mejorado.py "Barcelona"

🔍 Consultando clima para: Barcelona...

==================================================
📍 REPORTE METEOROLÓGICO: BARCELONA
⏰ Fecha: 03/02/2026 15:32:10
==================================================
🌡️  Temperatura: 15.8°C
   ├─ Mínima: 13.5°C
   ├─ Máxima: 17.2°C
   └─ Sensación térmica: 14.9°C
☁️  Condición: Cielo despejado
💧 Humedad: 58%
🌬️  Viento: 2.1 m/s
🔽 Presión: 1015 hPa
==================================================
```

### Limpieza de Archivos

```bash
$ python3 limpieza_archivos_mejorado.py /tmp --dias 30

======================================================================
🧹 LIMPIEZA DE ARCHIVOS ANTIGUOS - SIMULACIÓN
======================================================================
📁 Directorio: /tmp
📅 Eliminar archivos anteriores a: 03/01/2026 15:30:00
⏰ Antigüedad mínima: 30 días
======================================================================

👁️  antiguo_log.log
   ├─ Última modificación: 15/12/2025 10:20:30
   ├─ Antigüedad: 50.2 días
   └─ Tamaño: 2.45 MB
   ⚠️  Se eliminaría en modo real

======================================================================
📊 RESUMEN DE LA OPERACIÓN
======================================================================
📁 Archivos analizados: 156
🗑️  Archivos que se eliminarían: 23
💾 Espacio a liberar: 145.67 MB
❌ Errores: 0
======================================================================
```

---

## ⏰ Automatización con Cron

Para ejecutar los scripts automáticamente en horarios específicos:

```bash
# Editar crontab
crontab -e
```

**Ejemplos de tareas programadas:**

```bash
# Clima diario a las 8 AM
0 8 * * * /usr/bin/python3 /ruta/consulta_clima_mejorado.py "Madrid" >> /var/log/clima.log 2>&1

# Limpieza semanal (domingos a las 2 AM)
0 2 * * 0 /usr/bin/python3 /ruta/limpieza_archivos_mejorado.py /tmp --dias 7 --ejecutar >> /var/log/limpieza.log 2>&1

# Reporte diario del sistema a las 9 AM
0 9 * * * /usr/bin/python3 /ruta/monitor_sistema_integrado.py >> /var/log/sistema.log 2>&1
```

**Sintaxis de Cron:**
```
* * * * * comando
│ │ │ │ │
│ │ │ │ └─── Día de la semana (0-7, 0 y 7 = domingo)
│ │ │ └───── Mes (1-12)
│ │ └─────── Día del mes (1-31)
│ └───────── Hora (0-23)
└─────────── Minuto (0-59)
```

---

## 🎓 Conceptos DevOps Aplicados

### 1. 🤖 Automatización de Tareas
- Scripts que ejecutan procesos sin intervención manual
- Eliminación de tareas repetitivas propensas a errores
- Programación con cron para ejecución periódica

### 2. 🌐 Integración con APIs
- Consumo de servicios web RESTful
- Autenticación mediante API keys
- Procesamiento de respuestas JSON
- Manejo de códigos de estado HTTP

### 3. 📦 Gestión de Dependencias
- Uso de `pip` como gestor de paquetes
- Archivo `requirements.txt` para reproducibilidad
- Entornos virtuales para aislamiento

### 4. 🖥️ Herramientas CLI
- Argumentos de línea de comandos
- Menús interactivos
- Salida formateada

### 5. 🛡️ Programación Defensiva
- Validación de inputs
- Manejo de excepciones
- Modo de vista previa
- Mensajes de error claros

### 6. 📝 Logging y Monitoreo
- Registro de operaciones
- Estadísticas detalladas
- Trazabilidad

---

## 🔧 Solución de Problemas

### `ModuleNotFoundError: No module named 'requests'`

```bash
pip install requests
# O: pip3 install requests
# O: python3 -m pip install requests
```

### `Permission denied`

```bash
chmod +x script.py
# O ejecutar con: python3 script.py
```

### API del clima no responde

1. Verificar conexión: `ping api.openweathermap.org`
2. Obtener nueva API key en openweathermap.org
3. Verificar límites de uso en tu cuenta

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas!

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -am 'Añade mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---



---

## 🙏 Agradecimientos

- [OpenWeatherMap](https://openweathermap.org/) por la API gratuita
- La comunidad de Python
- [Requests](https://requests.readthedocs.io/) por hacer HTTP simple

---

## 📚 Recursos Adicionales

- [Python Documentation](https://docs.python.org/3/)
- [Requests Library](https://requests.readthedocs.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Real Python - Working with APIs](https://realpython.com/api-integration-in-python/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

---

<div align="center">

### ⭐ Si este proyecto te fue útil, considera darle una estrella

**Made with ❤️ and Python** 🐍

</div>