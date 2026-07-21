from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Issue(Base):
    __tablename__ = "Issue"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)
    volume_id = Column(Integer, ForeignKey("Volume.id",ondelete="CASCADE"))

    volume = relationship("Volume", back_populates="issues")
    characters = relationship("Character", secondary="character_issue", back_populates="issues")
    credits = relationship("Issue_Credit", back_populates="issue")