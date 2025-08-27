import os
from extractor import StockDataExtractor
from processor import DataProcessor
from visualizer import DataVisualizer
from dotenv import load_dotenv

def main():
    # Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    symbol = "AAPL"

    # 1. Extracción de datos
    extractor = StockDataExtractor(api_key)
    df = extractor.get_stock_data(symbol)
    extractor.save_to_csv(df, symbol)

    # 2. Procesamiento de datos
    processor = DataProcessor(df)
    df = processor.add_moving_averages([20, 50])
    df = processor.calculate_volatility(20)
    df = processor.calculate_returns()
    stats = processor.basic_stats()

    # Guardar reporte
    os.makedirs("results/reports", exist_ok=True)
    report_path = f"results/reports/{symbol}_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Reporte de Análisis - {symbol}\n\n")
        f.write("## Estadísticas Básicas\n")
        for k, v in stats.items():
            f.write(f"- **{k}**: {v:.2f}\n")
    print(f"Reporte generado en {report_path}")

    # 3. Visualización
    visualizer = DataVisualizer(df, symbol)
    visualizer.plot_prices_with_sma()
    visualizer.plot_volatility()
    visualizer.plot_histogram_returns()
    # Nota: el gráfico de correlación requiere múltiples acciones cargadas

if __name__ == "__main__":
    main()
import os
from extractor import StockDataExtractor
from processor import DataProcessor
from visualizer import DataVisualizer

def main():
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")  # Guardar API key en .env
    symbol = "AAPL"

    # 1. Extracción de datos
    extractor = StockDataExtractor(api_key)
    df = extractor.get_stock_data(symbol)
    extractor.save_to_csv(df, symbol)

    # 2. Procesamiento de datos
    processor = DataProcessor(df)
    df = processor.add_moving_averages([20, 50])
    df = processor.calculate_volatility(20)
    df = processor.calculate_returns()
    stats = processor.basic_stats()
    print("Estadísticas básicas:", stats)

    # 3. Visualización
    visualizer = DataVisualizer(df, symbol)
    visualizer.plot_prices_with_sma()
    visualizer.plot_volatility()

if __name__ == "__main__":
    main()
