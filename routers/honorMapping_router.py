from fastapi import APIRouter
from database import db_dependency
from services import honorMapping_service as honorMappingService
from schema.honorMapping import HonorMappingBase, HonorMappingResponse, HonorMappingDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[HonorMappingResponse])
def get_honorMapping(db: db_dependency, user: user_dependency):
    return honorMappingService.get_honorMapping(db)

@router.post("/")
def create_honorMapping(new_honorMapping: HonorMappingBase, db: db_dependency, user: user_dependency):
    return honorMappingService.create_honorMapping(new_honorMapping, db, user)

@router.put("/{honorMapping_id}")
def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingBase, db: db_dependency, user: user_dependency):
    return honorMappingService.update_honorMapping(honorMapping_id, updated_honorMapping, db, user)

@router.delete("/{honorMapping_id}")
def delete_honorMapping(honorMapping_id: int, honorMapping_delete: HonorMappingDelete, db: db_dependency, user: user_dependency):
    return honorMappingService.delete_honorMapping(honorMapping_id, honorMapping_delete, db, user)