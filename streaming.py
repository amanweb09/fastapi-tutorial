from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()

def stream_video():
    for i in range(10):
        yield b"these are video bytes"

@router.get("/play-video")
def play():
    return StreamingResponse(stream_video())