from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import request_and_response
import query as query_routes
import validation
import cookie_handling
import forms
import error_handling
import auth
import background_tasks
import templating
import web_sockets

# do something before the app starts
@asynccontextmanager
async def lifespan():
    print("starting app..")
    # we need to perform cleanup as well

app = FastAPI(
    # adding metadata to our API
    title="Tutorial API",
    description="This is an API written in Python using FastAPI",
    version="1",
    terms_of_service="No terms",

    lifespan=lifespan
)

# cors middleware
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# serving static files
app.mount("/static", StaticFiles(directory="static"))

# code splitting
app.include_router(request_and_response.router)
app.include_router(auth.router) 
app.include_router(query_routes.router)
app.include_router(validation.router)
app.include_router(cookie_handling.router)
app.include_router(forms.router)
app.include_router(error_handling.router)
app.include_router(background_tasks.router)
app.include_router(templating.router)
app.include_router(web_sockets.router)

@app.get("/")
def root():
    return {"message": "Welcome to Home"}