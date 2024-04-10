from fastapi import Cookie ,APIRouter, Response
from typing import Annotated

router = APIRouter()

# receiving cookies from the client
@router.get("/account")
def show_account(ad: Annotated[str, Cookie()]):
    return ad

# sending cookies to the client
@router.get("/send-cookie")
def send_cookie(res:Response):
    res.set_cookie(key="refresh-token", value="mytoken123")
    return {"msg": "success"}
