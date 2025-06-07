<<<<<<< HEAD
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
=======
    #Observadores

class Estacaoclimatica:
    def __init__(self):
        self._observadores = []
        self._temperatura = None
    def adicionar_observador(self,observador):
        self._observadores.append(observador)
    
    def remover_observador(self,observador):
        self._observadores.remove(observador)
    def notificar_observador(self):
        for obs in self._observadores:
            obs.atualizar(self._temperatura)
    
    def definir_temperatura(self, nova_temp):
        print(f'\n[Estação] Temperatura alterada para {nova_temp}°C')
        self._temperatura = nova_temp
        self.notificar_observador()
#Observador sendo criado
class TelaCelular:
    def atualizar(self, temperatura):
        print(f'[CELULAR] Nova Temperatura: {temperatura} °C')
class TelaPainel:
    def atualizar(self, temperatura):
        print(f'[Painel Digital] Temperatura atualizada para: {temperatura} °C')
estacao = Estacaoclimatica()
celular = TelaCelular()
painel = TelaPainel()

estacao.adicionar_observador(celular)
estacao.adicionar_observador(painel)

estacao.definir_temperatura(25)
estacao.definir_temperatura(30)
>>>>>>> 2edeabfc2ac0f2a117820b0a1e5731ee33484865
