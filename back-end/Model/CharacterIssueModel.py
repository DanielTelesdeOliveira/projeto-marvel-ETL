from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class Character_Issue(Base):
    __tablename__ = "character_issue"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    issue_id = Column(Integer, ForeignKey("Issue.id", ondelete="CASCADE"))
    