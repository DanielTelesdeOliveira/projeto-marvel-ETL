from pydantic import BaseModel, ConfigDict
from .IssueSchema import IssueVolumeResponse

class VolumeResponse(BaseModel):
    id: int
    name: str
    issues_quantity: int
    
    issues: list[IssueVolumeResponse]

    model_config = ConfigDict(from_attributes=True)

class VolumeListResponse(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)