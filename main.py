from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

#  http://127.0.0.1:8000/

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#  http://127.0.0.1:8000/items/3

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# http://127.0.0.1:8000/models/alexnet


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/items/?skip=0&limit=10


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item