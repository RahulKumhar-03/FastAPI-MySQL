from fastapi import APIRouter
from database import db_dependency
from services import award_service as awardService
from schema.award import AwardCreate, AwardUpdate

router = APIRouter()

@router.get("/")
def get_award(db: db_dependency):
    return awardService.get_award(db)

@router.post("/")
def create_award(new_award: AwardCreate, db: db_dependency):
    return awardService.create_award(new_award, db)

@router.put("/{award_id}")
def update_award(award_id: int, updated_award: AwardUpdate, db: db_dependency):
    return awardService.update_award(award_id, updated_award, db)

@router.delete("/{award_id}")
def delete_award(award_id: int, db: db_dependency):
    return awardService.delete_award(award_id, db)