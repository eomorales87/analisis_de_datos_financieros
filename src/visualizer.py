import matplotlib.pyplot as plt
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, df: pd.DataFrame, symbol: str):
        self.df = df
        self.symbol = symbol
        os.makedirs("results/plots", exist_ok=True)

    def plot_prices_with_sma(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.df["Date"], self.df["Close"], label="Close Price")
        if "SMA_20" in self.df.columns:
            plt.plot(self.df["Date"], self.df["SMA_20"], label="SMA 20")
        if "SMA_50" in self.df.columns:
            plt.plot(self.df["Date"], self.df["SMA_50"], label="SMA 50")
        plt.title(f"{self.symbol} - Precio con Medias Móviles")
        plt.xlabel("Fecha")
        plt.ylabel("Precio")
        plt.legend()
        plt.xticks(rotation=45)
        path = f"results/plots/{self.symbol}_sma.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")

    def plot_volatility(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.df["Date"], self.df["Volatility"], label="Volatility")
        plt.title(f"{self.symbol} - Volatilidad")
        plt.xlabel("Fecha")
        plt.ylabel("Volatilidad")
        plt.legend()
        plt.xticks(rotation=45)
        path = f"results/plots/{self.symbol}_volatility.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")

    def plot_histogram_returns(self):
        if "Daily_Return" not in self.df.columns:
            print("No hay rendimientos calculados.")
            return
        plt.figure(figsize=(8,5))
        self.df["Daily_Return"].dropna().hist(bins=30, edgecolor="black")
        plt.title(f"{self.symbol} - Histograma de Rendimientos Diarios")
        plt.xlabel("Rendimiento")
        plt.ylabel("Frecuencia")
        path = f"results/plots/{self.symbol}_returns_hist.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")

    @staticmethod
    def plot_correlation(dfs: dict):
        """Recibe un diccionario { 'AAPL': df1, 'MSFT': df2, ... }"""
        returns = pd.DataFrame({symbol: df["Close"].pct_change() for symbol, df in dfs.items()})
        corr = returns.corr()

        plt.figure(figsize=(6,5))
        plt.imshow(corr, cmap="coolwarm", interpolation="none")
        plt.colorbar(label="Correlación")
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
        plt.yticks(range(len(corr.index)), corr.index)
        plt.title("Matriz de Correlación de Rendimientos")
        path = "results/plots/correlation_matrix.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")
import matplotlib.pyplot as plt
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, df: pd.DataFrame, symbol: str):
        self.df = df
        self.symbol = symbol
        os.makedirs("results/plots", exist_ok=True)

    def plot_prices_with_sma(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.df["Date"], self.df["Close"], label="Close Price")
        if "SMA_20" in self.df.columns:
            plt.plot(self.df["Date"], self.df["SMA_20"], label="SMA 20")
        if "SMA_50" in self.df.columns:
            plt.plot(self.df["Date"], self.df["SMA_50"], label="SMA 50")
        plt.title(f"{self.symbol} - Precio con Medias Móviles")
        plt.xlabel("Fecha")
        plt.ylabel("Precio")
        plt.legend()
        plt.xticks(rotation=45)
        path = f"results/plots/{self.symbol}_sma.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")

    def plot_volatility(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.df["Date"], self.df["Volatility"], label="Volatility")
        plt.title(f"{self.symbol} - Volatilidad")
        plt.xlabel("Fecha")
        plt.ylabel("Volatilidad")
        plt.legend()
        plt.xticks(rotation=45)
        path = f"results/plots/{self.symbol}_volatility.png"
        plt.savefig(path)
        plt.close()
        print(f"Gráfico guardado en {path}")
