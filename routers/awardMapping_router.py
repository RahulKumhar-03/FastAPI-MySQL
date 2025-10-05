from fastapi import APIRouter
from database import db_dependency
from services import awardMapping_service as awardMappingService
from schema.awardMapping import awardMappingCreate, AwardMappingUpdate

router = APIRouter()

@router.get("/")
def get_awardMapping(db: db_dependency):
    return awardMappingService.get_awardMapping(db)

@router.post("/")
def create_awardMapping(new_awardMapping: awardMappingCreate, db: db_dependency):
    return awardMappingService.create_awardMapping(new_awardMapping, db)

@router.put("/{awardMapping_id}")
def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingUpdate, db: db_dependency):
    return awardMappingService.update_awardMapping(awardMapping_id, updated_awardMapping, db)

@router.delete("/{awardMapping_id}")
def delete_awardMapping(awardMapping_id: int, db: db_dependency):
    return awardMappingService.delete_awardMapping(awardMapping_id, db)