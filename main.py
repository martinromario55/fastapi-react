from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Hello World"}


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)