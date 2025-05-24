
class Animais:
    def __init__(self):
        self.__voa = True
    def __str__(self):
        return f'cavalo voa'
    @property #getter
    def voa(self):
        return self.__voa    
    @voa.setter #setter
    def config(self, voar): 
        self.__voa = voar

cavalo = Animais()
#print(cavalo.__voa) #Objeto não tem acesso ao atributo privado.
print(cavalo._Animais__voa)
cavalo.config = False
print(cavalo.voa)