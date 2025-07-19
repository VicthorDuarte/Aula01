from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

#chave secreta
app.config['SECRET_KEY'] = 'lucas2905'

#Usuarios  fixos para simular login
usuarios = {
    'admin': 'senha123',
    'joao' : 'teste'
}

def token_obrigatorio(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
        if bearer.startswith('Bearer'):
            token = bearer.split(' ')[1]
        if not token:
            return jsonify({'erro': 'Token ausente'})
        try:
            dados = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256'])
            usuario = dados['usuario']
        except jwt.ExpiredSignatureError:
            return jsonify({'erro': 'token expirado'}), 401
        except Exception as e:
            return jsonify ({'erro': f'token invalido: {str(e)}'}), 401
        return f(usuario,*args, **kwargs)
    return decorada

#Rote de login> retorna um jwt
@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    if not usuario  or not senha or usuarios.get(usuario) != senha:
        return jsonify({"Erro": " Credenciais invalidas!"})
    
    token = jwt.encode({"usuario": usuario, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token' : token})


#Endpoint protegido por token
@app.route('/protegida', methods=['GET'])
@token_obrigatorio
def rota_segura(usuario):
    return jsonify({'Mensagem': f'Bem vindo {usuario}!'})


# rodar app
if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0" )
    


    