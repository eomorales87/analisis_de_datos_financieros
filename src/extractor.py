import requests
import pandas as pd
import time
import os
from typing import Dict

class StockDataExtractor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_stock_data(self, symbol: str) -> pd.DataFrame:
        url = f"{self.base_url}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={self.api_key}&outputsize=compact"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if "Time Series (Daily)" not in data:
                raise ValueError("Respuesta inválida de la API")

            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index", dtype=float)
            df = df.rename(columns={
                "1. open": "Open",
                "2. high": "High",
                "3. low": "Low",
                "4. close": "Close",
                "6. volume": "Volume"
            })
            df.index.name = "Date"
            df.reset_index(inplace=True)
            return df

        except Exception as e:
            print(f"Error obteniendo datos: {e}")
            return pd.DataFrame()

    def save_to_csv(self, df: pd.DataFrame, symbol: str) -> None:
        os.makedirs("data/raw", exist_ok=True)
        path = f"data/raw/{symbol}.csv"
        df.to_csv(path, index=False)
        print(f"Datos guardados en {path}")
