from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Usuario, database
login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.get("/")
async def home():
    return {"Mensagem": "Rota funcionando.", "Status": True}

@login_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str): #FastAPI funciona melhor declarando o tipo de dado da variável
    SessionLocal = sessionmaker(bind=database)
    session = SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem": "Já existe um usuário com esse email."}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuário cadastrado com sucesso."}