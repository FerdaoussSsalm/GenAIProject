def detect_swings(df, window=30):
    df = df.copy()
    df['swing_high'] = df['High'].rolling(window=window).max()
    df['swing_low'] = df['Low'].rolling(window=window).min()
    return df
