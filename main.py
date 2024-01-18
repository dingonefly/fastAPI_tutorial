from fastapi import FastAPI, Header
from pydantic import BaseModel, HttpUrl, Field
from typing import Annotated

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["a nice description"])
    price: float = Field(examples=[13.1])
    tax: float | None = Field(default=None, examples=[3.2])
    tags: set[str] = Field(default=set(), examples=[("a", "b")])
    images: list[Image] | None = Field(default=None, examples=[[{"url": "http://www.qq.com", "name": "baidu"}]])


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.get("/header/items/")
async def get_items(user_agent: Annotated[str | None, Header()] = None):
    return {
        "User_agent": user_agent
    }
