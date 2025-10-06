from fastapi import APIRouter
from database import db_dependency
from services import skillValidated_service as skillValidatedService
from schema.skillValidated import SkillValidatedCreate, SkillValidatedUpdate, SkillValidatedResponse, SkillValidatedDelete

router = APIRouter()

@router.get("/", response_model=list[SkillValidatedResponse])
def get_skillValidated(db: db_dependency):
    return skillValidatedService.get_skillValidated(db)

@router.post("/")
def create_skillValidated(new_skillValidated: SkillValidatedCreate, db: db_dependency):
    return skillValidatedService.create_skillValidated(new_skillValidated, db)

@router.put("/{skillValidated_id}")
def update_skillValidated(skillValidated_id: int, updated_skillValidated: SkillValidatedUpdate, db: db_dependency):
    return skillValidatedService.update_skillValidated(skillValidated_id, updated_skillValidated, db)

@router.delete("/{skillValidated_id}")
def delete_skillValidated(skillValidated_id: int, skillValidated_delete: SkillValidatedDelete,  db: db_dependency):
    return skillValidatedService.delete_skillValidated(skillValidated_id, skillValidated_delete, db)