from Repository.IssueRepository import IssueRepository
from fastapi import HTTPException

class IssueService:
    def __init__(self):
        self.repository = IssueRepository()

    def get_all(self, db):
        issue_list = self.repository.find_all(db)
        return issue_list

    def get_by_id(self, db, id):
        if id < 0:
            raise HTTPException(status_code=400, detail="Invalid issue id")

        issue = self.repository.find_by_id(db, id)    

        if issue is None:
            raise HTTPException(status_code=404, detail="Issue not found")
        
        return issue