from Model import Character
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from database import get_db

router = APIRouter(
    prefix="/characters",
    tags=["Characters"] # Organiza a documentação automática
)

@router.get("/")
async def character_root():
    return {"message": "Hello World!! Characters Homepage!"}

@router.get("/show")
def list_characters(db: Session = Depends(database.get_db)):
    characters_list = db.query(Character).all()
    return characters_list

@router.get("/show/{character_id}")
def get_character(character_id: int, db: Session = Depends(database.get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character
