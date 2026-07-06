from pydantic import BaseModel

class CharacterResponse(BaseModel):
    id: int
    name: str
    description: str

    #Permite que o Pydanyic leia objetos Python
    class Config:
        from_attributes = True

class CharacterListResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True