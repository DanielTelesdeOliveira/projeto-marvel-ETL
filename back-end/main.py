from fastapi import FastAPI
import database
import Model
from Controller import CharacterController, PersonController

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(CharacterController.router)
app.include_router(PersonController.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

