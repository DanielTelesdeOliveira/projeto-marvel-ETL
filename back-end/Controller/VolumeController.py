from Service.VolumeService import VolumeService
from Schema.VolumeSchema import VolumeResponse
from Schema.ReferenceSchema import VolumeReferenceResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from database import get_db

router = APIRouter(
    prefix="/volume",
    tags=["Volume"]
)

service = VolumeService()

@router.get("/")
async def volume_root():
    return {"message": "Volume homepage!!"}

@router.get("/show", response_model=list[VolumeReferenceResponse])
async def list_volumes(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/show/{volume_id}", response_model=VolumeResponse)
async def get_volume_by_id(volume_id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, volume_id)
