from fastapi import APIRouter
login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.get("/")
async def login():
    return {"Mensagem": "Rota funcionando.", "Status": True}