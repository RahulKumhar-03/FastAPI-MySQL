from fastapi import APIRouter
from database import db_dependency
from services import skillValidatedMapping_service as skillValidatedMappingService
from schema.skillValidatedMapping import SkillValidatedMappingBase, SkillValidatedMappingResponse, SkillValidatedMappingDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[SkillValidatedMappingResponse])
def get_skillValidatedMapping(db: db_dependency, user: user_dependency):
    return skillValidatedMappingService.get_skillValidatedMapping(db)

@router.post("/")
def create_skillValidatedMapping(new_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, user: user_dependency):
    return skillValidatedMappingService.create_skillValidatedMapping(new_skillValidatedMapping, db, user)

@router.put("/{skillValidatedMapping_id}")
def update_skillValidatedMapping(skillValidatedMapping_id: int, updated_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, user: user_dependency):
    return skillValidatedMappingService.update_skillValidatedMapping(skillValidatedMapping_id, updated_skillValidatedMapping, db, user)

@router.delete("/{skillValidatedMapping_id}")
def delete_skillValidatedMapping(skillValidatedMapping_id: int, skillValidatedMapping_delete: SkillValidatedMappingDelete, db: db_dependency, user: user_dependency):
    return skillValidatedMappingService.delete_skillValidatedMapping(skillValidatedMapping_id, skillValidatedMapping_delete, db, user)