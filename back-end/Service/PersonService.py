from Repository.PersonRepository import PersonRepository
from fastapi import HTTPException

class PersonService:
    def __init__(self):
        self.repository = PersonRepository()
    
    #Buscar todos
    def get_all(self, db):
        people_list = self.repository.find_all(db)
        return people_list
        
    def get_by_id(self, db, id):
        if id < 0:
            raise HTTPException(status_code=400, detail="Invalid person id")
        
        person = self.repository.find_by_id(db, id)

        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        
        return person
        

