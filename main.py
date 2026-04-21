from fastapi import FastAPI
from h11 import Data

app = FastAPI()

@app.get('/')


def index():
    return {'Data': {'message': 'Hello World!'}}

@app.get('/blog/{id}')

def show(id: int):
    return {'Data': id}

@app.get('/orders/{id}/items')

def items(id: int):
    return {'Data': id}