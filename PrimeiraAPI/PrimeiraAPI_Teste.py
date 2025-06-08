from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {1: "Hello, World"}

@app.get("/filosofo-pedro")
def read_root():
    return {"Pro avião voar ele teve que planar"}