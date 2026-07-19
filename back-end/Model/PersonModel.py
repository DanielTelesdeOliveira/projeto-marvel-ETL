from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    characters = relationship("Character", secondary="character_creator", back_populates="creators")
