# Proyecto: Análisis de Datos Financieros con Python

Este proyecto implementa un sistema de análisis financiero utilizando datos históricos de acciones obtenidos desde la API de Alpha Vantage.

## 📂 Estructura del Proyecto
```
proyecto/
│
├── src/
│   ├── extractor.py      # Extracción de datos desde Alpha Vantage
│   ├── processor.py      # Procesamiento de datos (estadísticos, medias móviles, volatilidad)
│   ├── visualizer.py     # Visualizaciones con matplotlib
│   └── main.py           # Script principal
│
├── data/
│   └── raw/              # CSVs descargados o de ejemplo
│       └── AAPL.csv
│
├── results/
│   ├── plots/            # Gráficas generadas
│   └── reports/          # Reportes en formato markdown
│
├── tests/
│   ├── test_extractor.py
│   ├── test_processor.py
│   └── test_visualizer.py
```

## 🚀 Instalación

1. Clonar el repositorio o descomprimir el archivo ZIP.
2. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate    # En Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

> Si no existe el archivo `requirements.txt`, puedes instalar manualmente:
```bash
pip install pandas numpy matplotlib requests python-dotenv
```

## 🔑 Configuración de la API Key

1. Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
ALPHAVANTAGE_API_KEY=tu_api_key_aqui
```

2. Puedes obtener una API key gratuita en [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

## ▶️ Ejecución

Ejecutar el script principal:

```bash
python src/main.py
```

Esto realizará:
- Descarga de datos históricos de la acción configurada (`AAPL` por defecto).
- Guardado en `data/raw/AAPL.csv`.
- Procesamiento de indicadores financieros.
- Generación de gráficas en `results/plots/`.

## 📊 Funcionalidades

- Cálculo de medias móviles (20 y 50 días).
- Cálculo de volatilidad histórica.
- Rendimientos diarios.
- Estadísticas básicas (media, máximo, mínimo, desviación estándar).
- Visualizaciones (precios con SMA, volatilidad, etc.).

## 📌 Notas

- Puedes cambiar el símbolo de la acción en `src/main.py` (`symbol = "AAPL"`).
- Si la API limita el acceso, el proyecto incluye un CSV de ejemplo (`AAPL.csv`) para pruebas.
