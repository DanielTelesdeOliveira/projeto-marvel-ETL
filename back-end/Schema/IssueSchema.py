from pydantic import BaseModel, ConfigDict

class IssueResponse(BaseModel):
    id: int
    name: str
    number: int

    model_config = ConfigDict(from_attributes=True)

class IssueListResponse(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)