Встановлення залежностей: `uv sync`

Створення схеми БД: `uv run alembic -c items_app/alembic.ini upgrade head`

Наповнення БД сутностями: `uv run python -m items_app.db_seed`

Запуск FastAPI сервера: `uv run uvicorn items_app:create_app --reload`        
