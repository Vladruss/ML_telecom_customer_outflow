# Telecom customer outflow
This project is an example of using machine learning to predict customer churn.
The best trained model was integrated in Api using FastAPI. The web application was packaged in a Docker container.

## Requirements:
* Python 3.10+

## Training and tuning models
Data preprocessing, training and tuning model in jupyter [telecom_customer_outflow.ipynb](https://github.com/Vladruss/ML_Determining_the_cost_of_cars/blob/main/Determining_the_cost_of_cars.ipynb)

## Running the model locally in fastapi
1. Activate the environment and install dependencies
```
source /path/to/venv/bin/activate
pip install -r requirements.txt
```
or
```
python3 -m pip install poetry==1.6.1
poetry install
```

2. Launch the service
```
uvicorn main:app --reload
```

## Deployment with Docker
1. Build the Docker image
```
docker build -t ml_api .
```
3. Running the Docker image
```
docker run -d -p 8000:8000 ml_api
```


