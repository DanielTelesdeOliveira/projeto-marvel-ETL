from Service.IssueService import IssueService
from Schema.IssueSchema import IssueResponse
from Schema.ReferenceSchema import IssueReferenceResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/issue",
    tags=["Issue"]
)

service = IssueService()

@router.get("/")
async def issue_root():
    return {"message": "Issue homepage!!"}

@router.get("/show", response_model=list[IssueReferenceResponse])
async def list_issues(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/show/{issue_id}", response_model=IssueResponse)
async def get_issue_by_id(issue_id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, issue_id)