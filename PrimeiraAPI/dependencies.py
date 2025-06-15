from models import database
from sqlalchemy.orm import sessionmaker, declarative_base

def pegar_sessao():
    try:
        SessionLocal = sessionmaker(bind=database)
        session = SessionLocal()
        yield session #retorna o valor sem encerrar a função
    finally: #Garantir que a rota seja fechada
        session.close()