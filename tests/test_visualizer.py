import os
import sys
import numpy as np
import pandas as pd

# Usar backend 'Agg' para ambientes sin display
import matplotlib
matplotlib.use("Agg", force=True)

# Asegurar que src esté en el path
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from visualizer import DataVisualizer

def test_visualizations(tmp_path):
    dates = pd.date_range("2025-06-01", periods=30, freq="D").strftime("%Y-%m-%d")
    close = np.linspace(100, 120, 30)
    df = pd.DataFrame({
        "Date": dates,
        "Close": close
    })
    # Añadir columnas para que no falle el graficado de SMAs/Volatilidad
    df["SMA_20"] = pd.Series(close).rolling(20).mean()
    df["SMA_50"] = pd.Series(close).rolling(20).mean()  # dummy
    df["Volatility"] = pd.Series(close).pct_change().rolling(20).std()

    # Cambiar cwd para que 'results/plots' se cree en tmp_path
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        viz = DataVisualizer(df, "TEST")
        viz.plot_prices_with_sma()
        viz.plot_volatility()
        assert os.path.exists(os.path.join("results","plots","TEST_sma.png"))
        assert os.path.exists(os.path.join("results","plots","TEST_volatility.png"))
    finally:
        os.chdir(cwd)
