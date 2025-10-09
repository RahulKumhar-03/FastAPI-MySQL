from repository import activity_repo as activity_repo
from database import db_dependency
from schema.activity import ActivityCreate, ActivityBase, ActivityDelete

def get_activity(db: db_dependency):
    return activity_repo.get_activitys(db)

def create_activity(new_activity: ActivityCreate, db: db_dependency, currentUser):
    return activity_repo.create_activity(new_activity, db, currentUser)

def update_activity(activity_id: int, updated_activity: ActivityBase, db: db_dependency, currentUser):
    return activity_repo.update_activity(activity_id, updated_activity, db, currentUser)

def delete_activity(activity_id: int, activity_tobe_deleted: ActivityDelete, db: db_dependency, currentUser):
    return activity_repo.delete_activity(activity_id, activity_tobe_deleted, db, currentUser)