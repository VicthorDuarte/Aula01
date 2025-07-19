from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime, timedelta
import bcrypt

# === CONFIGURAÇÕES ===
SECRET_KEY = "minha_chave_jwt_supersecreta"
ALGORITHM = "HS256"
ACESSO_EXPIRA_MIN = 30

# === BANCO DE DADOS ===
SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# === MODELO SQLALCHEMY ===
class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    senha_hash = Column(String)

Base.metadata.create_all(bind=engine)

# === MODELO Pydantic ===
class Usuario(BaseModel):
    nome: str
    senha: str

class UsuarioSaida(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# === FASTAPI ===
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# === UTILS ===
def obter_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def criar_token(usuario: UsuarioDB):
    expira = datetime.utcnow() + timedelta(minutes=ACESSO_EXPIRA_MIN)
    dados = {"sub": usuario.nome, "exp": expira}
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

def obter_usuario_por_nome(db: Session, nome: str):
    return db.query(UsuarioDB).filter(UsuarioDB.nome == nome).first()

def verificar_token(token: str = Depends(oauth2_scheme), db: Session = Depends(obter_sessao)) -> UsuarioDB:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        nome = payload.get("sub")
        if nome is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        usuario = obter_usuario_por_nome(db, nome)
        if usuario is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        return usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# === ROTAS ===

@app.post("/registro", response_model=UsuarioSaida)
def registrar(usuario: Usuario, db: Session = Depends(obter_sessao)):
    if obter_usuario_por_nome(db, usuario.nome):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    senha_hash = bcrypt.hashpw(usuario.senha.encode(), bcrypt.gensalt()).decode()
    novo = UsuarioDB(nome=usuario.nome, senha_hash=senha_hash)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(obter_sessao)): # injeto depends() na variavel form  e na variavel db
    usuario = obter_usuario_por_nome(db, form.username)
    if not usuario or not bcrypt.checkpw(form.password.encode(), usuario.senha_hash.encode()):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token(usuario)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=UsuarioSaida)
def ler_me(usuario: UsuarioDB = Depends(verificar_token)):
    return usuario

@app.get("/usuarios", response_model=list[UsuarioSaida])
def listar(db: Session = Depends(obter_sessao), usuario: UsuarioDB = Depends(verificar_token)):
    return db.query(UsuarioDB).all()

@app.put("/usuarios/{usuario_id}", response_model=UsuarioSaida)
def atualizar(usuario_id: int, dados: Usuario, db: Session = Depends(obter_sessao), usuario_atual: UsuarioDB = Depends(verificar_token)):
    usuario = db.query(UsuarioDB).get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.nome = dados.nome
    usuario.senha_hash = bcrypt.hashpw(dados.senha.encode(), bcrypt.gensalt()).decode()
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}")
def deletar(usuario_id: int, db: Session = Depends(obter_sessao), usuario_atual: UsuarioDB = Depends(verificar_token)):
    usuario = db.query(UsuarioDB).get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário deletado"}