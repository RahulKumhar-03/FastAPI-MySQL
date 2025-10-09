from fastapi import APIRouter
from database import db_dependency
from services import activityMapping_service as activityMappingService
from services.auth_service import user_dependency
from schema.activityMapping import ActivityMappingBase, ActivityMappingResponse, ActivityMappingDelete

router = APIRouter()

@router.get("/", response_model=list[ActivityMappingResponse])
def get_activityMapping(db: db_dependency, user: user_dependency):
    return activityMappingService.get_activityMapping(db)

@router.post("/")
def create_activityMapping(new_activityMapping: ActivityMappingBase, db: db_dependency, user: user_dependency):
    return activityMappingService.create_activityMapping(new_activityMapping, db, user)

@router.put("/{activityMapping_id}")
def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingBase, db: db_dependency, user: user_dependency):
    return activityMappingService.update_activityMapping(activityMapping_id, updated_activityMapping, db, user)

@router.delete("/{activityMapping_id}")
def delete_activityMapping(activityMapping_id: int, activity_delete: ActivityMappingDelete, db: db_dependency, user: user_dependency):
    return activityMappingService.delete_activityMapping(activityMapping_id, activity_delete, db, user)