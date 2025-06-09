from fastapi import FastAPI
import uvicorn
app = FastAPI()

#Requisições GET - POST - PUT/PATCH - DELETE
@app.get("/")
def read_root():
    return {1: "Hello, World"}

@app.get("/filosofo-pedro")
def read_root():
    return {"Pro avião voar ele teve que planar"}

if __name__ == "__main__":
    uvicorn.run("PrimeiraAPI_Teste:app", host="127.0.0.1", reload=True)