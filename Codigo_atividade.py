from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlite3
connect = sqlite3.connect('Armazenamento.db')
cursor = connect.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos( id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT NOT NULL,
quantidade INT NOT NULL,
valor int NOT NULL)''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS Vendas( id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT NOT NULL,
Produto TEXT NOT NULL,
quantidade INT NOT NULL,
valor int NOT NULL)''')
connect.commit()
class identificador_de_arquivotxt:
    pass

class Venda:
    def Venda(self, usuario, produto, quantidade, valor):
        self.usuario = usuario
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        pass
class Vendarepositório(Venda, identificador_de_arquivotxt):
    def inserir_vendas(self, usuario, produto, quantidade, valor):
        cursor.execute('''INSERT INTO Vendas ('usuario', 'Produto', quantidade, valor) VALUES (?, ?, ?, ?)''',
                       (usuario, produto, quantidade, valor))
        connect.commit()
        print("Venda inserida com sucesso!")
    def ler_arquivos(self):
         Consulta = cursor.execute('''SELECT * FROM Vendas''')
         for linha in Consulta:
             print(linha)
         pass


Vendas = Vendarepositório()
Vendas.inserir_vendas('Cleber Contel', 'Playstation 5', 1, 5000)
Vendas.inserir_vendas('Matheus Lopes', 'Tablet', 1, 1200)
Vendas.inserir_vendas('Jhonathan Melo', 'Iphone 11', 1, 2000)
Vendas.inserir_vendas('João Lucas', 'Fritadeira', 1, 300)
Vendas.ler_arquivos()
connect.close()









#Com ORM
Base = declarative_base()

engine = create_engine("sqlite:///Armazenamento.db", echo=True)

Session = sessionmaker(bind=engine)

session = Session()

class Tabela_de_vendas(Base):
    __tablename__ = 'Vendas'
    id = Column(Integer, primary_key=True)
    usuario = Column(String)
    produto = Column(String)
    quantidade = Column(Integer)
    valor = Column(Integer)

Base.metadata.create_all(engine)

class vendasrepositorio:
    def venda_info(self, usuario, produto, quantidade, valor):
        nova_venda = Tabela_de_vendas(usuario=usuario, produto=produto, quantidade=quantidade, valor=valor)
        session.add(nova_venda)
        session.commit()

    def consultar_vendas(self):
        usuarios = session.query(Tabela_de_vendas).all()
        for u in usuarios:
            print(u)
Vendarepositorio = vendasrepositorio()
Vendarepositorio.venda_info('Jorge', 'Lava Louças', 1, 145)
Vendarepositorio.venda_info('Jonathan Pinheiro', 'Chave Philips', 1, 60)
Vendarepositorio.venda_info('Pedro Nogueira', 'Carregador Usb', 1, 20)
Vendarepositorio.consultar_vendas()