from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routes import router


app = FastAPI(
    title="FastAPI with React",
    description="A fast ORM for Tortoise ORM",
    version="0.1.0",
    docs_url="/",
    redoc_url="/redoc",
)



app.include_router(router)


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)