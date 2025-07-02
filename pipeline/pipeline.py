from prefect import flow, task

@task
def load_data():
    return pd.read_csv("data/processed_FD001.csv")

@task
def train_model(data):
    X = data.drop("RUL", axis=1)
    y = data["RUL"]
    model = xgb.XGBRegressor().fit(X, y)
    joblib.dump(model, "models/xgb_pipeline_model.pkl")

@flow
def training_pipeline():
    data = load_data()
    train_model(data)

training_pipeline()
