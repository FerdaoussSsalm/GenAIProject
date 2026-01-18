def add_recommendations(df):
    df = df.copy()  # Assurez-vous que df est un DataFrame
    df.sort_index(inplace=True)

    # Exemple simple de recommandation IA basée sur signaux et RSI
    def generate_text(row):
        if row['signal'] == 'BUY':
            return f"Strong BUY signal: RSI={row['rsi']:.1f}, price near fib_0.382={row['fib_0.382']:.2f}"
        elif row['signal'] == 'SELL':
            return f"Strong SELL signal: RSI={row['rsi']:.1f}, price near fib_0.618={row['fib_0.618']:.2f}"
        else:
            return "No clear signal - HOLD"

    df['recommendation'] = df.apply(generate_text, axis=1)
    
    return df  # ← uniquement le DataFrame, pas un tuple
