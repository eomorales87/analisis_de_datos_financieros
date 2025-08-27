import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def add_moving_averages(self, windows=[20, 50]):
        for w in windows:
            self.df[f"SMA_{w}"] = self.df["Close"].rolling(window=w).mean()
        return self.df

    def calculate_volatility(self, window=20):
        self.df["Volatility"] = self.df["Close"].pct_change().rolling(window).std()
        return self.df

    def calculate_returns(self):
        self.df["Daily_Return"] = self.df["Close"].pct_change()
        return self.df

    def basic_stats(self) -> dict:
        return {
            "mean_close": self.df["Close"].mean(),
            "max_close": self.df["Close"].max(),
            "min_close": self.df["Close"].min(),
            "std_close": self.df["Close"].std()
        }
