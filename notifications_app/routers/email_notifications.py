from fastapi import BackgroundTasks, APIRouter

notifications_router = APIRouter()


def write_notifications(email: str, message="") -> None:
    with open("../log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@notifications_router.post("/send-notification/{email}")
async def send_notification(email:str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notifications, email, message="some notification")
    return {"message": "Notification sent in the background"}

