from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from schemas import PedidoSchema
from sqlalchemy.orm import session
from models import pedido

crud_router = APIRouter(prefix="/pedidos", tags=["crud"])

@crud_router.get("/")
async def pedidos():
    return {"messagem": "Rota funcionando"}

@crud_router.post("/pedido")
async def criar_pedido(pedido_schema:PedidoSchema, session: session = Depends(pegar_sessao)):
    novo_pedido = pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido Criado com sucesso! ID: {novo_pedido.id}"}