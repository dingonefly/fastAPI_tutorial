from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, Field

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
