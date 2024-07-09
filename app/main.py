from model import Predict
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Input(BaseModel):
    question: str
    context: str


@app.get("/")
def read_root():
    return {"Message": "Hello World"}


#  I need to get message from the user!
@app.post("/predict")
def get_prediction(input: Input):
    output, time = Predict(input.question, input.context)
    return output, time
