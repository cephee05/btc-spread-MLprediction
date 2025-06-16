# btc-spread-MLprediction
This project presents a machine learning model designed to predict the BTC/USDT bid-ask spread at a one-minute resolution.

Ce projet met en place le pipeline ML complet pour prédire le spread BTCUSDT sur des données 1-minute.

## Structure

- **data/raw/**: fichiers OHLC 1m bruts.
- **data/processed/**: features calculées prêtes à l'emploi.
- **notebooks/**:
  - `01_data_exploration.ipynb` : compréhension des données.
  - `02_feature_engineering.ipynb` : création et analyse des features.
  - `03_model_training.ipynb` : entraînement, tuning et évaluation du modèle.
- **src/utils.py**: fonctions pour charger et pré-traiter les données.
- **src/train.py**: script pour entraîner et sauvegarder le modèle LGBM.
- **src/predict.py**: script pour charger le modèle et générer des prédictions.
- **models/**: stockage du fichier `btc_spread_lgbm.pkl`.
- **reports/metrics.md**: résultats chiffrés et graphiques comparatifs.
- **Makefile**: raccourcis pour installer et lancer les scripts.

## Installation

```bash
git clone https://github.com/ton-user/btc-spread-ml.git
cd btc-spread-ml
make setup
