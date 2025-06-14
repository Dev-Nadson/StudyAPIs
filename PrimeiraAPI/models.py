from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database", "banco.db")
database = create_engine(f"sqlite:///{db_path}")
base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=True)
    email = Column("email", String, nullable=True)
    senha = Column("senha", String, nullable=True)
    ativo = Column("ativo", Boolean, nullable=True)
    admin = Column("admin", Integer, nullable=True, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class pedido(base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (("PENDENTE", "PENDENTE"),("CANCELADO", "CANCELADO"),("FINALIZADO", "FINALIZADO"))

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario = Column("usuario", ForeignKey("usuarios.id"), nullable=True)
    status = Column("status", String, nullable=True)
    preco = Column("preco", Float, nullable=True)
    #itens =

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

class itensPedido(base):
    __tablename__ = "itensPedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=True)
    sabor = Column("sabor", String, nullable=True)
    tamanho = Column("tamanho", String, nullable=True)
    preco_unitario = Column("preco_unitario", Float, nullable=True)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

base.metadata.create_all(bind=database)