from Model.IssueModel import Issue

class IssueRepository:
    def find_all(self, db):
        issue_list = db.query(Issue).all()
        return issue_list
    
    def find_by_id(self, db, id):
        issue = db.query(Issue).filter(Issue.id == id).first()
        return issue