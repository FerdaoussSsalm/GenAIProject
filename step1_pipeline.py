# ----------------------------
# 0️⃣ Imports
# ----------------------------
import pandas as pd
from step1_collect import get_data
from step2_indicators import add_indicators
from step3_swings import detect_swings
from step4_fibonacci import apply_fibonacci
from step5_signals import generate_signals
from step6_backtest import backtest
from step7_metrics import add_recommendations

# ----------------------------
# 1️⃣ Fonction pipeline complète
# ----------------------------
def run_pipeline(symbol: str, capital: float = 10000):
    # 1️⃣ Collecte
    df = get_data(symbol)
    
    # 2️⃣ Indicateurs
    df = add_indicators(df)
    df['signal'] = 'NEUTRAL'  # par défaut

    # RSI < 30 → BUY, RSI > 70 → SELL
    df.loc[df['rsi'] < 30, 'signal'] = 'BUY'
    df.loc[df['rsi'] > 70, 'signal'] = 'SELL'

    # Vérifier
    print(df['signal'].value_counts())

    # 3️⃣ Swings
    df = detect_swings(df)
    
    # 4️⃣ Fibonacci
    df = apply_fibonacci(df)
    
    # 4b️⃣ Nettoyage MultiIndex si nécessaire
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    if isinstance(df.index, pd.MultiIndex):
        df = df.reset_index(level=0, drop=True)
    
    df.sort_index(inplace=True)  # Tri par date
    
    # 5️⃣ Signaux
    df = generate_signals(df)
    
    # 6️⃣ Backtesting
    df, trades = backtest(df)   # maintenant trades est un DataFrame
    nb_trades = df['signal'].isin(['BUY', 'SELL']).sum()
    print("Nombre de trades générés:", nb_trades)
   
    
    # 7️⃣ Recommandations IA
    df = add_recommendations(df)
    
    return df, trades

# ----------------------------
# 2️⃣ Exécution pour Or et Nasdaq
# ----------------------------
symbols = ["GC=F", "^IXIC"]
results = {}

for sym in symbols:
    print(f"\n===== Pipeline pour {sym} =====")
    df, trades = run_pipeline(sym)
    results[sym] = {"df": df, "trades": trades}
    
    # Aperçu
    print(df[['Close','fib_0.382','fib_0.618','signal','capital','drawdown','recommendation']].tail(5))
    nb_trades = df['signal'].isin(['BUY', 'SELL']).sum()
    print("Nombre de trades générés:",nb_trades )

# ----------------------------
# 3️⃣ Accès aux données
# ----------------------------
# Par exemple, pour Or
df_gold = results["GC=F"]["df"]
trades_gold = results["GC=F"]["trades"]
print("les trades OR :",df_gold)
# Pour Nasdaq
df_nasdaq = results["^IXIC"]["df"]
trades_nasdaq = results["^IXIC"]["trades"]
print("les trades Nasdaq :",df_nasdaq)


