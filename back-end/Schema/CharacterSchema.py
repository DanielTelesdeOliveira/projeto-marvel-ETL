from pydantic import BaseModel, ConfigDict
from .ReferenceSchema import PersonReferenceResponse, IssueReferenceResponse
from .PowerSchema import PowerListResponse

class CharacterResponse(BaseModel):
    id: int
    name: str
    description: str
    
    issues: list[IssueReferenceResponse]
    creators: list[PersonReferenceResponse]
    powers: list[PowerListResponse]

    #Permite que o Pydanyic leia objetos Python
    model_config = ConfigDict(from_attributes=True)

class CharacterListResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)