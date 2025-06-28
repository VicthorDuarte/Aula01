class Livro:
    
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f'{self.titulo}, {self.autor}'
    
livro = Livro('O Hobbit', 'J.R.R. Tolkien') #Definindo o nome do livro
print(livro)