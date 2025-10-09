from fastapi import APIRouter
from database import db_dependency
from services import awardMapping_service as awardMappingService
from schema.awardMapping import AwardMappingBase, AwardMappingResponse, AwardMappingDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[AwardMappingResponse])
def get_awardMapping(db: db_dependency, user: user_dependency):
    return awardMappingService.get_awardMapping(db)

@router.post("/")
def create_awardMapping(new_awardMapping: AwardMappingBase, db: db_dependency, user: user_dependency):
    return awardMappingService.create_awardMapping(new_awardMapping, db, user)

@router.put("/{awardMapping_id}")
def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingBase, db: db_dependency, user: user_dependency):
    return awardMappingService.update_awardMapping(awardMapping_id, updated_awardMapping, db, user)

@router.delete("/{awardMapping_id}")
def delete_awardMapping(awardMapping_id: int, awardMapping_delete: AwardMappingDelete, db: db_dependency, user: user_dependency):
    return awardMappingService.delete_awardMapping(awardMapping_id, awardMapping_delete, db, user)