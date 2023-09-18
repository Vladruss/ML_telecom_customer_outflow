from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from src.schemas import  ChurnPredictionRequest, ChurnPrediction, ChurnPredictionResult, ChurnPredicted


app = FastAPI(
    title="Customer_churn"
)

def get_model():
    """ Function to get model """
    with open('model_store/cat_model.pkl', 'rb') as model_path:
        model = pickle.load(model_path)
    return model['model']

model = get_model()


@app.post('/predict', response_model=ChurnPredictionResult)
async def predict(request: ChurnPredictionRequest):
    data = [churn.dict() for churn in request.churncustomers]
    df = pd.DataFrame(data).set_index('id')
    propabilities = model.predict_proba(df)[:,1]
    tre = 0.29
    pred_valid = propabilities > tre
    result = []
    for i, pred in zip(df.index, pred_valid):
        result.append({
            'id': str(i)
            ,'target': int(pred)})

    return ChurnPredictionResult(result=result)
