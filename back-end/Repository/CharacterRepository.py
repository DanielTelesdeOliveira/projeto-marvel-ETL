from Model import Character, Power, Character_Power,Person,Character_Creator,Issue,Character_Issue 
from sqlalchemy.orm import selectinload

class CharacterRepository:
    def find_all(self, db):
        characters_list = db.query(Character).all()
        return characters_list
    
    def find_by_id(self, db, id):
        character = (db.query(Character)
        .options(selectinload(Character.creators),
                 selectinload(Character.issues),
                 selectinload(Character.powers))
        .filter(Character.id == id).first())
        return character