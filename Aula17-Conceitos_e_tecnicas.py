#Solid
#S:
#Exemplo ruim:
class pedido:
    def __init__(self,cliente,itens):
        self.cliente = cliente
        self.itens = itens
    def calcular_total(self):
        return sum(item.preco for item in self.itens)
    def salvar_no_banco(self):
        pass
    def enviar_email(self):
        pass
#Exemplo bom:
class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
class CalcularTotal:
    def calcular_total(self, pedido):
        #calcular o total do pedido
        return sum(item.preco for item in pedido.itens)
class SalvarPedido:
    def salvar_no_banco(self, pedido):
        #salvar no banco de dados
        pass
class EnviarEmail:
    def enviar_email(self, pedido):
        #enviar email
        pass
#O:
 
#Exemplo ruim:
class Calculadora_de_descontos:
    def calcular(self,cliente):
        if cliente.tipo == 'vip':
            return 0.2
        elif cliente.tipo == 'normal':
            return 0.1
        else:
            return 0.0
        
#se surgir um novo tipo de cliente, é necessário alterar a classe.

#Exemplo bom:
class Cliente:
    def get_desconto(self):
        return 0.0
    
class ClienteVip(Cliente):
    def get_desconto(self):
        return 0.2

class ClienteRegular(Cliente):
    def get_desconto(self):
        return 0.1

#Desta forma a clase calculardesconto nao precisa saber qual o tipo de cliente, apenas calcular o desconto.

class CalcularDesconto:
    def calcular(self, cliente: Cliente):
        return cliente.get_desconto()
# L:

#Exemplo ruim:
class Ave:
    def voar(self):
        return "Estou voando"
class Pinguim(Ave):
    def voar(self):
        raise Exception("Pinguins não podem voar")
def fazer_voar(ave: Ave):
    return ave.voar()

#Neste caso, a classe Pinguim herda de Ave, mas não pode voar, o que gera uma exceção quando o método voar é chamado. Isso viola o princípio Liskov Substitution Principle (LSP), que diz que objetos de uma classe base devem poder ser substituídos por objetos de uma classe derivada sem alterar o comportamento do programa.

#Exemplo bom:

class Ave:
    def emitir_som(self):
        return "som de ave"
class Avevoadora(Ave):
    def voar(self):
        return "Estou voando"
class Andorinha(Avevoadora):
    pass

class Pinguim(Ave):
    def nadar(self):
        return "Estou nadando"

#Cada um tem uma função específica, e não há necessidade de lançar exceções, se caso o pinguim for passado como parâmetro, ele não terá o método voar, mas sim o método nadar.

# I:

#Exemplo ruim:
class Trabalhador:
    def trabalhar(self):
        pass
    def comer(self):
        pass
class Robo(Trabalhador):
    def trabalhar(self):
        return "robo trabalhando"
    def comer(self):
        raise Exception("Robo não come")

# robo não come, mas a classe pai tem o método comer, o que gera uma exceção.

#Exemplo bom:
class Trabalhador:
    def trabalhar(self):
        pass
class comer:
    def comer(self):
        pass
class Humano(Trabalhador, comer):
    def traalhar(self):
        return "Humano trabalhando"
    def comer(self):
        return "Humano comendo"
class Robo(Trabalhador):
    def trabalhar(self):
        return "Robo trabalhando"

#Robo não tem o método comer, mas a classe pai tem Só tem o método trabalhar, o que não gera exceção.

# D:

#Exemplo ruim:
class MySQLRepository:
    def salvar(self, dados):
        print('Salvando dados MySQL...')

class usuario_Service:
    def __init__(self):
        self.repositorio = MySQLRepository()
    def cadastrar_usuario(self,usuario):
        self.repositorio.salvar(usuario)

#Neste caso, o usuario_Service está acoplado diretamente ao MySQLRepository, o que dificulta a manutenção e testes, pois não é possível trocar a implementação do repositório sem alterar o serviço.

#Exemplo bom:

#implementação do repositório abstrata
class Repositorio_usuario:
    def salvar(self,dados):
        raise NotImplementedError("Método salvar não implementado")

#implementação concreta do repositório
class MySQLRepository(Repositorio_usuario):
    def salvar(self, dados):
        print('Salvando dados MySQL...')

class usuario_Service:
    def __init__(self,repositorio: Repositorio_usuario):
        self.repositorio = repositorio #injetado a dependência
    def cadastrar_usuario(self, usuario):
        self.repositorio.salvar(usuario)

#Ja neste caso, o usuario_Service não está acoplado diretamente ao MySQLRepository, mas sim a uma abstração (Repositorio_usuario). Isso permite que diferentes implementações de repositórios sejam injetadas no serviço, facilitando a manutenção e testes.

#Lambda:

# Uma função anônima que pode ser usada para criar funções pequenas e simples de forma rápida.

#exemplo de uso:


numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x *2, numeros))
print(dobrados)

#Filtrar
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

produtos = [('banana', 2), ('maçã', 3), ('laranja', 1)]
produtos_ordenados = sorted(produtos, key=lambda x: x[1])
print(produtos_ordenados)

#list comprehension
numeros = [1, 2, 3, 4, 5]
dobrados = [x * 2 for x in numeros]
print(dobrados)
pares = [x for x in numeros if x % 2 == 0]
print(pares)
nomes = ['Ana', 'João', 'Maria']
saudações = [f'Olá, {nome}!' for nome in nomes]
print(saudações)

# List comprehension é uma forma concisa de criar listas em Python, permitindo aplicar operações e filtros diretamente na criação da lista.

matriz = [[i*j for j in range(3)] for i in range(3)]
print(matriz)
#matriz

#set comprehension
numeros = [1, 2, 3, 4, 5]
quadrados = {x**2 for x in numeros}
print(quadrados)

pares = {x for x in range (10) if x % 2 == 0}
print(pares)

#dict comprehension
nomes = ['Ana', 'João', 'Maria']
comprimentos  = {nome: len(nome) for nome in nomes}
print(comprimentos)

pares_quadrados= {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_quadrados)

chaves = ['a', 'b', 'c']
valores = [1, 2, 3]
dicionario = {k: v for k, v in zip(chaves, valores  )}
print(dicionario)
#dict comprehension é uma forma concisa de criar dicionários em Python, permitindo aplicar operações e filtros diretamente na criação do dicionário.


#Tratamento de exceções

try: 
    a = int('abc')
    b = 10/0
except ValueError as e:
    print(f"Erro de valor: {e}")

class idadeInvalida(Exception):
    pass
def verificar_idade(idade):
    if idade < 0 :
        raise idadeInvalida("Idade não pode ser negativa")
try:
    verificar_idade(-5)
except idadeInvalida as e:
    print(f"Erro de idade: {e}")
try:
    x = int('abc')


#Captura todos os erros e exibe uma mensagem genérica
except Exception as e:
    print(f'ocorreu um erro: {e}')
finally:
    raise idadeInvalida("Voce ainda é menor de idade")