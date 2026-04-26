from fastapi import FastAPI
from items_app.routers.items import items_router
from items_app.lifespan import lifespan

def create_app() -> FastAPI:

    app = FastAPI(
        lifespan=lifespan,
    )

    app.include_router(items_router)

    return app

