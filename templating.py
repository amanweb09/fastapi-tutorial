# we will use jinja2 for templating
# pip install jinja2

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request

router = APIRouter()

templates = Jinja2Templates("templates")

@router.get("/home")
def render_home(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html", 
        context={"msg": "Hello from jinja2"})