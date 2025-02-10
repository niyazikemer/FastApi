from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#  http://127.0.0.1:8000/

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#  http://127.0.0.1:8000/items/3