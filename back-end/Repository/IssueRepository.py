from Model.IssueModel import Issue
from sqlalchemy.orm import selectinload
class IssueRepository:
    def find_all(self, db):
        issue_list = db.query(Issue).all()
        return issue_list
    
    def find_by_id(self, db, id):
        issue = (db.query(Issue)
                 .options(selectinload(Issue.characters),
                          selectinload(Issue.credits),
                          selectinload(Issue.volume))
                .filter(Issue.id == id).first())
        return issue