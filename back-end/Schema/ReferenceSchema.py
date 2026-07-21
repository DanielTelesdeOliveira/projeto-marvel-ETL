from pydantic import BaseModel, ConfigDict

class PersonReferenceResponse(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)

class CharacterReferenceResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class IssueReferenceResponse(BaseModel):
    id: int
    name: str
    number: int

    model_config = ConfigDict(from_attributes=True)

class VolumeReferenceResponse(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)
