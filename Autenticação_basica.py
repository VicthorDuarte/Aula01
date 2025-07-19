from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

usuarios = {
    'Admin' : 'senha123',
    'joao' : '123'
}

@auth.verify_password
def verificar(usuario,senha):
    return usuarios.get(usuario) == senha

@app.route('/Admin1')
@auth.login_required
def acesso_admin():
    if auth.current_user() == 'Admin':
        return(f'Olá, Usuario {auth.current_user()}! Bem vindo ao painel de controle', 200)
    elif auth.current_user != 'Admin':
        return(f'Olá, Usuário {auth.current_user()} voce não tem acesso ao painel admin.', 403)
    else:
        raise Exception

@app.route('/usuario')
@auth.login_required
def rota_segura():
        return(f'Olá, Usuário {auth.current_user()}')

if __name__ == '__main__':
    app.run(debug=True)