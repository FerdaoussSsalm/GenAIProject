# Trading Pipeline — GC=F & NASDAQ (IA + Fibonacci + Indicateurs Techniques)

Ce projet implémente une pipeline complète d'analyse et de génération de signaux de trading appliquée à l'Or (**GC=F**) et au **NASDAQ**.  
Il combine indicateurs techniques classiques, retracements de Fibonacci et un système de recommandation textuelle afin d'obtenir des signaux exploitables.  
Un dashboard Streamlit permet de visualiser les résultats ainsi que le backtest et les métriques associées.

---

## 🎯 Objectifs du projet

- Télécharger et nettoyer des données financières (GC=F, IXIC)
- Calculer plusieurs indicateurs techniques
- Détecter swings locaux
- Générer niveaux de Fibonacci
- Produire signaux BUY / SELL
- Backtester la stratégie (capital, drawdown, win rate)
- Produire recommandations textuelles
- Comparer GC vs NASDAQ via un dashboard interactif

---

## 🧰 Technologies utilisées

- Python 3.x
- `yfinance`
- `pandas`
- `numpy`
- `matplotlib`
- `streamlit`
- (optionnel) Google Colab

---

## 📁 Structure du repository
├── step1_collect.py
├── step2_indicators.py
├── step3_swings.py
├── step4_fibonacci.py
├── step5_signals.py
├── step6_backtest.py
├── step7_metrics.py
├── dashboard_colab.py
├── sample_data/
├── trades_GCF.csv
├── trades_IXIC.csv
└── README.md


---

## 🛠 Installation

Cloner le repo :

```sh
git clone https://github.com/<username>/<repo>.git
cd <repo>

##Installer les dépendances :
yfinance
pandas
numpy
streamlit
matplotlib

##Exécution du pipeline

Pour lancer le pipeline complet sur un instrument :

from step1_pipeline import run_pipeline
df, trades = run_pipeline("GC=F")

##Dashboard interactif (Streamlit)

Pour afficher la comparaison GC vs NASDAQ :

streamlit run dashboard_colab.py

##Le dashboard permet de :

✔ visualiser le prix + signaux
✔ afficher les trades
✔ analyser le backtest
✔ comparer GC vs NASDAQ
✔ afficher les recommandations textuelles

📈 Exemple de signaux générés
BUY si prix < fib_0.382 & RSI < 40
SELL si prix > fib_0.618 & RSI > 60
HOLD sinon

🧪 Backtest & Evaluation

Le backtest calcule :

capital final

rendement cumulatif

drawdown max

win rate

nombre de trades

Exemple d'utilisation :

from step6_backtest import backtest
df_bt, trades = backtest(df)

📗 Manuel d'utilisation

1. Choisir un instrument

GC=F → Or

^IXIC → Nasdaq

2. Lancer le pipeline

df, trades = run_pipeline("GC=F")


3. Lancer le dashboard

streamlit run dashboard_colab.py


4. Interpréter

Zones de Fibonacci = supports/résistances probables

RSI = momentum/surachat/survente

Signaux BUY/SELL = opportunités potentielles

Win rate = qualité de la stratégie

Drawdown = risque

📦 Jeux de données fournis

trades_GCF.csv

trades_IXIC.csv

Contiennent :

Date, Signal, Price, RSI, Fibonacci Level, PnL...

🔄 Instruments comparés
Instrument	Type	Classe
GC=F	Futures Or	Actif refuge
^IXIC	Nasdaq Composite	Indice techno

🛡 Limitations connues

Stratégie simple (indic + fibo) → améliorable
Pas de gestion du slippage
Pas de coûts de transaction
Pas d'optimisation dynamique

📌 Pistes d'amélioration

Utiliser une IA générative pour enrichir les signaux
Ajouter LSTM/Transformer pour prédiction
Intégrer du sentiment market/news
Couvrir plusieurs horizons temporels

