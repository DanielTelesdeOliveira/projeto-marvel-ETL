from sqlalchemy import Column, Integer, String
from database import Base

class Issue(Base):
    __tablename__ = "Issue"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)
