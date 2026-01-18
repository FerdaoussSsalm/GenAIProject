import pandas as pd
def generate_signals(df):
    df = df.copy()

    # On s'assure d'un index simple
    if isinstance(df.index, pd.MultiIndex):
        df = df.reset_index(level=0, drop=True)
    df.sort_index(inplace=True)

    df['signal'] = 'HOLD'

    # Colonnes techniques
    close = df['Close']
    rsi = df['rsi']
    fib_382 = df['fib_0.382']
    fib_618 = df['fib_0.618']

    df.loc[(close < fib_382) & (rsi < 40), 'signal'] = 'BUY'
    df.loc[(close > fib_618) & (rsi > 60), 'signal'] = 'SELL'

    return df
