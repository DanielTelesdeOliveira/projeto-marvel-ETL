from pydantic import BaseModel, ConfigDict
from .ReferenceSchema import PersonReferenceResponse, IssueReferenceResponse

class IssueCreditIssueResponse(BaseModel):
    issue: IssueReferenceResponse
    person_role: str

    model_config = ConfigDict(from_attributes=True)

class IssueCreditPersonResponse(BaseModel):
    person: PersonReferenceResponse
    person_role: str

    model_config = ConfigDict(from_attributes=True)