from fastapi import FastAPI
import uvicorn
app = FastAPI()
from login_routes import *
from crud_routes import *

#Requisições GET - POST - PUT/PATCH - DELETE

if __name__ == "__main__":
    uvicorn.run("PrimeiraAPI_Teste:app", host="127.0.0.1", reload=True)