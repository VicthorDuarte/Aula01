import random
def gerar_primos(limite):
    for num in range(2, limite +1):
        if eh_primo(num):
            yield num
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1 ):
        if n % i == 0:
            return False
    return True

def gerador_infinito():
    n = 1
    while True:
        if eh_primo(n):
            yield n
        n += 1
        
print('Numeros primos até 30')
gen = gerar_primos(30)
gen2 = gerador_infinito()

for primo in gen2:
    logic = print(f'{primo}{random.choice(['a', 'b', 'c', 'd'])}', end = ' ')
    if logic == '145897a':
        break
    elif logic == '145897b':
        break
    elif primo == '145897c':
        break
    else:

        break
    