import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError

# Declarative base for models
Base = declarative_base()

# Modelo de Usuário
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    # Relacionamento com outras tabelas
    accounts = relationship('Account', backref='user', lazy=True)
    movements = relationship('Movement', backref='user', lazy=True)

# Modelo de Contas do Usuário
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_name = Column(String(100), nullable=False)
    balance = Column(Integer, nullable=False)

    # Relacionamento com o usuário
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

# Modelo de Movimentações do Usuário
class Movement(Base):
    __tablename__ = 'movements'
    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)

    # Relacionamento com o usuário
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

# Modelo de Operações
class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)

    # Relacionamento com o usuário
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='operations')

# Definir o caminho absoluto do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

# Configurar o engine e criar a sessão
engine = create_engine(DATABASE_PATH)
Session = sessionmaker(bind=engine)
session = Session()

# Criar as tabelas no banco de dados com tratamento de erro
def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("Tabelas criadas com sucesso.")
    except SQLAlchemyError as e:
        print(f"Erro ao criar as tabelas: {e}")

# Testar o banco de dados para verificar a presença de usuários
def test_database():
    try:
        # Verifique se há algum usuário existente
        user = session.query(User).first()
        if user:
            print(f"Usuário existente: {user.username}")
        else:
            print("Nenhum usuário encontrado.")
    except SQLAlchemyError as e:
        print(f"Erro ao acessar o banco de dados: {e}")

if __name__ == "__main__":
    create_tables()
    test_database()
