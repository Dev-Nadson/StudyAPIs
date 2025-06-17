from fastapi import APIRouter, HTTPException,Depends
from models import Usuario
from dependencies import pegar_sessao, bcrypt_context
from schemas import UsuarioSchema, AutenticacaoSchema
from sqlalchemy.orm import Session

login_router = APIRouter(prefix="/login", tags=["login"])

def criar_token(id_usuario):
    token = f"12345{id_usuario}"
    return token

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

@login_router.get("/")
async def home():
    return {"Mensagem": "Rota funcionando.", "Status": True}

@login_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)): #FastAPI funciona melhor declarando o tipo de dado da variável
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado") #retorna como erro, não com status code de 200
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(nome=usuario_schema.nome, email=usuario_schema.email, senha=senha_criptografada, ativo=usuario_schema.ativo, admin=usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuário cadastrado com sucesso {usuario_schema.email}"}

#Iniciando a autenticação do login vis Json Web Token
@login_router.post("/autenticacao")
async def autenticacao(autenticacao_schema: AutenticacaoSchema, session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(email=autenticacao_schema.email, senha=autenticacao_schema.senha, session=session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")
    else:
        access_token = criar_token(usuario.id)
        return {"access_token": access_token, "token_type": "Bearer"}