from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Issue(Base):
    __tablename__ = "Issue"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)

    characters = relationship("Character", secondary="character_issue", back_populates="issues")