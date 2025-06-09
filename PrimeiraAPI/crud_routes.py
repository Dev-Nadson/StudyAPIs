from fastapi import APIRouter
crud_router = APIRouter(prefix="/pedidos", tags=["crud"])

@crud_router.get("/")
async def pedidos():
    return {"messagem": "Rota funcionando"}