# 🚀 Learning FastAPI — My First CRUD API

> This is a personal learning project. Not production-ready, not polished just me working through FastAPI from scratch and documenting what I pick up along the way.

---

## 📖 Why I Built This

I wanted to understand how modern Python APIs are built. FastAPI kept coming up as the go to framework for data engineers and backend developers, so I decided to stop reading about it and start building with it. This project is my hands-on introduction.

---

## 🛠️ What It Does

A simple REST API with full **CRUD** support:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/items` | Retrieve all items |
| `GET` | `/items/{id}` | Retrieve a single item |
| `POST` | `/items` | Create a new item |
| `PUT` | `/items/{id}` | Update an existing item |
| `DELETE` | `/items/{id}` | Delete an item |

Data is stored **in memory** (a plain Python list/dict) no database yet. The focus here is on understanding routing, request/response flow, and how FastAPI handles things automatically.

---

## 📦 Stack

- **Python 3.9+**
- **FastAPI** — the web framework
- **Uvicorn** — the ASGI server that runs the app

That's it. No database, no ORM, no Docker — intentionally bare so the fundamentals are clear.

---

## ▶️ Running the Project

**1. Clone the repo**
```bash
git clone https://github.com/Fikre-Mamo/fastapi_learning.git
cd your-repo-name
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Start the server**
```bash
uvicorn main:app --reload
```

**5. Open the interactive docs**

FastAPI generates this automatically no setup needed.
```
http://127.0.0.1:8000/docs
```

---

## 🧠 What I Learned

### FastAPI generates docs for free
The moment you define a route, FastAPI creates interactive Swagger UI at `/docs` and ReDoc at `/redoc`. This was the first thing that genuinely surprised me no extra configuration needed.

### Path parameters vs query parameters
```python
# Path parameter part of the URL
@app.get("/items/{item_id}")
def get_item(item_id: int):
    ...

# Query parameter appended after ?
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    ...
```

### Pydantic does the validation automatically
Even with bare FastAPI, you use Pydantic models to define request bodies. If a client sends the wrong type, FastAPI rejects it with a clear error no manual validation code.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
```

### HTTP status codes matter
I learned to return proper status codes instead of always defaulting to 200:
- `201 Created` when a resource is successfully created
- `404 Not Found` when an item doesn't exist
- `422 Unprocessable Entity` FastAPI raises this automatically on bad input

### `--reload` is your best friend in development
It watches for file changes and restarts the server automatically. I was restarting the server manually for longer than I'd like to admit.

---

## 🗺️ What's Next

- [ ] Connect a real database using **SQLAlchemy + PostgreSQL**
- [ ] Add **Pydantic v2** models with proper validation rules
- [ ] Learn **dependency injection** (FastAPI's `Depends()`)
- [ ] Add **JWT authentication**
- [ ] Containerise the app with **Docker**

---

## 📝 Notes to Future Me

- In-memory storage resets every time the server restarts obvious in hindsight, good to feel it firsthand
- `async def` vs `def` in route handlers matters for performance at scale — worth studying properly before the next project
- The official FastAPI docs at [fastapi.tiangolo.com](https://fastapi.tiangolo.com) are genuinely one of the best sets of documentation I've read

---

<p align="center">
  <sub>Built while learning · Mistakes included · Progress ongoing</sub>
</p>
