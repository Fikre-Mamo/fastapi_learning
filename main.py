from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from h11 import Data
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
