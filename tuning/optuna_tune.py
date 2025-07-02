import optuna
from sklearn.model_selection import cross_val_score

def objective(trial):
    max_depth = trial.suggest_int("max_depth", 3, 10)
    learning_rate = trial.suggest_float("learning_rate", 0.01, 0.3)
    n_estimators = trial.suggest_int("n_estimators", 50, 300)

    model = xgb.XGBRegressor(max_depth=max_depth,
                             learning_rate=learning_rate,
                             n_estimators=n_estimators)
    
    scores = cross_val_score(model, X, y, scoring='neg_root_mean_squared_error', cv=3)
    return -1 * scores.mean()

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=20)
