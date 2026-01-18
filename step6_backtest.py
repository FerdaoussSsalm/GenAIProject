def backtest(df, capital=10000):
    df = df.copy()
    df['position'] = 0
    df['returns'] = 0.0

    # BUY = 1, SELL = -1
    df.loc[df['signal']=='BUY', 'position'] = 1
    df.loc[df['signal']=='SELL', 'position'] = -1

    # Shift position pour éviter lookahead
    df['position'] = df['position'].shift(1).fillna(0)

    # Returns journaliers
    df['returns'] = df['Close'].pct_change() * df['position']
    df['capital'] = (1 + df['returns']).cumprod() * capital

    # Drawdown
    df['cummax'] = df['capital'].cummax()
    df['drawdown'] = df['capital'] / df['cummax'] - 1

    # -----------------------------
    # Crée un DataFrame des trades (lignes où signal est BUY ou SELL)
    trades = df[df['signal'].isin(['BUY','SELL'])].copy()
    print("Nombre de trades générés:", len(trades))
    return df, trades   # <-- retourne les deux
