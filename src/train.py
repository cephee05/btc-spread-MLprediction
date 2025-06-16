import pandas as pd
import joblib
from sklearn.model_selection import TimeSeriesSplit, RandomizedSearchCV
from lightgbm import LGBMRegressor

# 1) Charger les features pré-calculées
# Assurez-vous que le CSV contient toutes les features dérivées et la colonne 'target_spread'
df_feat = pd.read_csv(
    r'C:\Users\\BTCUSDT-1m-features.csv',
    parse_dates=['datetime'], index_col='datetime'
)
df_feat.sort_index(inplace=True)

# 2) Préparer X et y pour le tuning
X_tune = df_feat.drop(columns=['target_spread'], errors='ignore')
y_tune = df_feat['target_spread'].astype(float)

# 3) Configurer la validation croisée temporelle
tscv = TimeSeriesSplit(n_splits=5)

# 4) Définir la grille de paramètres pour RandomizedSearchCV
param_dist = {
    'learning_rate': [0.01, 0.05, 0.1],
    'num_leaves': [31, 63, 127],
    'max_depth': [5, 8, 12, -1],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'reg_alpha': [0, 0.1, 1.0],
    'reg_lambda': [0, 0.1, 1.0]
}

# 5) Lancer la recherche aléatoire
model = LGBMRegressor(
    objective='huber',
    metric='l1',
    n_estimators=500,
    random_state=42
)
search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=20,
    cv=tscv,
    scoring='neg_mean_absolute_error',
    verbose=2,
    n_jobs=-1,
    random_state=42
)
print("Début de l'optimisation des hyperparamètres...")
search.fit(X_tune, y_tune)

# 6) Afficher et sauvegarder les meilleurs paramètres
print("Meilleurs paramètres trouvés :", search.best_params_)
best_model = search.best_estimator_
joblib.dump(best_model, 'best_lgbm_model.pkl')
print("Modèle optimisé sauvegardé sous 'best_lgbm_model.pkl'.")

