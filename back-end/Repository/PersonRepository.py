from Model import Person

class PersonRepository:
    def find_all(self, db):
        people_list = db.query(Person).all()
        return people_list
    
    def find_by_id(self, db, id):
        person = db.query(Person).filter(Person.id == id).first()
        return person