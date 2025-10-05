from fastapi import APIRouter
from database import db_dependency
from services import honorMapping_service as honorMappingService
from schema.honorMapping import HonorMappingCreate, HonorMappingUpdate

router = APIRouter()

@router.get("/")
def get_honorMapping(db: db_dependency):
    return honorMappingService.get_honorMapping(db)

@router.post("/")
def create_honorMapping(new_honorMapping: HonorMappingCreate, db: db_dependency):
    return honorMappingService.create_honorMapping(new_honorMapping, db)

@router.put("/{honorMapping_id}")
def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingUpdate, db: db_dependency):
    return honorMappingService.update_honorMapping(honorMapping_id, updated_honorMapping, db)

@router.delete("/{honorMapping_id}")
def delete_honorMapping(honorMapping_id: int, db: db_dependency):
    return honorMappingService.delete_honorMapping(honorMapping_id, db)