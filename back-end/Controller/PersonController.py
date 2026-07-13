from Service.PersonService import PersonService
from Schema.PersonSchema import PersonResponse, PersonListResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/person",
    tags=["Person"] # Organiza a documentação automática
)

service = PersonService()

@router.get("/")
async def person_root():
    return {"message": "Hello World!! Person Homepage!"}

@router.get("/show", response_model=list[PersonListResponse])
def list_people(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/show/{person_id}", response_model=PersonResponse)
def get_person_by_id(person_id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, person_id)
