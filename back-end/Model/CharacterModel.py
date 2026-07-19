from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    creators = relationship("Person", secondary="character_creator", back_populates="characters")
    issues = relationship("Issue", secondary="character_issue", back_populates="characters")
    powers = relationship("Power", secondary="character_powers", back_populates="characters")