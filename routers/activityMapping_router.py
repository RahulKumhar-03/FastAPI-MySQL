from fastapi import APIRouter
from database import db_dependency
from services import activityMapping_service as activityMappingService
from schema.activityMapping import ActivityMappingCreate, ActivityMappingUpdate, ActivityMappingResponse, ActivityMappingDelete

router = APIRouter()

@router.get("/", response_model=list[ActivityMappingResponse])
def get_activityMapping(db: db_dependency):
    return activityMappingService.get_activityMapping(db)

@router.post("/")
def create_activityMapping(new_activityMapping: ActivityMappingCreate, db: db_dependency):
    return activityMappingService.create_activityMapping(new_activityMapping, db)

@router.put("/{activityMapping_id}")
def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingUpdate, db: db_dependency):
    return activityMappingService.update_activityMapping(activityMapping_id, updated_activityMapping, db)

@router.delete("/{activityMapping_id}")
def delete_activityMapping(activityMapping_id: int, activity_delete: ActivityMappingDelete, db: db_dependency):
    return activityMappingService.delete_activityMapping(activityMapping_id, activity_delete, db)