from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "victhor"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
db = SQLAlchemy(app)

# Modelo de usuário no banco
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(80), nullable=False)
    escopo = db.Column(db.  String(20), nullable=False)  # 'admin' ou 'comum'

with app.app_context():
    db.create_all()

# Decorador para verificar token e escopo
def token_necessario(escopo_requerido=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                bearer = request.headers['Authorization']
                if bearer.startswith("Bearer "):
                    token = bearer.split(" ")[1]
            if not token:
                return jsonify({"erro": "Token ausente"}), 403
            try:
                payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
                if escopo_requerido and payload["escopo"] != escopo_requerido:
                    return jsonify({"erro": "Permissão negada"}), 403
                request.usuario_logado = payload
            except jwt.ExpiredSignatureError:
                return jsonify({"erro": "Token expirado"}), 401
            except Exception as e:
                return jsonify({"erro": f"Token inválido: {str(e)}"}), 401
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Login e geração de token
@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    nome = dados.get("nome")
    senha = dados.get("senha")
    usuario = Usuario.query.filter_by(nome=nome, senha=senha).first()

    if not usuario:
        return jsonify({"erro": "Credenciais inválidas"}), 401

    token = jwt.encode({
        "id": usuario.id,
        "nome": usuario.nome,
        "escopo": usuario.escopo,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token})

# Cadastro público (inicial)
@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.get_json()
    novo = Usuario(nome=dados["nome"], senha=dados["senha"], escopo="admin")
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado"}), 201

# Listar usuários (apenas admin)
@app.route("/usuarios", methods=["GET"])
@token_necessario(escopo_requerido="admin")
def listar1():
    todos = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome, "escopo": u.escopo} for u in todos])


@app.route("/usuarios/<int:id>", methods=["GET"])
@token_necessario(escopo_requerido="admin")
def listar2(id):
    dados = request.get_json()
    usuario = Usuario.query.get(id)
    usuario.nome = dados.get("nome", usuario.nome)
    usuario.escopo = dados.get("escopo", usuario.escopo)
    return jsonify({"id": id, "nome": usuario.nome, "escopo": usuario.escopo})



# Atualizar um usuário (admin)
@app.route("/usuarios/<int:id>", methods=["PUT"])
@token_necessario("admin")
def atualizar(id):
    dados = request.get_json()
    usuario = Usuario.query.get_or_404(id)
    usuario.nome = dados.get("nome", usuario.nome)
    usuario.escopo = dados.get("escopo", usuario.escopo)
    db.session.commit()
    return jsonify({"mensagem": "Usuário atualizado"})

# Deletar usuário (admin)
@app.route("/usuarios/<int:id>", methods=["DELETE"])
@token_necessario("admin")
def deletar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário deletado"})

# Rota protegida para usuários comuns ou admins
@app.route("/me", methods=["GET"])
@token_necessario()
def perfil():
    return jsonify(request.usuario_logado)

if __name__ == "__main__":
    app.run(debug=True)