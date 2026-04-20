from items_app.models import Item
from items_app.db import get_db
from items_app.schemas import ItemCreate, ItemResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, Query
items_router = APIRouter()



@items_router.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(data: ItemCreate, db: Session = Depends(get_db)):
    item = Item(name=data.name, price=data.price, in_stock=data.in_stock)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@items_router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
   item = db.get(Item, item_id)
   if not item:
       raise HTTPException(status_code=404, detail="Product not found")
   return item

@items_router.get("/items", response_model=list[ItemResponse])
def get_items_list(
        db: Session = Depends(get_db),
        skip: int = Query(0, ge=0),
        limit: int | None = Query(None, le=20),

):
    return db.query(Item).limit(limit).all()


