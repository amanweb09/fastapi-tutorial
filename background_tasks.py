from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

"""
background tasks are used when we want to perform something after the response
is sent. eg. sending an email 
User need not wait for the task to finish to receive a response
"""

send_email_to_user = lambda email: print(f"email sent to {email}...")

@router.get("/send-email/{email}")
def send_email(email: str, background_task: BackgroundTasks):
    background_task.add_task(send_email_to_user, email)
    return {"msg": "sent"}