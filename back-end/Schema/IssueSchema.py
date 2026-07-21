from pydantic import BaseModel, ConfigDict
from .IssueCreditSchema import IssueCreditPersonResponse, IssueCreditIssueResponse
from .ReferenceSchema import CharacterReferenceResponse, VolumeReferenceResponse


class IssueResponse(BaseModel):
    id: int
    name: str
    number: int
    
    characters: list[CharacterReferenceResponse]
    credits: list[IssueCreditPersonResponse]
    volume: VolumeReferenceResponse

    model_config = ConfigDict(from_attributes=True)

class IssueListResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class IssueVolumeResponse(BaseModel):
    id: int
    name: str
    number: int

    characters: list[CharacterReferenceResponse]
    credits: list[IssueCreditPersonResponse]

    model_config = ConfigDict(from_attributes=True)