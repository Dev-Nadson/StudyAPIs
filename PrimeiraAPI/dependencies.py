from models import database
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #garantir que a criptografia não seja obsoleta

def pegar_sessao():
    try:
        SessionLocal = sessionmaker(bind=database)
        session = SessionLocal()
        yield session #retorna o valor sem encerrar a função
    finally: #Garantir que a rota seja fechada
        session.close()