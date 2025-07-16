from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello from FastAPI Dev Container!"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
