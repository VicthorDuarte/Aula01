from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timedelta
import bcrypt

# === CONFIGURAÇÕES ===
SECRET_KEY = "123"
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
    nome: str = Field(...,title='Nome do usuario', example='Ricardo',  description='Nome definido pelo usuario.')
    senha: str = Field(...,title='Senha do usuario', example='123', description='Senha definida pelo usuario.')

class UsuarioSaida(BaseModel):
    id: int = Field(title='ID do usuario', example='1')
    nome: str = Field(title='Nome do usuario', example='Matheus')

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str = Field(title='Token de acesso', example='$2b$12$XJ2/iMRtD4lQaa.KnJRZQ./esE5TenhGIU5fW.ElkcvV2GB.YNQkC')
    token_type: str = Field(title='Tipo do token de acesso', example='Tipo do token de acesso')

# === FASTAPI ===
app = FastAPI(title='Documentação Api',description='Manual de uso da Api.',version='1.0.0',docs_url='/Swagger',openapi_url='/arquvoapi.json')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# === UTILS ===
def obter_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def obter_usuario_por_nome(db: Session, nome: str):
    return db.query(UsuarioDB).filter(UsuarioDB.nome == nome).first()

with open("Chaveprivada.pem", "r") as f:
    PRIVATE_KEY = f.read()
with open("certificado.pem", "r") as f:
    CERT_PUBLIC_KEY = f.read()

# Geração do token
def criar_token(usuario: UsuarioDB):
    expira = datetime.utcnow() + timedelta(minutes=ACESSO_EXPIRA_MIN)
    dados = {"sub": usuario.nome, "exp": expira}
    return jwt.encode(dados, PRIVATE_KEY, algorithm="RS256")

# Validação do token
def verificar_token(token: str = Depends(oauth2_scheme), db: Session = Depends(obter_sessao)) -> UsuarioDB:
    try:
        payload = jwt.decode(token, CERT_PUBLIC_KEY, algorithms=["RS256"])
        nome = payload.get("sub")
        if nome is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        usuario = obter_usuario_por_nome(db, nome)
        if usuario is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        return usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


    #--- ROTAS---Authorization: Bearer <token>
@app.post("/registro", response_description='Usuario criado com sucesso!',summary='Registrar um usuario.', description='Registra um usuario novo, se ja existe algum usuario com seus dados ou seu usuario for invalido, ele apresentará um erro.', response_model=UsuarioSaida)
def registrar(usuario: Usuario, db: Session = Depends(obter_sessao)):
    if obter_usuario_por_nome(db, usuario.nome):
        raise HTTPException(status_code=400, detail="Usuario já existe")
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

@app.get("/me", response_description='Verificação concluida com sucesso!', summary='Verificar meu própio usuario.', response_model=UsuarioSaida)
def ler_me(usuario: UsuarioDB = Depends(verificar_token)):
    return usuario

@app.get("/usuarios", response_model=list[UsuarioSaida], description='Verificar quais os usuarios registrados no banco de dados.', summary='Listar usuarios cadastrados.', response_description='Usuarios listados com sucesso!')
def listar(db: Session = Depends(obter_sessao), usuario: UsuarioDB = Depends(verificar_token)):
    return db.query(UsuarioDB).all()


@app.put("/usuarios/{usuario_id}", response_model=UsuarioSaida,summary='Atualizar dados de um usuario.',response_description='Usuario atualizado com sucesso!',description='Atualiza dados de um usuario através de seu id cadastrado no banco de dados.')
def atualizar(usuario_id: int, dados: Usuario, db: Session = Depends(obter_sessao), usuario_atual: UsuarioDB = Depends(verificar_token)):
    usuario = db.query(UsuarioDB).get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.nome = dados.nome
    usuario.senha_hash = bcrypt.hashpw(dados.senha.encode(), bcrypt.gensalt()).decode()
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}",description='Deletar um usuario através de seu id cadastrado no banco de dados', summary='Deletar um usuario por id.', response_description='Usuario deletado com sucessso!')
def deletar(usuario_id: int, db: Session = Depends(obter_sessao), usuario_atual: UsuarioDB = Depends(verificar_token)):
    usuario = db.query(UsuarioDB).get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário deletado"}