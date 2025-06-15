from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao, bcrypt_context

login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.get("/")
async def home():
    return {"Mensagem": "Rota funcionando.", "Status": True}

@login_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)): #FastAPI funciona melhor declarando o tipo de dado da variável
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem": "Já existe um usuário com esse email."}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuário cadastrado com sucesso."}