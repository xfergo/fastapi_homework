import asyncio
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from items_app.models import Item
from items_app.db import AsyncSessionLocal

async def seed_db():
    async with AsyncSessionLocal() as session:

        result = await session.execute(select(func.count()).select_from(Item))
        count = result.scalar()

        if count == 0:
            print("Seeding database...")
            items = [
                Item(
                    name=f"Item {i}",
                    price=10.0 + i,
                    in_stock=True
                ) for i in range(100)
            ]
            session.add_all(items)
            await session.commit()
            print("Database seeded successfully")
        else:
            print(f"Database already has {count} items. Skipping.")

if __name__ == "__main__":
    asyncio.run(seed_db())