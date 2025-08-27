import os
import sys
import numpy as np
import pandas as pd

# Asegurar que src esté en el path
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from processor import DataProcessor

def test_processor_pipeline():
    # Crear datos de cierre de 60 días
    dates = pd.date_range("2025-06-01", periods=60, freq="D").strftime("%Y-%m-%d")
    close = np.arange(1, 61, dtype=float)  # 1,2,...,60
    df = pd.DataFrame({"Date": dates, "Close": close})

    p = DataProcessor(df)
    df2 = p.add_moving_averages([20,50])
    df2 = p.calculate_returns()
    df2 = p.calculate_volatility(20)

    # Columnas creadas
    for col in ["SMA_20","SMA_50","Daily_Return","Volatility"]:
        assert col in df2.columns

    # Validar primer valor no nulo de SMA_20
    first_valid_idx = df2["SMA_20"].first_valid_index()
    expected = close[0:20].mean()
    assert np.isclose(df2.loc[first_valid_idx, "SMA_20"], expected, atol=1e-9)
