def apply_fibonacci(df):
    df = df.copy()
    ratios = [0.236, 0.382, 0.5, 0.618, 0.786]
    for r in ratios:
        df[f'fib_{r}'] = df['swing_high'] - (df['swing_high'] - df['swing_low']) * r
    # Forward/backward fill pour éviter les NaN
    fib_cols = [c for c in df.columns if c.startswith('fib_')]
    df[fib_cols] = df[fib_cols].ffill().bfill()
    return df
