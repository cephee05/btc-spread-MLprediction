# Data Directory

- **raw/**: place raw OHLC CSV files here. Required columns:
  - `datetime` (YYYY-MM-DD HH:MM:SS)
  - `open`, `high`, `low`, `close`, `volume`

- **processed/**: populated by `src/train.py`.

**Usage**:
1. Copy your raw CSV to `data/raw/`.
2. Run `make train` to generate `data/processed/BTCUSDT-1m-features.csv` and train the model.
