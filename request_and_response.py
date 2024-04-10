from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse ,Response

router = APIRouter()

@router.post("/basic")
def basics(req: Request, res:Response):
    print(req.cookies)
    return req.body

# types of responses - JSON response, redirect response, html response
@router.get("/dashboard")
def handle_dashboard():
    is_login:bool = False

    if not is_login:
        return RedirectResponse(url="/login")
    else:
        return JSONResponse("Access granted!")

@router.get("/cart")
def show_cart():
    return HTMLResponse(""" <h1> Welcome to Cart </h1> """)

# Response status code
@router.get("/tasks")
def check_tasks(task:str):
    tasks = ["office", "gym"]
    if task not in tasks:
        return JSONResponse("Not found", status_code=404)
    return JSONResponse("found")

# method 2 for setting status code
@router.get("/tasks/1")
def check_tasks_1(task:str, res:Response):
    tasks = ["office", "gym"]
    if task not in tasks:
        res.status_code = 404
        return {"msg": "not found", "status": res.status_code}
    return "found"

# setting headers
@router.get("/set-headers")
def set_headers(res: Response, req:Request):
    res.headers["X-my-header"] = "My header"
    return {
        "headers": req.headers
    }