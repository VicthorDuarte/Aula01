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