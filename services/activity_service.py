from repository import activity_repo as activity_repo
from database import db_dependency
from schema.activity import ActivityCreate, ActivityUpdate

def get_activity(db: db_dependency):
    return activity_repo.get_activitys(db)

def create_activity(new_activity: ActivityCreate, db: db_dependency):
    return activity_repo.create_activity(new_activity, db)

def update_activity(activity_id: int, updated_activity: ActivityUpdate, db: db_dependency):
    return activity_repo.update_activity(activity_id, updated_activity, db)

def delete_activity(activity_id: int, db: db_dependency):
    return activity_repo.delete_activity(activity_id, db)