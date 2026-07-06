from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class Character_Person(Base):
    __tablename__ = "character_person"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    person_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"))
    