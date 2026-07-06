from fastapi import HTTPException
from Model import Character

class CharacterRepository:
    def find_all(self, db):
        characters_list = db.query(Character).all()
        return characters_list
    
    def find_by_id(self, db, id):
        character = db.query(Character).filter(Character.id == id).first()
        return character
        