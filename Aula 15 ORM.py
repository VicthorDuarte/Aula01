from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
#Configuração do banco de dados
Base = declarative_base()
Engine = create_engine('sqlite:///Aula15orm.db', echo=True)
Session = sessionmaker(bind=Engine)
session = Session()

#Modelo(tabela)
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)
    def __repr__(self):
        return f'Usuarios: (id={self.id}, nome={self.nome}, idade={self.idade})'

#Criação da tabela
Base.metadata.create_all(Engine)

#Inserindo dados na tabela
novo_usuario = Usuario(nome= 'João', idade = 15)
session.add(novo_usuario)
novo_usuario = Usuario(nome= 'Alice', idade = 29)
session.add(novo_usuario)
session.commit()

#Lendo dados da tabela
usuarios = session.query(Usuario).all()
for u in usuarios:
    print(u)

#Atualizando dados na tabela
usuario = session.query(Usuario).filter_by(nome='João').first()
usuario.idade = 20
usuario.nome = 'João Silva'
session.commit()
for u in usuarios:
    print(u)


#Deletando dados da tabela
session.delete(usuario)
session.commit()