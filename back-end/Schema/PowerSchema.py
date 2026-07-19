from pydantic import BaseModel, ConfigDict

class PowerListResponse(BaseModel): 
    name: str

    model_config = ConfigDict(from_attributes=True)

    