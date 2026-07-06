from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Cria arquivo local para desenvolvimento
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Depedencias que a FastAPI ira usar nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    