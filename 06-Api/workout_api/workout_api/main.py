from pyngrok import ngrok
import nest_asyncio
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate, Params
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
import uvicorn

nest_asyncio.apply()

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  # Use SQLite para simplicidade
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class AtletaModel(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    centro_treinamento = Column(String)
    categoria = Column(String)


Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco de dados


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de dados para entrada e saída


class AtletaBase(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str


class AtletaCreate(AtletaBase):
    pass


class Atleta(AtletaBase):
    id: int

    class Config:
        orm_mode = True


@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}


@app.post("/atletas/", response_model=Atleta)
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    db_atleta = AtletaModel(**atleta.dict())
    db.add(db_atleta)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    db.refresh(db_atleta)
    return db_atleta


@app.get("/atletas/", response_model=Page[Atleta])
def read_atletas(
    nome: Optional[str] = None,
    cpf: Optional[str] = None,
    params: Params = Depends(),
    db: Session = Depends(get_db)
):
    query = db.query(AtletaModel)
    if nome:
        query = query.filter(AtletaModel.nome == nome)
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)
    return paginate(query.all(), params)


@app.get("/atletas/{atleta_id}", response_model=Atleta)
def read_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = db.query(AtletaModel).filter(AtletaModel.id == atleta_id).first()
    if atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta


# Configuração do ngrok
# Substitua pelo seu token do ngrok
ngrok.set_auth_token('2k0xhK1I6JnJ4gNqSm5KdU14d5C_6qZ2T7Lsjt6Kt9XaeyHk9')
public_url = ngrok.connect(8000)
print(f"API disponível em: {public_url}")

# Rodar o servidor no ambiente do notebook
uvicorn.run(app, host="0.0.0.0", port=8000)
