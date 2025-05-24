# Aula 01 - Introdução ao Curso
while True:
    class pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def apresentar(self):
            print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    p = pessoa(input('Digite seu nome: '), int(input('Agora por favor, digite sua idade: ')))
    p.apresentar()