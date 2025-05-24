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