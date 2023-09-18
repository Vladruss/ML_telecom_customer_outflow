from pydantic import BaseModel, Field
from typing import List, Literal


class ChurnPrediction(BaseModel):
    id:str
    day:int = Field(gt=0)
    MonthlyCharges:float
    Type:Literal['Month-to-month', 'One year', 'Two year']


class ChurnPredictionRequest(BaseModel):
    churncustomers: List[ChurnPrediction] 


class ChurnPredicted(BaseModel):
    id:str
    target: int


class ChurnPredictionResult(BaseModel):
    result: List[ChurnPredicted] = Field(default_factory=list)