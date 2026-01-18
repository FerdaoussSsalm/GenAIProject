import yfinance as yf
import pandas as pd

def get_data(symbol, start="2000-01-01"):
    df = yf.download(symbol, start=start, auto_adjust=False)

    if df is None or len(df) == 0:
        raise ValueError(f"Yahoo Finance returned no data for {symbol}")

    # -------- FIX MultiIndex Yahoo pour indices --------
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # -------- Vérif Volume sinon création --------
    if "Volume" not in df.columns:
        df["Volume"] = 0

    # -------- On garde OHLCV --------
    expected_cols = ["Open","High","Low","Close","Volume"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' missing in data for {symbol}")

    df = df[expected_cols]

    # -------- Nettoyage --------
    df.dropna(inplace=True)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    return df
