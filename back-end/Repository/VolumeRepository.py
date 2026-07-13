from Model.VolumeModel import Volume

class VolumeRepository:
    def find_all(self, db):
        volumes_list = db.query(Volume).all()
        return volumes_list
    
    def find_by_id(self, db, id):
        volume = db.query(Volume).filter(Volume.id == id).first()
        return volume
