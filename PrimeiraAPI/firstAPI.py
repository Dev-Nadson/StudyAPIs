from fastapi import FastAPI
import uvicorn

app = FastAPI()

from login_routes import login_router
from crud_routes import crud_router

app.include_router(login_router)
app.include_router(crud_router)

#Requisições GET - POST - PUT/PATCH - DELETE

if __name__ == "__main__":
    uvicorn.run("firstAPI:app", host="127.0.0.1", reload=True)