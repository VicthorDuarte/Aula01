<<<<<<< HEAD
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    def ligar(self):
        print(f'Motor ligado com potência a potecia de {self.potencia}')
        pass
class carro:
    def __init__(self,modelo,motor):
        self.modelo = modelo
        self.motor = motor #aqui acontece a composição
    def ligar(self):
        print(f'ligando carrro moodelo {self.modelo}')
        self.motor.ligar() #Usando o metodo objeto motor

Motorv8 = Motor(500)
carro_esportivo = carro('Mustang',Motorv8)
carro_esportivo.ligar()
=======
from abc import ABC, abstractmethod
import time
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self,valor):
        pass

class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        print(f'processando pagamento no valor de R${valor:2f} via Cartão de Crédito.')
        
class Paypal(Pagamento):
    def processar_pagamento(self, valor):
        print(f'processando pagamento no valor de R${valor:2f} via PayPal.')

class pix(Pagamento):
    def processar_pagamento(self, valor):
        print(f'processando pagamento no valor de R${valor:2f} via Pix.')
def finalizar_compra(metodo_pagamento: Pagamento, valor: float):
    metodo_pagamento.processar_pagamento(valor)
if __name__ == '__main__':
        pagamentos = [CartaoCredito(),
                      Paypal(),
                      pix()
                      ]
for metodo in pagamentos:
    time.sleep(1)
    finalizar_compra(metodo, 99.99)
>>>>>>> 2edeabfc2ac0f2a117820b0a1e5731ee33484865
