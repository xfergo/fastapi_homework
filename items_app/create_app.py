from fastapi import FastAPI
from items_app.routers.items import items_router
from items_app.db import engine
from items_app.models import Base

def create_app() -> FastAPI:

    Base.metadata.create_all(bind=engine)
    app = FastAPI()

    app.include_router(items_router)

    return app

