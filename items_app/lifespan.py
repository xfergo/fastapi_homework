from contextlib import asynccontextmanager
from typing import TYPE_CHECKING
from venv import logger
from fastapi import FastAPI
from collections.abc import AsyncGenerator

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI


# noinspection PyUnusedLocal
@asynccontextmanager
async def lifespan(
    app: FastAPI,  # pyright: ignore[reportUnusedParameter]  # noqa: ARG001
) -> AsyncGenerator[None]:
    """Lifespan context manager.

    This function is used to set up and tear down resources for the FastAPI application.
    """
    # Set up resources here
    logger.info("Starting app")

    try:
        yield
    finally:
        # Tear down resources here
        logger.info("Stopping app")