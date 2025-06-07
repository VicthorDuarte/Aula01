from enum import Enum
class Pato:
    def quack(self):
        print('Quack!')

class Cachorro:
    def latir(self):
        print('AU AU AU!')

class Pessoa:
    def quack(self):
        print('estou imitando um pato, Quack!')

class status(Enum):
    Pessoa = Pessoa()
    Pato = Pato()
    Cachorro = Cachorro().latir()