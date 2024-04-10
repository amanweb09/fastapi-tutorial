from fastapi import FastAPI

"""
mounting is used for creating independent APIs and mounting them to the main api
"""

app = FastAPI()

sub_api = FastAPI()

@app.get("/pqr")
def handle_api():
    return "Thanks"

@sub_api.get("/abc")
def handler():
    return "hello"

app.mount(sub_api)