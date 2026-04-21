from fastapi import FastAPI
from h11 import Data
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# @app.get('/blog')


# def index(limit: int=10, published: bool=True):
#     if published:
#         return {'Data': f'{limit} published blogs'}
#     else:
#         return {'Data': f'{limit} blogs'}

@app.get('/blog/{id}')

def show(id: int):
    return {'Data': id}

@app.get('/orders/{id}/items')

def items(id: int):
    return {'Data': id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'Data': f"Blog is created with title '{blog.title}' and body '{blog.body}'"}
