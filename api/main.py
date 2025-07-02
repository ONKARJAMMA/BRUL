from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/xgb_rul_model.pkl")

feature_names = [f"op_set{i}" for i in range(1, 4)] + [f"sensor{i}" for i in range(1, 22)]

class SensorData(BaseModel):
    data: list[float]  # 24 values: 3 op_set + 21 sensor readings

@app.post("/predict")
def predict_rul(input: SensorData):
    input_df = pd.DataFrame([input.data], columns=feature_names)
    prediction = model.predict(input_df)[0]
    return {"predicted_rul": round(float(prediction), 2)}
