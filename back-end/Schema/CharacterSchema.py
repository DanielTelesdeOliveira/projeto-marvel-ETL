from pydantic import BaseModel, ConfigDict

class CharacterResponse(BaseModel):
    id: int
    name: str
    description: str

    #Permite que o Pydanyic leia objetos Python
    model_config = ConfigDict(from_atrributes=True)

class CharacterListResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_atrributes=True)