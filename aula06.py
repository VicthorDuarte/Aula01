class LogMixin:
    def log(self, message):
        print(f'[LOG]: {message}')
class Database:
    def connect(self):
        print('Conectando ao banco de dados...')
class LoggedDatabase(Database, LogMixin):
    def connect(self):
        self.log('Tentando conectar ao banco de dados...')
        super().connect()
# uso: 
db = LoggedDatabase()
db.connect()
from dataclasses import dataclass
from dataclasses import field
@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class produto:
    nome : str
    preço: float
@dataclass
class Pedido:
    cliente: Pessoa
    produtos: list[produto] = field(default_factory=list)
@dataclass (frozen = True)
class coordenada:
    lat: float
    lon: float


#Customização da str com dunder methods

class pessoa:
    def __init__ (self,nome):
        self.nome = nome
    def __str__(self):
        return f'Pessoa: {self.nome}'
    def __repr__(self):
        return f'pessoa(nome={self.nome!r})'
class produto:
    def __init__(self, preco):
        self.preco = preco
    def __eq__(self, other):
        return self.preco == other.preco
class Minhalista:
    def __init_ (self, itens):
        self.itens = itens
    def __len__(self):
        return len(self.itens)
    def __getitem__(self, index):
        return self.itens[index]
