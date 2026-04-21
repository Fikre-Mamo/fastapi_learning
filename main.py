from fastapi import FastAPI
from h11 import Data

app = FastAPI()

@app.get('/')


def index():
    return {'Data': {'message': 'Hello World!'}}


@app.get('/about')

def about():
    return {'Data': {'message': 'This is a simple FastAPI application.'}}