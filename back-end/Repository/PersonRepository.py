from Model import Person
from sqlalchemy.orm import selectinload
class PersonRepository:
    def find_all(self, db):
        people_list = db.query(Person).all()
        return people_list
    
    def find_by_id(self, db, id):
        person = (db.query(Person)
                  .options(selectinload(Person.characters),
                           selectinload(Person.credits))
                  .filter(Person.id == id).first())
        return person