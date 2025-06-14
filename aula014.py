import sqlite3
conn = sqlite3.connect('Bancodedados.db')
conn.execute("PRAGMA foreign_keys=ON")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS cliente (cpf INTEGER PRIMARY KEY, 
               nome TEXT NOT NULL,
               datansc TEXT NOT NULL,
               sexo TEXT NOT NULL,
               telefone INTEGER NOT NULL)
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS vendas (codigo_vnd INTEGER PRIMARY KEY AUTOINCREMENT, 
               produto TEXT NOT NULL,
               cod_produto INTEGER NOT NULL,
               cpf_cliente INTEGER NOT NULL,
               x INTEGER NOT NULL,
               FOREIGN KEY (cod_produto) REFERENCES produto(cod_produto)
               FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf)
               )
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS produto (cod_produto INTEGER PRIMARY KEY AUTOINCREMENT,
               produto TEXT NOT NULL,
               quantidade INTEGER NOT NULL,
               descrição  TEXT NOT NULL
               )
               ''')

def criar_usuario(nome, cpf, datansc, sexo, telefone):
    cursor.execute(f"INSERT INTO cliente (nome, cpf, datansc, sexo, telefone) VALUES ('{nome}', {cpf}, '{datansc}', '{sexo}', {telefone})")
    conn.commit()

def vendas(produto, cod_produto, cpf_cliente, x):
    cursor.execute(f"INSERT INTO vendas (produto, cod_produto, cpf_cliente, x) VALUES ('{produto}', {cod_produto},{cpf_cliente}, {x})")
    conn.commit()
    cursor.execute(f"SELECT quantidade FROM produto WHERE cod_produto = {cod_produto} ")
    quantidade = cursor.fetchall()[0][0]
    if x <= quantidade:
        print('Venda feita com sucesso')
        a_estoque = quantidade-x
        cursor.execute(f"UPDATE produto SET quantidade = {a_estoque} WHERE cod_produto = {cod_produto}")
        conn.commit()
    else:
        print('Venda não foi concluida')
    conn.commit()
def criar_produto(produto,quantidade,descrição):
    cursor.execute(f"INSERT INTO produto (produto, quantidade, descrição) VALUES ('{produto}',{quantidade},'{descrição}')")
    conn.commit()


criar_usuario('Pedro', 4388229091,'29/04/2005', 'Masculino', 51997891920)
criar_usuario('Laura', 322320091,'02/01/2000', 'Feminino', 5199891289)
criar_usuario('Rodrigo', 954762722,'04/02/1992', 'Masculino', 479925328)
criar_usuario('Alice', 88842722,'12/06/2002', 'Feminino', 512763049)

criar_produto('Chaleira', 50, 'Chaleira inox metálica.')
criar_produto('Camiseta', 100, 'Camisetas basicas do P ao GG.')
criar_produto('Camera', 15, 'Indicado para gravações profissionais.')
criar_produto('Liquidificador', 40, 'Completo e compacto.')
criar_produto('Calça jogger', 20, 'Calça leve e colada.')
criar_produto('Meia preta', 17, 'Meia tamanho médio.')

vendas('Camiseta', 2, 954762722, 4 )
vendas('Meia preta', 6, 954762722, 5 )
vendas('Liquidificador', 4, 322320091, 6 )
vendas('Camera', 3, 88842722, 11)
vendas('Camiseta', 2, 4388229091, 14 )


def list_all():
    print('Tabela de cliente\n')
    cursor.execute("SELECT * FROM cliente")
    for row in cursor.fetchall():
        print(row)

    print('\nTabela de produtos')
    cursor.execute("SELECT * FROM produto")
    for row in cursor.fetchall():
        print(row)

    print('\nTabela de vendas')
    cursor.execute("SELECT * FROM vendas")
    for row in cursor.fetchall():
        print(row)
list_all()