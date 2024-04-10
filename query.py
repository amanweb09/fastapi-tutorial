from fastapi import APIRouter
from typing import Annotated
from fastapi import Query

router = APIRouter()


# *********** PATH PARAMS *************
@router.get("/product/{id}")
def get_product_id(id:str):     # we get this id in the function as a param
    return {"id": f"The product ID is {id}"}

# if path params itself contain a path like /home/text.pdf
@router.get("/file/{file_path:path}")  #specify by :path
def show_file(file_path: str):
    return f"The path is {file_path}"



# ******** QUERY PARAMS (?) *********
ids = [i for i in range(100)]
@router.get("/products")   #the req will be on /products?limit=10
def show_products(limit: int):
    return ids[:limit]

# optional params
@router.get("/products")   #Here start is an optional param
def show_products(start: int | None ,limit: int):
    if start:
        return ids[:limit]
    else:
        return ids[start:limit]


# ******* ADDING METADATA TO PARAMS ******
# for this we use annotated as it helps to combine assign multiple datatypes to  a variable or param
# Query will help use specify various rules for the params like length, size, etc

@router.get("/items")
def handle_items(
    # this meta data says id can be a str or None and max_length of 50 chars
    id: Annotated[str , Query(max_length=5, min_length=3)]   
):
    return id
