from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Issue_Credit(Base):
    __tablename__ = "issue_credit"
    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("Issue.id", ondelete="CASCADE"))
    person_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"))
    person_role = Column(String)
    