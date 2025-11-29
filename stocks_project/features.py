# Function to create features for modeling stock prices

import pandas as pd
import numpy as np

def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add basic features: Daily Return, Moving Averages, and Volatility.
    """

    df = df.copy()

    # How much the price changed from the previous day
    df['daily_return'] = df['adj_close'].pct_change()

    # 7-day and 21-day moving averages
    df['ma_7'] = df['adj_close'].rolling(window=7).mean()
    df['ma_21'] = df['adj_close'].rolling(window=21).mean()

    # Volatility: Standard deviation of daily returns over the past 21 days
    df['volatility_21'] = df['daily_return'].rolling(window=21).std()

    return df

def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add lag features for the previous 1, 2, and 3 days' adjusted close prices.
    """
    df = df.copy()
    df['lag_1'] = df['adj_close'].shift(1)
    df['lag_2'] = df['adj_close'].shift(2)
    df['lag_3'] = df['adj_close'].shift(3)
    df['lag_7'] = df['adj_close'].shift(7)
    df['lag_14'] = df['adj_close'].shift(14)
    return df

def add_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """
    Add RSI (Relative Strength Index) feature.
    """
    df = df.copy()
    delta = df['adj_close'].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / (avg_loss + 1e-10)
    df['rsi_14'] = 100 - (100 / (1 + rs))
    return df

def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add MACD and MACD Signal features.
    """
    df = df.copy()
    short_ema = df['adj_close'].ewm(span=12, adjust=False).mean()
    long_ema = df['adj_close'].ewm(span=26, adjust=False).mean()
    df['macd'] = short_ema - long_ema
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    return df

def add_bollinger_width(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Add Bollinger Band width feature.
    """
    df = df.copy()
    mid = df['adj_close'].rolling(window=window).mean()
    std = df['adj_close'].rolling(window=window).std()
    upper = mid + (std * 2)
    lower = mid - (std * 2)
    df['bb_width'] = (upper - lower)
    return df

def add_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add target column: Next day's closing price.
    """
    df = df.copy()
    df['target_next_close'] = df['adj_close'].shift(-1)
    return df

def build_feature_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full feature pipeline: Adds all features and drops NaNs.
    """
    df = add_basic_features(df)
    df = add_lag_features(df)
    df = add_rsi(df)
    df = add_macd(df)
    df = add_bollinger_width(df)
    df = add_target(df)

    df = df.dropna().copy()
    return df