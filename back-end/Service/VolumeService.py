from Repository.VolumeRepository import VolumeRepository
from fastapi import HTTPException

class VolumeService:
    def __init__(self):
        self.repository = VolumeRepository()

    def get_all(self, db):
        volumes_list = self.repository.find_all(db)
        return volumes_list
    
    def get_by_id(self, db, id):
        if id < 0:
            raise HTTPException(status_code=400, detail="Invalid volume id")
        
        volume = self.repository.find_by_id(db, id)

        if volume is None:
            raise HTTPException(status_code=404, detail="Volume not found")
        
        return volume