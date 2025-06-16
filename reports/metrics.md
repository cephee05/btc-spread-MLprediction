# Modèle LightGBM – Résultats de test

- **MAE test** : 33.440224  
- **RMSE test** : 54.483306  
- **R² test**  : 0.1846  

_Les métriques sont calculées sur le jeu de données de test après entraînement avec early stopping._

### Learning Curve
![image](https://github.com/user-attachments/assets/622fb963-ad09-4957-949f-6399cd41d3da)

### Prédiction vs Réel
![image](https://github.com/user-attachments/assets/6466d199-e030-4f0a-ba3f-22c25159eb27)

### Distribution des résidus
![image](https://github.com/user-attachments/assets/0d0f3b62-e7aa-4856-820b-0030719e8a78)

### Importance des features (Top 20)
![image](https://github.com/user-attachments/assets/94e674ab-8138-4444-bdf5-a6699d91a853)

**Conclusion**

The LightGBM model delivers a test MAE of **33.44 ticks** (≈ 0.334 USDT) and an RMSE of **54.48 ticks**, capturing about **18.5 %** of the spread’s variance (R² = 0.1846). The learning curves show smooth, parallel declines in training and validation MAE, indicating good generalization without significant overfitting. Residuals are mostly within ±10 ticks, though a few large outliers remain. Feature importance confirms that longer-term spread averages and volume are the strongest predictors, while momentum and volatility features add incremental value.

Overall, this model forms a solid baseline for spread prediction in market-making. Future improvements could include outlier handling, richer order-book–based features, or sequence models (e.g., LSTM) to better capture temporal dynamics.
