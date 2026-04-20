from pydantic import BaseModel, Field
from typing import Annotated


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

class ItemResponse(BaseModel):
    id: int
    name: Annotated[str, Field(exclude=True, examples=["dsafasdf"])]
    price: Annotated[float, Field(examples=[12,2])]
    in_stock: Annotated[bool, Field(examples=["true"])]
    model_config = {"from_attributes": True}