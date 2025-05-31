from functools import wraps
import time
class configuracao:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print('Criando nova instancia de configuracao')
        return cls._instancia
    def __init__(self):
        self.ambiente = 'producao'
        self.debug = False
config1 = configuracao()
config2 = configuracao()
print(config1 is config2)  # True, ambas variáveis referenciam a mesma instância
print(config1.ambiente)  # producao
config1.debug = True
print(config2.debug)  # True, pois config1 e config2 são a mesma instância

#Design pattern Decorator
def logar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] Chamando {func.__name__} com args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper
def tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f'[TEMPO] {func.__name__} levou {fim - inicio:.4f} segundos')
        return resultado
    return wrapper
@logar
@tempo
def processar_dados(x):
    time.sleep(1)
    return x*2
resultado = processar_dados(5)
print(f'Resultado: {resultado}')