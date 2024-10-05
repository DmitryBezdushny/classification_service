from fastapi import FastAPI
from fastapi.params import Body

from src.model import Model

app = FastAPI()
model = Model()


@app.get("/")
def index():
    return {"message": "App is working"}
 
@app.post("/predict")
def predict(features: dict = Body(...)):
    return model.predict(features)

