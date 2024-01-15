#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2023/9/6
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel


app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get('/')
async def read_root():
    return {"Hello": "World"}


@app.get('/items/{item_id}')
async def read_user_item(item_id: int, needy: str, skip: int = 0, limit: Union[int, None] = None):
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit,
    }
    return item



@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    print(type(model_name))
    print(model_name)
    print(model_name.value)
    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name,
            "message": "Deep Learning FTW!"
        }
    if model_name.value == "resnet":
        return {
            "model_name": model_name,
            "message": "LeCNN all the images"
        }

    return {"model_name": model_name, "message": "Have some residuals"}



@app.post("/items/")
async def create_item(item: Item):
    return item