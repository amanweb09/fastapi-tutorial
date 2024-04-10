"""
Forms are used for receiving <form></form> data like name, username, password, etc

For this we need to install python-multipart
"""

from fastapi import APIRouter, Form, File, UploadFile
from typing import Annotated

router = APIRouter()

@router.post('/signup')
def handle_signup(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return "Signup successful!"


# Uploading files
@router.post('/create-avatar')
def create_avatar(
    file: Annotated[bytes, File(description="This is my avatar")]
):
    return f"The size of the file is {len(file)}"


# method 2
@router.post('/create-avatar')
def create_avatar(
    file: UploadFile        # the file received in the request
):
    pass

# multiple files
@router.post('/send-images')
def create_avatar(
    file: list[UploadFile]
):
    return f"The size of the file is {len(file)}"