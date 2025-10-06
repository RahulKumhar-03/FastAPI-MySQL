from fastapi import APIRouter
from database import db_dependency
from services import activity_service as activityService
from schema.activity import ActivityCreate, ActivityUpdate, ActivityResponse

router = APIRouter()

@router.get("/", response_model=list[ActivityResponse])
def get_activity(db: db_dependency):
    return activityService.get_activity(db)

@router.post("/")
def create_activity(new_activity: ActivityCreate, db: db_dependency):
    return activityService.create_activity(new_activity, db)

@router.put("/{activity_id}")
def update_activity(activity_id: int, updated_activity: ActivityUpdate, db: db_dependency):
    return activityService.update_activity(activity_id, updated_activity, db)

@router.delete("/{activity_id}")
def delete_activity(activity_id: int, db: db_dependency):
    return activityService.delete_activity(activity_id, db)