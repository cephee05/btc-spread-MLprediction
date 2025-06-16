# btc-spread-MLprediction
This project presents a machine learning model designed to predict the BTC/USDT bid-ask spread at a one-minute resolution.

Ce projet met en place le pipeline ML complet pour prédire le spread BTCUSDT sur des données 1-minute.

- **data/**
  - **raw/**: place your raw OHLC CSV files here (format: `datetime,open,high,low,close,volume`).
  - **processed/**: automatically populated by `src/train.py` with feature CSVs.
  - **README.md**: instructions for adding raw CSVs and generating processed features.
- **src/**
  - `utils.py`: loading and preprocessing functions (e.g., load_ohlc).
  - `train.py`: trains the LightGBM model, exports feature CSV to `data/processed/`, and saves the model to `models/`.
  - `predict.py`: loads the trained model and generates spread predictions from processed features.
- **models/**
  - `btc_spread_lgbm.pkl`: trained model file (use Git LFS for large files).
- **reports/**
  - `metrics.md`: stores MAE, RMSE, R² metrics and key performance plots.
- **Makefile**: defines shortcuts:
  - `make setup`: install dependencies
  - `make train`: run training pipeline
  - `make predict`: run prediction script
- **requirements.txt**: Python dependencies with version pinning.
- **LICENSE**: MIT license.

## Quickstart

```bash
git clone https://github.com/ton-user/btc-spread-ml.git
cd btc-spread-ml
make setup
