import pytest 
import Model
from main import app
from database import Base, get_db
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(name="session")
def session_fixture():
    #Criacao das tabelas em memoria antes dos testes
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        character_1 = Model.CharacterModel.Character(id=1, name="Tony Stark", description="Tony Stark was the arrogant son of wealthy, weapon manufacturer Howard Stark.")
        character_2 = Model.CharacterModel.Character(id=2, name="Peter Parker", description="Peter Parker was bitten by a radioactive spider as a teenager, granting him spider-like powers.")
        person_1 = Model.PersonModel.Person(id=1, name="Stan Lee")
        person_2 = Model.PersonModel.Person(id=2, name="Jack Kirby")
        char_person_1 = Model.CharacterCreatorModel.Character_Creator(id=1,character_id=1, creator_id=1)
        char_person_2 = Model.CharacterCreatorModel.Character_Creator(id=2,character_id=2, creator_id=2)
        db.add_all([character_1, character_2, person_1, person_2, char_person_1, char_person_2])
        db.commit()
        yield db
    finally:
        db.close()
        #Limpa o banco na memoria apos cada teste
        Base.metadata.drop_all(bind=engine)    

@pytest.fixture(name="client")
def client_fixture(session):
    def override_get_db():
        yield session

    #Substitui o banco real pelo da memoria
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

