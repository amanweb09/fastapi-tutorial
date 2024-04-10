from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws")
async def handle_ws(ws: WebSocket):
    await ws.accept()
    
    while True:
        data = ws.receive_text()
        print(data)
        await ws.send_text("Hello")