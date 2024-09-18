import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from werkzeug.security import generate_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


# Definir o caminho absoluto do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

# Criar o engine e a sessão
engine = create_engine(DATABASE_PATH)
Session = sessionmaker(bind=engine)
session = Session()


# Função para criar o banco de dados
def init_db():
    Base.metadata.create_all(engine)

    # Verificar se o admin já existe
    admin_user = session.query(User).filter_by(username='admin').first()
    if not admin_user:
        # Hashear a senha antes de salvar
        hashed_password = generate_password_hash('toor')
        admin_user = User(username='admin', password=hashed_password)
        session.add(admin_user)
        session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")


if __name__ == "__main__":
    init_db()
