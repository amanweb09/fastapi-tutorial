from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/admin")
def handle_admin():
    is_admin = False

    if not is_admin:
        raise HTTPException(status_code=401, detail="unauthorized")
    else:
        return "admin panel..."