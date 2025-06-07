class ColecaoNomes:
    def __init__(self):
        self._nomes = []
    def adicionar(self, nome):
        self._nomes.append(nome)
    def __iter__(self):
        return IteratorNomes(self._nomes)
class IteratorNomes:
    def __init__(self, nomes):
        self._nomes = nomes
        self._posicao = 0
    def __next__(self):
        if self._posicao >= len(self._nomes):
            raise StopIteration
        nome = self._nomes[self._posicao]
        self._posicao += 1
        return nome
    def __iter__ (self):
        return self
colecao = ColecaoNomes()
colecao.adicionar("Alice")
colecao.adicionar("Bruno")
colecao.adicionar('Carla')

for nome in colecao:
    print(nome)

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