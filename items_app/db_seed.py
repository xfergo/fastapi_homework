from sqlalchemy.orm import Session
from items_app.models import Item, Base
from items_app.db import engine

Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    if session.query(Item).count() == 0:
        print("Seeding database...")
        items = [
            Item(
                name=f"Item {i}",
                price=10.0 + i,
                in_stock=True
            ) for i in range(100)
        ]
        session.add_all(items)
        session.commit()
        print("Database seeded successfully")
    else:
        print("Database already has data. Skipping.")