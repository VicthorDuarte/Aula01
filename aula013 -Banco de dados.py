#Banco de dados SQLite
import sqlite3
conn  = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
#CRUD
#C - CREATE
#R - LEITURA
#U - UPDATE
#D
#CREATE - criação da tabela 
cursor.execute('''
               CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL)
               ''')
conn.commit()
 # INSERT - Inserindo dados na tabela
def criar_usuario(nome,idade):
    cursor.execute(f"INSERT INTO usuarios (nome, idade) VALUES ('{nome}',{idade})")
    conn.commit()

# SELECT Lendo os dados
def lendo_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        print(row)

# UPDATE Atualizando os dados 
def atualizar_usuario(id, novo_nome, novo_idade):
    cursor.execute('UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?', (novo_nome, novo_idade, id))
    conn.commit()

#DELETE Deletando informações do Banco de dados
def deletar_usuario(id):
    cursor.execute(f'DELETE FROM usuarios WHERE id = {id}')
    conn.commit()

print('Criando Usuários')
criar_usuario('Pedro', 21)
criar_usuario('Bob', 17)
criar_usuario('Carol', 22)
print('listando usuários')
lendo_usuarios()
print('Atualizando usuario de ID 2')
atualizar_usuario(2, 'Ricardo', 30)
lendo_usuarios()
print('Deletando usuário de ID 1')
deletar_usuario(1)
lendo_usuarios()

#Fechando a conexão...
conn.close()
