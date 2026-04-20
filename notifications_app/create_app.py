from fastapi import FastAPI
from notifications_app.routers.email_notifications import notifications_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(notifications_router)

    return app

