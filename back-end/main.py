from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import Model
from Controller import CharacterController, PersonController

database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:8000", "http://127.0.0.1:5500"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
                   )

app.include_router(CharacterController.router)
app.include_router(PersonController.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

