from Model import Volume, Issue
from sqlalchemy.orm import selectinload

class VolumeRepository:
    def find_all(self, db):
        volumes_list = db.query(Volume).all()
        return volumes_list
    
    def find_by_id(self, db, id):
        volume = (db.query(Volume)
                  .options(selectinload(Volume.issues).selectinload(Issue.characters),
                           selectinload(Volume.issues).selectinload(Issue.credits))
                  .filter(Volume.id == id).first())
        return volume
