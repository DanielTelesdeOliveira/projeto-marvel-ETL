from Service import CharacterService
from Schema.CharacterResponse import CharacterResponse, CharacterListResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/characters",
    tags=["Characters"] # Organiza a documentação automática
)

service = CharacterService()

@router.get("/")
async def character_root():
    return {"message": "Hello World!! Characters Homepage!"}

@router.get("/show", response_model=list[CharacterListResponse])
def list_characters(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/show/{character_id}", response_model=CharacterResponse)
def get_character(character_id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, character_id)
