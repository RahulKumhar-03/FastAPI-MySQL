from fastapi import APIRouter
from database import db_dependency
from services import activity_service as activityService
from schema.activity import ActivityCreate, ActivityBase, ActivityResponse, ActivityDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[ActivityResponse])
def get_activity(db: db_dependency, user: user_dependency):
    return activityService.get_activity(db)

@router.post("/")
def create_activity(new_activity: ActivityCreate, db: db_dependency, user: user_dependency):
    return activityService.create_activity(new_activity, db, user)

@router.put("/{activity_id}")
def update_activity(activity_id: int, updated_activity: ActivityBase, db: db_dependency, user: user_dependency):
    return activityService.update_activity(activity_id, updated_activity, db, user)

@router.delete("/{activity_id}")
def delete_activity(activity_id: int, activity_deleted: ActivityDelete, db: db_dependency, user: user_dependency):
    return activityService.delete_activity(activity_id, activity_deleted, db, user)