from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    usuario: int
    class Config:
        from_attributes = True

class AutenticacaoSchema(BaseModel):
    email: str
    senha: str
    class Config:
        from_attributes = True