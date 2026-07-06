from Repository import CharacterRepository
from fastapi import HTTPException

class CharacterService:
    def __init__(self):
        self.repository = CharacterRepository()

    def get_all(self, db):
        character_list = self.repository.find_all(db)
        return character_list

    def get_by_id(self, id, db):
        if id <= 0:
            raise HTTPException(status_code=400, detail="Invalid character id")
        
        character = self.repository.find_by_id(db, id)

        if character is None:
            raise HTTPException(status_code=404, detail="Character not found")
        
        return character