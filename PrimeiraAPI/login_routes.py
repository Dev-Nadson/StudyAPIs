from fastapi import APIRouter, HTTPException,Depends
from models import Usuario
from dependencies import pegar_sessao, bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import session

login_router = APIRouter(prefix="/login", tags=["login"])
@login_router.get("/")
async def home():
    return {"Mensagem": "Rota funcionando.", "Status": True}

@login_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: session = Depends(pegar_sessao)): #FastAPI funciona melhor declarando o tipo de dado da variável
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado") #retorna como erro, não com status code de 200
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(nome=usuario_schema.nome, email=usuario_schema.email, senha=senha_criptografada, ativo=usuario_schema.ativo, admin=usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuário cadastrado com sucesso {usuario_schema.email}"}