import os
import sys
import types
import pandas as pd

# Asegurar que src esté en el path
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from extractor import StockDataExtractor

def test_get_stock_data_success(monkeypatch):
    class MockResponse:
        def raise_for_status(self): 
            return None
        def json(self):
            return {
                "Time Series (Daily)": {
                    "2025-08-26": {
                        "1. open": "1.00",
                        "2. high": "2.00",
                        "3. low": "0.50",
                        "4. close": "1.50",
                        "6. volume": "1000"
                    }
                }
            }
    def mock_get(url):
        return MockResponse()

    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    extractor = StockDataExtractor(api_key="test")
    df = extractor.get_stock_data("AAPL")
    assert not df.empty
    expected_cols = {"Date","Open","High","Low","Close","Volume"}
    assert expected_cols.issubset(set(df.columns))

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({
        "Date": ["2025-08-26"],
        "Open": [1.0],
        "High": [2.0],
        "Low": [0.5],
        "Close": [1.5],
        "Volume": [1000]
    })
    # Cambiar a un directorio temporal para pruebas
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        os.makedirs("data/raw", exist_ok=True)
        extractor = StockDataExtractor(api_key="x")
        extractor.save_to_csv(df, "TEST")
        assert os.path.exists(os.path.join("data","raw","TEST.csv"))
    finally:
        os.chdir(cwd)
