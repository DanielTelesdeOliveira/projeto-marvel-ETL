from pydantic import BaseModel, ConfigDict

class VolumeResponse(BaseModel):
    id: int
    name: str
    issue_quantity: int

    model_config = ConfigDict(from_attributes=True)

class VolumeListResponse(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)