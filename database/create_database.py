import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker  # Atualizando para a nova versão

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

# Definir o caminho absoluto do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Certifique-se de que o diretório 'database' exista
database_dir = os.path.join(BASE_DIR)
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

# Definir o caminho do banco de dados
DATABASE_PATH = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

# Criar o engine
engine = create_engine(DATABASE_PATH)
Session = sessionmaker(bind=engine)
session = Session()

# Função para criar o banco de dados
def init_db():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Verificar se o admin já existe
    admin_user = session.query(User).filter_by(username='admin').first()
    if not admin_user:
        # Criar usuário admin
        admin_user = User(username='admin', password='toor')
        session.add(admin_user)
        session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")


if __name__ == "__main__":
    init_db()
