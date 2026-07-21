from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Volume(Base):
    __tablename__ = "Volume"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    issues_quantity = Column(Integer)

    issues = relationship("Issue", back_populates="volume")