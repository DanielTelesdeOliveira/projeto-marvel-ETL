from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship 
from database import Base

class Power(Base):
    __tablename__ = "powers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    characters = relationship("Character", secondary="character_powers", back_populates="powers")