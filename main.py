from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging

# Настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка модели
model = joblib.load('text_classifier.joblib')
logger.info("Model loaded successfully")

# FastAPI-приложение
app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.post("/predict")
async def predict(input_data: TextInput):
    logger.info(f"Predicting for: {input_data.text}")
    prediction = model.predict([input_data.text])[0]
    return {"prediction": int(prediction)}
