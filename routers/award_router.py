from fastapi import APIRouter
from database import db_dependency
from services import award_service as awardService
from schema.award import AwardBase, AwardResponse, AwardDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[AwardResponse])
def get_award(db: db_dependency, user: user_dependency):
    return awardService.get_award(db)

@router.post("/")
def create_award(new_award: AwardBase, db: db_dependency, user: user_dependency):
    return awardService.create_award(new_award, db, user)

@router.put("/{award_id}")
def update_award(award_id: int, updated_award: AwardBase, db: db_dependency, user: user_dependency):
    return awardService.update_award(award_id, updated_award, db, user)

@router.delete("/{award_id}")
def delete_award(award_id: int, award_delete: AwardDelete, db: db_dependency, user: user_dependency):
    return awardService.delete_award(award_id, award_delete, db, user)