from repository import activityMapping_repo as activityMapping_repo
from database import db_dependency
from schema.activityMapping import ActivityMappingBase, ActivityMappingDelete

def get_activityMapping(db: db_dependency):
    return activityMapping_repo.get_activityMapping(db)

def create_activityMapping(new_activityMapping: ActivityMappingBase, db: db_dependency, currentUser):
    return activityMapping_repo.create_activityMapping(new_activityMapping, db, currentUser)

def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingBase, db: db_dependency, currentUser):
    return activityMapping_repo.update_activityMapping(activityMapping_id, updated_activityMapping, db, currentUser)

def delete_activityMapping(activityMapping_id: int, activityMapping_delete: ActivityMappingDelete, db: db_dependency, currentUser):
    return activityMapping_repo.delete_activityMapping(activityMapping_id, activityMapping_delete, db, currentUser)