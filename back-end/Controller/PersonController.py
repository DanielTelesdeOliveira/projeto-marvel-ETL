from Model import Person
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from database import get_db

router = APIRouter(
    prefix="/person",
    tags=["Person"] # Organiza a documentação automática
)

@router.get("/")
async def person_root():
    return {"message": "Hello World!! Person Homepage!"}

@router.get("/show")
def list_person(db: Session = Depends(database.get_db)):
    person_list = db.query(Person).all()
    return person_list

@router.get("/show/{person_id}")
def get_person(person_id: int, db: Session = Depends(database.get_db)):
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person
