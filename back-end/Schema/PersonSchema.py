from pydantic import BaseModel, ConfigDict
from .ReferenceSchema import CharacterReferenceResponse
from .IssueCreditSchema import IssueCreditIssueResponse

class PersonResponse(BaseModel):
    id: int
    name: str

    characters: list[CharacterReferenceResponse]
    credits: list[IssueCreditIssueResponse]
    
    model_config = ConfigDict(from_attributes=True)

class PersonListResponse(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)