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

# Classes aninhadas

class Externa:
    class Interna:
        def mostrar(self):
            print('Classe interna acessada')
            
obj = Externa.Interna()
obj.mostrar()
# Acessando a classe interna


class pessoa:
    especie = 'humano'
    def __init__(self,nome):
       self.nome = nome
    @staticmethod
    def e_maior_idade(idade):
         return idade >= 18
print(pessoa.e_maior_idade(20))
print(pessoa.e_maior_idade(15))
p1 = pessoa('Ana')
print(p1.nome)
print(p1.especie)

#Mudando  o atributo da classe
pessoa.especie  = 'alienigena'
print(p1.especie) #alienigena