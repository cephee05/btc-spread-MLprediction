import pandas as pd
import joblib
import matplotlib.pyplot as plt
import lightgbm as lgb
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1) Chargement des features
df = pd.read_csv(
    r'C:\Users\\BTCUSDT-1m-features.csv',
    parse_dates=['datetime'], index_col='datetime'
)

# 2) Création de la cible : spread à t+1 minute
df['target_spread'] = df['spread'].shift(-1)

# 3) Suppression des lignes NaN (notamment la dernière)
df.dropna(inplace=True)

# 4) Séparation X / y
X = df.drop(columns=['target_spread'])
y = df['target_spread'].astype(float)

# 5) Split chronologique train / validation / test
n = len(df)
i_train = int(n * 0.70)
i_val   = int(n * 0.85)
X_train, y_train = X.iloc[:i_train],     y.iloc[:i_train]
X_val,   y_val   = X.iloc[i_train:i_val], y.iloc[i_train:i_val]
X_test,  y_test  = X.iloc[i_val:],       y.iloc[i_val:]

# 6) Instanciation du modèle optimisé avec les meilleurs paramètres
best_params = {
    'subsample':       0.8,
    'reg_lambda':      0,
    'reg_alpha':       0.1,
    'num_leaves':      127,
    'max_depth':       -1,
    'learning_rate':   0.1,
    'colsample_bytree':0.6
}
model = LGBMRegressor(
    objective='huber',
    metric='l1',
    n_estimators=500,
    random_state=42,
    **best_params
)

# 7) Entraînement avec early stopping et capture des courbes de MAE
evals_result = {}
model.fit(
    X_train, y_train,
    eval_set=[(X_train, y_train), (X_val, y_val)],
    eval_names=['train', 'valid'],
    eval_metric='l1',
    callbacks=[
        lgb.early_stopping(stopping_rounds=50, verbose=False),
        lgb.record_evaluation(evals_result)
    ]
)

# 8) Sauvegarde du modèle entraîné
joblib.dump(model, 'btc_spread_lgbm.pkl')

# 9) Évaluation sur le jeu de test
pred     = model.predict(X_test)
mae_test = mean_absolute_error(y_test, pred)
rmse_test= mean_squared_error(y_test, pred, squared=False)
r2_test  = r2_score(y_test, pred)
print(f"MAE test :  {mae_test:.6f}")
print(f"RMSE test:  {rmse_test:.6f}")
print(f"R² test  :  {r2_test:.4f}")

# 10) Tracé de la courbe d'apprentissage (MAE vs itération)
plt.figure(figsize=(8,5))
plt.plot(evals_result['train']['l1'], label='Train MAE')
plt.plot(evals_result['valid']['l1'], label='Validation MAE')
plt.xlabel('Itération')
plt.ylabel('MAE')
plt.title('LightGBM Learning Curve')
plt.legend()
plt.tight_layout()
plt.show()

# 11) Scatter plot : prédiction vs réel
plt.figure(figsize=(6,6))
plt.scatter(y_test, pred, alpha=0.3, s=10)
max_val = max(y_test.max(), pred.max())
plt.plot([0, max_val], [0, max_val], 'r--')
plt.xlabel('Spread réel')
plt.ylabel('Spread prédit')
plt.title('Prédiction vs Réel')
plt.tight_layout()
plt.show()

# 12) Histogramme des résidus
residuals = y_test - pred
plt.figure(figsize=(8,4))
plt.hist(residuals, bins=50)
plt.xlabel('Résidu (réel - prédit)')
plt.ylabel('Fréquence')
plt.title('Distribution des résidus')
plt.tight_layout()
plt.show()

# 13) Feature importance (Top 20)
fi = pd.Series(
    model.feature_importances_, index=X.columns
).sort_values(ascending=False).head(20)
plt.figure(figsize=(8,6))
fi.plot(kind='barh')
plt.gca().invert_yaxis()
plt.xlabel('Importance')
plt.title('Top 20 Features')
plt.tight_layout()
plt.show()

# 14) Moyenne historique du spread pour contexte
historical_mean = df['spread'].mean()
print(f"Spread historique moyen : {historical_mean:.2f} ticks")
