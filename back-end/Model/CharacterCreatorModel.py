from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class Character_Creator(Base):
    __tablename__ = "character_creator"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    creator_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"))
    