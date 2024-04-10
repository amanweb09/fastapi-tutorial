from fastapi import APIRouter, Body
from typing import Annotated
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from uuid import UUID

router = APIRouter()

class Product(BaseModel):
    id: UUID
    # user_email: EmailStr
    title: str
    price: float
    image: HttpUrl
    created_at: datetime

    # specifing example schema  --> model_config
    model_config = {
        "product": {
            "id": "FA12",
            "title": "T-shirt",
            "price": 499,
            "image": "https://www.google.com/images/xyz.png"
        }
    }

@router.post("/create-product", response_model=Product)    #specifies response type
def create_product(product:Product):  #we get the req.body in this function as a param
    return {"product": product}

# *********** DIFINING BODY SCHEMA *************
# appending something to the body
# if we dont use Body class, it will take it as a query param and not body of the request
@router.post("/items/{item_id}")
def handle_body(
    id:int,
    message: Annotated[str, Body()] 
):
    return f"{id} -> {message}"

# defining schema
@router.put("/message/hello")
def update_item(msg: Annotated[str, Body(embed=True)]):
    # when we pass embed=True, it will expect a key named "msg"
    # i.e {
    #   msg: {...}
    # }
    return msg


# *********** VALIDATING THE INTERFACE ******
# for this we will use Field class 
from pydantic import Field
class Product(BaseModel):
    title: str
    description: str = Field(
        max_length=500,
        default=None,
        title="Description of the product"
    )
    price: int = Field(
        title="Price of the product",
        gt=0    #greater than 0
    )

@router.post("/create-new-product")
def create_new(product: Annotated[Product, Body(embed=True)]):
    return product
