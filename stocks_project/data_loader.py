# Functions to download and prepare raw stock data

import yfinance as yf
import pandas as pd
from typing import List

def load_stock_data_yahoo(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Download OHLCV Stock data from Yahoo Finance from given tickers.
    Returns a DataFrame with MultiIndex columns.
    """

    data = yf.download(tickers, start=start, end=end)
    return data

def get_single_ticker_df(data: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """
    Extract a Single Stock's Adjusted Close Price as a simple DataFrame.
    """
    df = data['Close'][ticker].to_frame(name='Adj Close')
    return df

def show_basic_info(df: pd.DataFrame, name: str = "Data") -> None:
    """
    Print basic information about the DataFrame.
    """
    print(f"=== {name} shape ===")
    print(df.shape)
    print("\n=== Head ===")
    print(df.head())
    print("\n=== Missing values per column ===")
    print(df.isna().sum())   